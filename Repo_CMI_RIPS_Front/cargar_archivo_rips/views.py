# -*- coding: utf-8 -*-
import json
import boto3
import botocore.config
import ast
import base64
from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponseForbidden
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context_processors import csrf
from rips_base.settings import AWS_LAMBDA_DATOS, AWS_LAMBDA_ESTRUCTURA, \
    AWS_DEFAULT_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME, AWS_LAMBDA_GUARDADO
from cargar_archivo_rips.estado_lambda_enum import EstadoLambda
from validaciones.models import TripsRegistrosValidados as Registros
import cargar_archivo_rips.validacion_token as validar_token
from validaciones.models import TripsClientesEapb as Eapb
from validaciones.models import TripsDinamismo as Dinamismo
from django.db.models import Q


@xframe_options_exempt
def index(request):
    context = {}
    context.update(csrf(request))
    try:
        estado_token = validar_token.check(request.GET['token'], request.GET['cliente'], request.GET['prestador'])
        if estado_token['status']:
            cod_cliente = estado_token['data']['idCliente']
            dinamismo = obtener_valores_dinamismo(cod_cliente)
            datos = {"token": request.GET['token'], "dinamismo": dinamismo, "cliente_token": request.GET['cliente'],
                     "prestador_token": request.GET['prestador']}
            return render(request, 'paginas/index.html', {"datos": datos})
        else:
            return HttpResponseForbidden()
    except Exception as ex:
        raise Http404("Página no existe")


def cargar_archivo_rips(request):
    try:
        archivo = request.FILES['archivo_zip']
        datos = ast.literal_eval(request.POST['datos'])
        estado_token = validar_token.check(datos['token'], datos['cliente_token'], datos['prestador_token'])
        if estado_token['status'] == True:
            if archivo.size < 5242880:
                data = obtener_datos_token(estado_token, datos['dinamismo'])
                if archivo.name.lower().endswith('.zip'):
                    if not Registros.objects.filter(nmcodigo_prestador=estado_token['data']['codigoHabilitacion']).filter(dsnumero_remision=archivo.name[:-4]).exists():
                        if subir_archivo_s3(archivo) is not False:
                            lambda_estructura = invocar_lambda(archivo.name, AWS_LAMBDA_ESTRUCTURA, data,
                                                               EstadoLambda.ESTRUCTURA.obtener_descripcion())
                            if lambda_estructura is not False:
                                datos['nombre_zip'] = archivo.name
                                lambda_estructura['datos_extra'] = base64.b64encode(
                                    json.dumps(datos).encode('utf-8')).decode('utf-8')
                                print(lambda_estructura)
                                return JsonResponse(lambda_estructura)
                            return JsonResponse({'statusCode': 502,
                                                 'mensaje': "Ha ocurrido un error al validar la estructura del RIPS."})
                        return JsonResponse({'statusCode': 502, 'mensaje': "Internal server error in S3."})
                    else:
                        registro_rips = Registros.objects.filter(dsnumero_remision=archivo.name[:-4]).first()
                        return JsonResponse({'statusCode': 409,
                                             'mensaje': "El RIPS \"" + archivo.name[:-4] +
                                                        "\" ya fue validado y guardado exitosamente. Fecha: " +
                                                        str(registro_rips.fefecha_registro)[:10] + " Hora: " +
                                                        str(registro_rips.fefecha_registro)[10:16] + "."})
                return JsonResponse({'statusCode': 400,
                                     'mensaje': "RIPS inválido, por favor subir un archivo RIPS con extensión .zip."})
            else:
                return JsonResponse({'statusCode': 400, 'mensaje': 'RIPS inválido. El zip no debe pesar más de 5MB.'})
        else:
            return JsonResponse({'statusCode': 400, 'mensaje': 'La sesión ha caducado, por favor vuelve a Iniciar Sesión.'})

    except Exception as ex:
        return JsonResponse({'statusCode': 502, 'mensaje': "Error interno del server en la validación de estructura."})



def validar_datos_rips(request):
    try:
        if request.method == 'POST':
            datos = request.body.decode('utf-8')
            datos = json.loads(base64.b64decode(datos).decode('utf-8'))
            estado_token = validar_token.check(datos['token'], datos['cliente_token'],
                                               datos['prestador_token'])
            if estado_token['status']:
                datos_extra = obtener_datos_token(estado_token, datos['dinamismo'])
                lambda_datos = invocar_lambda(datos['nombre_zip'], AWS_LAMBDA_DATOS, datos_extra,
                                              EstadoLambda.DATOS.obtener_descripcion())
                if lambda_datos is not False:
                    lambda_datos['datos_extra'] = request.body.decode('utf-8')
                    return JsonResponse(lambda_datos)
                return JsonResponse(
                    {'statusCode': 502, 'mensaje': "Ha ocurrido un error al validar los datos del RIPS."})
            else:
                return HttpResponseForbidden()
    except Exception as ex:
        JsonResponse({'statusCode': 502, 'mensaje': "Error interno del server en la validación de datos."})


def guardar_datos_rips(request):
    try:
        if request.method == 'POST':
            datos = request.body.decode('utf-8')
            datos = json.loads(base64.b64decode(datos).decode('utf-8'))
            estado_token = validar_token.check(datos['token'], datos['cliente_token'],
                                               datos['prestador_token'])
            if estado_token['status']:
                datos_extra = obtener_datos_token(estado_token, datos['dinamismo'])
                lambda_guardar = invocar_lambda(datos['nombre_zip'], AWS_LAMBDA_GUARDADO, datos_extra,
                                                EstadoLambda.DATOS.obtener_descripcion())
                if lambda_guardar is not False:
                    if lambda_guardar['statusCode'] == 200:
                        lambda_guardar['datos']['estado'] = EstadoLambda.FINALIZADO.obtener_descripcion()
                    return JsonResponse(lambda_guardar)
                return JsonResponse({'statusCode': 502, 'mensaje': "Ha ocurrido un error al guardar el RIPS."})
            else:
                return HttpResponseForbidden()
    except Exception as ex:
        JsonResponse({'statusCode': 502, 'mensaje': "Error interno del server en el guardado de datos."})


def obtener_valores_dinamismo(cod_cliente):
    cliente = Eapb.objects.filter(dscodigo_entidad=cod_cliente).first()
    dinamismo = Dinamismo.objects.filter(Q(cdidcliente=cliente.cdid) & Q(snactive=1)).first()

    if dinamismo:
        return dinamismo.nmcod_metodo
    else:
        return None


def subir_archivo_s3(archivo):
    bucket_s3 = boto3.client('s3',
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    key = archivo.name
    try:
        bucket_s3.put_object(Bucket=AWS_BUCKET_NAME, Body=archivo, Key=key)
    except Exception as ex:
        return False


def invocar_lambda(nombre_zip, nombre_lambda, datos, estado_validacion):
    config = botocore.config.Config(connect_timeout=900, read_timeout=900, retries={'max_attempts': 0})

    aws_lambda = boto3.client('lambda',
                              region_name=AWS_DEFAULT_REGION,
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                              config=config)
    payload = {"pathParameters": {
        "bucket": AWS_BUCKET_NAME,
        "key": nombre_zip,
        "datos": datos,
    }}

    try:
        response = aws_lambda.invoke(
            FunctionName=nombre_lambda,
            InvocationType='RequestResponse',
            Payload=json.dumps(payload))
        if response:
            data = json.loads(response['Payload'].read())
            if "statusCode" in data and data["body"]:
                data['datos'] = {'nombre_zip': nombre_zip, 'codigo_cliente': datos['codigo_cliente'],
                                 'codigo_prestador': datos['codigo_prestador'],
                                 'estado': estado_validacion}
                return data
            return False
    except Exception as ex:
        return False


def obtener_datos_token(estado_token, dinamismo):
    cod_cliente = estado_token['data']['idCliente']
    cod_prestador = estado_token['data']['idPrestador']
    cod_habilitacion = estado_token['data']['codigoHabilitacion']
    nit_cliente = estado_token['data']['nitCliente']
    data = {"codigo_cliente": cod_cliente, "codigo_prestador": cod_prestador,
            "codigo_habilitacion": cod_habilitacion, "nit_cliente": nit_cliente, "dinamismo": dinamismo}
    return data

# -*- coding: utf-8 -*-
import os

import boto3
from Servicio.Controladores.ejecucion import Ejecucion
from Aplicacion.Pdf.pdf import GenerarPdf
from codecs import BOM_UTF8
import io
import zipfile
from Aplicacion.General.general import General

s3 = boto3.client('s3')

def lambda_handler(event, context):
    respuesta = {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {
            'Content-Type': 'content_type',
        },
        "body": ""
    }
    general = General()
    bucket = event['pathParameters']['bucket']
    __nombre_zip = event['pathParameters']['key']
    __codigo_cliente = event['pathParameters']['datos']['codigo_cliente']
    __id_prestador = event['pathParameters']['datos']['codigo_prestador']
    __codigo_habilitacion = event['pathParameters']['datos']['codigo_habilitacion']
    __nit_cliente = event['pathParameters']['datos']['nit_cliente']
    __zip_file = obtener_zip(bucket, __nombre_zip)
    if __zip_file is not None:
        with io.BytesIO(__zip_file.read()) as tf:
            tf.seek(0)
            print(str(__id_prestador))
            agregar_s3(tf, __nombre_zip, __nit_cliente,__id_prestador)
            with zipfile.ZipFile(tf, mode='r') as zipf:
                response = Ejecucion().ejecutar_lambda(zipf, __nombre_zip, __codigo_habilitacion, __codigo_cliente)
                lista_archivos_ct = []
                lista_archivos_ct = generar_lista_ct(zipf)
                GenerarPdf().obtener_instancia().asignar_asignar_ct(lista_archivos_ct)
                pdf = GenerarPdf().generar_pdf(lista_archivos_ct,__codigo_cliente)
                if response:
                    respuesta['statusCode'] = 200
                    respuesta['body'] = 'ok'
                    respuesta['mensaje'] = 'El RIPS #' + __nombre_zip[:-4] + ' fue validado y guardado exitosamente. Fecha: ' + response[:10] + ' Hora: ' + response[10:16]
                    respuesta["nombrePdf"] = 'CERTIFICADO REMISIÓN - ' + __nombre_zip[:-4]
                    respuesta['pdf'] = pdf
                else:
                    respuesta['statusCode'] = 500
                    respuesta['body'] = 'fail'
                    respuesta['mensaje'] = 'Ha ocurrido un error al guardar, el RIPS "' + __nombre_zip[:-4] + '" ya existe.'
                    # respuesta['mensaje'] = 'Ha ocurrido un error al guardar el RIPS "' + __nombre_zip[:-4] + '".'
    eliminar_archivos_temporales()
    return respuesta


def obtener_zip(bucket_nombre, zip_nombre):
    try:
        archivo = s3.get_object(Bucket=bucket_nombre, Key=zip_nombre)
    except Exception as e:
        return None
    return archivo['Body']


def agregar_s3(zip, nombre_zip, __nit_cliente,__id_prestador ):
    try:
        s3.put_object(Bucket=os.environ['bucket'], Body=zip, Key='RIPS-Validados/{}/original/{}/{}'.format(__nit_cliente,__id_prestador,nombre_zip)  )
        zip_modificado = codificar_zip_utf8(zip)
        s3.put_object(Bucket=os.environ['bucket'], Body=zip_modificado, Key='RIPS-Validados/{}/{}/{}'.format(__nit_cliente,__id_prestador,nombre_zip) )
    except FileNotFoundError:
        print("The file was not found")
        return False

def codificar_zip_utf8(zip):
    zipf = zipfile.ZipFile(zip,mode='r')
    nombres_archivos = zipf.namelist()
    with zipfile.ZipFile("/tmp/temporal.zip", "w") as zip_corregido:
        for nombre_archivo in nombres_archivos:
            with zipf.open(nombre_archivo) as archivo:
                contenido = archivo.read()
                if contenido.startswith(BOM_UTF8):
                    decodificado = contenido.decode("utf-8-sig")
                    zip_corregido.writestr(nombre_archivo,decodificado)
                else:
                    zip_corregido.writestr(nombre_archivo, contenido)
        zip_corregido.close()
    return io.BytesIO(open("/tmp/temporal.zip",'rb').read())
                    

def eliminar_archivos_temporales():
    array = os.listdir('/tmp')
    lista_archivos_ct=[]
    for item in array:
        os.remove('/tmp/' + item)


def generar_lista_ct(direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'CT':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

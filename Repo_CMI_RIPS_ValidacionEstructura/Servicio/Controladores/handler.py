# -*- coding: utf-8 -*-
from Servicio.Controladores.validar import Validador
import json
import boto3
import io
import os
import zipfile
import base64

s3 = boto3.client('s3')


def obtener_zip(bucket_nombre, zip_nombre):
    try:
        archivo = s3.get_object(Bucket=bucket_nombre, Key=zip_nombre)
    except Exception as e:
        return None
    return archivo['Body']


def eliminar_archivos_temporales():
    array = os.listdir('/tmp')
    for item in array:
        os.remove('/tmp/' + item)


def lambda_handler(event, context):
    respuesta = {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {
            'Content-Type': 'content_type',
        },
        "body": ""
    }
    bucket = event['pathParameters']['bucket']
    key = event['pathParameters']['key']
    codigo_cliente = event['pathParameters']['datos']['codigo_cliente']
    codigo_prestador = event['pathParameters']['datos']['codigo_prestador']
    codigo_habilitacion = event['pathParameters']['datos']['codigo_habilitacion']
    if event['pathParameters']['datos']['codigo_habilitacion']:
        if "," in codigo_habilitacion:
            codigos = codigo_habilitacion[1:]
            codigos_final = codigos[0:len(codigos)-1]
            codigo=codigos_final.replace("'","")
            codigo_habilitacion = codigo.split(',')
        elif "[" in codigo_habilitacion or "]" in codigo_habilitacion:
            codigos = codigo_habilitacion[1:]
            codigos_final = codigos[0:len(codigos)-1]
            codigo=codigos_final.replace("'","")
            codigo_habilitacion = [codigo]

    
    print("El código de habilitación es: " + str(codigo_habilitacion))
    print("El código de cliente es: " + str(codigo_cliente))
    print("El código de prestador es: " + str(codigo_prestador))
    
    if event['pathParameters']['datos']['dinamismo']:
        if "," in str(event['pathParameters']['datos']['dinamismo']):
            dinamismo = event['pathParameters']['datos']['dinamismo'].split(',')
            dinamismo = [int(cod) for cod in dinamismo]
        else:
            dinamismo = list()
            dinamismo.append(int(event['pathParameters']['datos']['dinamismo']))
    else:
        dinamismo = []
    zipp = obtener_zip(bucket, key)

    if zipp is not None:
        with io.BytesIO(zipp.read()) as tf:
            tf.seek(0)
            with zipfile.ZipFile(tf, mode='r') as zipf:
                validaciones_zip = Validador(zipf, key)
                zip_es_valido = validaciones_zip.validar_archivos(codigo_habilitacion,dinamismo)
                body = validaciones_zip.crear_zip()

        if not isinstance(body, str):
            with open(body.filename, "rb") as f:
                bytes = f.read()
                respuesta['body'] = base64.b64encode(bytes).decode("utf-8")
                if zip_es_valido:
                    respuesta['error'] = 'RIPS_' + key[:-4] + '_ERRORES_ESTRUCTURA.zip'
                else:
                    respuesta['error'] = 'RIPS_' + key[:-4] + '_ERRORES_ZIP.zip'
                f.close()
        else:
            respuesta['body'] = body
    
    eliminar_archivos_temporales()
    return respuesta



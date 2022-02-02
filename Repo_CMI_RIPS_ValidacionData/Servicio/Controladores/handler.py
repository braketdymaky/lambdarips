# -*- coding: utf-8 -*-
from Servicio.Controladores.validar import Validador
from Persistencia.Datos.datos import Datos
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


def crear_lista_por_archivo(direccion_archivo):
    """
    Método para generar listas por cada tipo de archivo
    :param direccion_archivo:
    :return:
    """
    listas_archivos_registros = {'AC': [], 'AF': [], 'AH': [], 'AM': [], 'AP': [], 'AT': [],
                                 'AU': [], 'CT': [], 'US': [], 'AD': [], 'AN': []}
    for archivo in direccion_archivo.namelist():
        archivo_texto = direccion_archivo.open(archivo, 'r').name
        archivo_base = direccion_archivo.open(archivo_texto, 'r')
        archivo_leido = archivo_base.read()
        registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
        for item in registros:
            if item != "":
                listas_archivos_registros[archivo[:2]].append(item.split(","))
        archivo_base.close()
    return listas_archivos_registros


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
    if event['pathParameters']['datos']['dinamismo']:
        dinamismo = event['pathParameters']['datos']['dinamismo'].split(',')
        dinamismo = [int(cod) for cod in dinamismo]
    else:
        dinamismo = []
    zipp = obtener_zip(bucket, key)

    if zipp is not None:
        with io.BytesIO(zipp.read()) as tf:
            tf.seek(0)
            with zipfile.ZipFile(tf, mode='r') as zipf:
                
                Datos().obtener_listas_parametrizadas()
                listas = crear_lista_por_archivo(zipf)
                validaciones_zip = Validador(zipf, key, codigo_cliente, listas, dinamismo,codigo_habilitacion,codigo_prestador)
                validaciones_zip.validar_archivos()
                body = validaciones_zip.crear_zip()
                
        if not isinstance(body, str):
            with open(body.filename, "rb") as f:
                bytes = f.read()
                respuesta['body'] = base64.b64encode(bytes).decode("utf-8")
                respuesta['error'] = 'RIPS_' + key[:-4] + '_ERRORES_DATOS.zip'
                f.close()
        else:
            respuesta['body'] = body
    
    eliminar_archivos_temporales()
    return respuesta

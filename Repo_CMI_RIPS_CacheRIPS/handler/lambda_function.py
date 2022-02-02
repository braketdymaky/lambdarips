import json
from servicio.datos import Tablas
import pymysql

def lambda_handler(event, context):
    # TODO implement
    Tablas().obtener_ficheros()
    return {
        'statusCode': 200,
        'body': json.dumps('Ficheros actualizados')
    }

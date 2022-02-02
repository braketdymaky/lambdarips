import pickle
import io
import zipfile

import boto3

s3 = boto3.client('s3')


class ListaBaseDatos:
    bucket = 'cmirips-dev-02'
    key = 'Ficheros/ficheros.zip'

    def obtener_lista_fichero(self, nombre_archivo):
        __zip_file = self.obtener_zip(self.bucket, self.key)
        if __zip_file is not None:
            with io.BytesIO(__zip_file.read()) as tf:
                tf.seek(0)
                with zipfile.ZipFile(tf, mode='r') as zipf:
                    respuesta = self.obtener_lista(zipf, nombre_archivo)
                    return respuesta

    def obtener_lista(self, zip, nombre_archivo):
        for archivo in zip.namelist():
            if archivo == nombre_archivo:
                fichero = zip.open(archivo, 'r')
                lista_tupla = pickle.load(fichero)
                respuesta = []
                for item in lista_tupla:
                    respuesta.append(list(item))
                return respuesta

    def obtener_zip(self, bucket_nombre, zip_nombre):
        try:
            archivo = s3.get_object(Bucket=bucket_nombre, Key=zip_nombre)
        except Exception as e:
            return None
        return archivo['Body']

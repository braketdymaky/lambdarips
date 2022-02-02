import boto3
from botocore.exceptions import ClientError

from servicio.conexion import Bucket


class AlmacenarFichero:
    bucket = Bucket()

    def almacenar_fichero_s3(self, fichero_zip):
        try:

            s3 = boto3.client('s3')
            key = fichero_zip.filename
            s3.upload_file(key, self.bucket.obtener_bucket_direccion(), self.bucket.obtener_bucket_carpeta())
        except ClientError as e:
            raise e
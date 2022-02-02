import pymysql
import sys
import os

class BaseDatos:
    __REGION = os.environ['aws_region']
    __rds_host = os.environ['host']
    __user = os.environ['user']
    __password = os.environ['password']
    __db_name = os.environ['db_name']

    conn = pymysql.connect(__rds_host, user=__user, passwd=__password, db=__db_name, connect_timeout=5)


class Bucket:
    __aws_bucket_direccion = 'cmirips-dev-02'
    __aws_bucket_carpeta = 'Ficheros/ficheros.zip'

    def obtener_bucket_direccion(self):
        """
        Retorna la direccion del bucket
        :return:
        """
        return self.__aws_bucket_direccion

    def obtener_bucket_carpeta(self):
        """
        Retorna la direccion de la carpeta que se actualizará
        :return:
        """
        return self.__aws_bucket_carpeta

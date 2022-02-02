import os
import zipfile
from pathlib import Path


class ModeloZip:
    __instance = None
    __direccion = ''
    __lista_archivos = []
    __extension = ''
    __nombre = ''
    __lista_registros_archivos = dict()

    @classmethod
    def obtener_instancia(cls):
        """
        obtener la instancia de la clase
        :return:
        """
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def asignar_valores(self, direccion_archivo, nombre_archivo):
        lista_archivos = direccion_archivo.namelist()
        lista_archivos = [archivo.upper() for archivo in lista_archivos]
        nombre = nombre_archivo
        self.__archivo = direccion_archivo
        self.__lista_archivos = lista_archivos
        self.__extension = nombre[len(nombre):len(nombre)-4]
        self.__nombre = nombre.replace(self.__extension, '')

    def obtener_direccion(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__direccion

    def obtener_lista_archivos(self):
        """
        Retorna la lista de archivos
        :return:
        """
        return self.__lista_archivos

    def obtener_extension(self):
        """
        Retorna la extension
        :return:
        """
        return self.__extension

    def obtener_nombre(self):
        """
        Retorna el nombre
        :return:
        """
        return self.__nombre

    def obtener_lista_registros_archivos(self):
        """
        Retorna el nombre
        :return:
        """
        return self.__lista_registros_archivos

    def asignar_lista_registros_archivos(self, lista_registros_archivos):
        """
        Asignar valor a la lista de lista de registros por archivos
        :param lista_registros_archivos:
        """
        self.__lista_registros_archivos = lista_registros_archivos

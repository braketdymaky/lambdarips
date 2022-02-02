# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as US_Columnas
from Aplicacion.Zip import zip


class ModeloUsuarios:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 14
    __campos_opcionales = [US_Columnas.US.obtener_segundo_apellido[zip.posicion_campo],
                           US_Columnas.US.obtener_segundo_nombre[zip.posicion_campo]]
    __campos_numericos = [US_Columnas.US.obtener_edad[zip.posicion_campo]]
    __lista_posiciones_con_longitudes = US_Columnas.US.obtener_lista

    @classmethod
    def obtener_instancia(cls):
        """
        obtener la instancia de la clase
        :return:
        """
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def asignar_valores(self, lista_registros):
        self.__lista_registros = lista_registros

    def obtener_lista(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__lista_registros

    def obtener_cantidad_columnas(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__cantidad_columnas

    def obtener_lista_longitudes(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__lista_posiciones_con_longitudes

    def obtener_campos_opcionales(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__campos_opcionales
        
    def obtener_campos_numericos(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__campos_numericos

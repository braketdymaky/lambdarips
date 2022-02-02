# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.recien_nacidos_enum import RecienNacidosColumnaEnum as AN_Columnas
from Aplicacion.Zip import zip


class ModeloRecienNacidos:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 14
    __campos_opcionales = [AN_Columnas.AN.obtener_diagnostico_de_nacido[zip.posicion_campo],
                           AN_Columnas.AN.obtener_causa_de_muerte[zip.posicion_campo],
                           AN_Columnas.AN.obtener_fecha_de_muerte[zip.posicion_campo],
                           AN_Columnas.AN.obtener_hora_de_muerte[zip.posicion_campo]]
    
    __campos_fecha = [AN_Columnas.AN.obtener_fecha_nacimiento[zip.posicion_campo],
                      AN_Columnas.AN.obtener_fecha_de_muerte[zip.posicion_campo]]
    
    __campos_numericos = [AN_Columnas.AN.obtener_peso_nacido[zip.posicion_campo]]

    __lista_posiciones_con_longitudes = AN_Columnas.AN.obtener_lista

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
        
    def obtener_campos_fecha(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__campos_fecha

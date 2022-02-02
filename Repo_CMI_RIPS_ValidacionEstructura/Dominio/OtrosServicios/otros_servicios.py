# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.otros_servicios_enum import OtrosServiciosColumnasEnum as AT_Columnas
from Aplicacion.Zip import zip


class ModeloOtrosServicios:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 11
    __campos_opcionales = [AT_Columnas.AT.obtener_codigo_servicio[zip.posicion_campo]]
    __campos_numericos = [AT_Columnas.AT.obtener_numero_unidades[zip.posicion_campo],
                          AT_Columnas.AT.obtener_valor_unitario[zip.posicion_campo],
                          AT_Columnas.AT.obtener_valor_total[zip.posicion_campo]]

    __lista_posiciones_con_longitudes = AT_Columnas.AT.obtener_lista

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

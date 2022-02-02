# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.descripcion_agrupada_enum import DescripcionAgrupadaColumnasEnum as Columnas
from Aplicacion.Zip import zip


class ModeloDescripcionAgrupada:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 6
    __campos_opcionales = []
    __campos_numericos = [Columnas.AD.obtener_codigo_concepto[zip.posicion_campo],
                          Columnas.AD.obtener_valor_unitario[zip.posicion_campo],
                          Columnas.AD.obtener_valor_total[zip.posicion_campo]]
    __lista_posiciones_con_longitudes = Columnas.AD.obtener_lista

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

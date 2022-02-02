# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.hospitalizaciones_enum import HospitalizacionesColumnasEnum as Columnas
from Aplicacion.Zip import zip


class ModeloHospitalizaciones:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 19
    __campos_opcionales = [Columnas.AH.obtener_diagnostico_relacionado_1[zip.posicion_campo],
                           Columnas.AH.obtener_diagnostico_relacionado_2[zip.posicion_campo],
                           Columnas.AH.obtener_diagnostico_relacionado_3[zip.posicion_campo],
                           Columnas.AH.obtener_complicacion[zip.posicion_campo],
                           Columnas.AH.obtener_causa_muerte[zip.posicion_campo],
                           Columnas.AH.obtener_numero_autorizacion[zip.posicion_campo]]
    __campos_fecha = [Columnas.AH.obtener_fecha_ingreso[zip.posicion_campo], 
                      Columnas.AH.obtener_fecha_egreso[zip.posicion_campo]]
    __campo_hora = []

    __lista_posiciones_con_longitudes = Columnas.AH.obtener_lista

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

    def obtener_campos_fecha(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__campos_fecha

    def obtener_campos_hora(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__campo_hora

    def obtener_campos_opcionales(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__campos_opcionales

# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.procedimientos_enum import ProcedimientosColumnasEnum as AP_Columnas
from Aplicacion.Zip import zip


class ModeloProcedimientos:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 15
    __campos_opcionales = [AP_Columnas.AP.obtener_numero_autorizacion[zip.posicion_campo],
                           AP_Columnas.AP.obtener_personal_que_atendio[zip.posicion_campo],
                           AP_Columnas.AP.obtener_diagnostico_principal[zip.posicion_campo],
                           AP_Columnas.AP.obtener_diagnostico_relacionado_1[zip.posicion_campo],
                           AP_Columnas.AP.obtener_complicacion[zip.posicion_campo],
                           AP_Columnas.AP.obtener_realizacion_act_quirurgico[zip.posicion_campo]]
                           
    __campos_numericos = [AP_Columnas.AP.obtener_valor[zip.posicion_campo]]
    
    __campos_fecha = [AP_Columnas.AP.obtener_fecha_procedimiento[zip.posicion_campo]]
    
    __lista_posiciones_con_longitudes = AP_Columnas.AP.obtener_lista

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
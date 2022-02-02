# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.urgencias_enum import UrgenciasColumnasEnum as AU_Columnas
from Aplicacion.Zip import zip


class ModeloUrgencias:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 17
    __campos_opcionales = [AU_Columnas.AU.obtener_diagnostico_relacionado_1[zip.posicion_campo],
                           AU_Columnas.AU.obtener_diagnostico_relacionado_2[zip.posicion_campo],
                           AU_Columnas.AU.obtener_diagnostico_relacionado_3[zip.posicion_campo],
                           AU_Columnas.AU.obtener_causa_muerte[zip.posicion_campo]]
                           
    __campos_fecha = [AU_Columnas.AU.obtener_fecha_ingreso[zip.posicion_campo],
                      AU_Columnas.AU.obtener_fecha_salida[zip.posicion_campo]]
    
    __lista_posiciones_con_longitudes = AU_Columnas.AU.obtener_lista

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
        
    def obtener_campos_fecha(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__campos_fecha
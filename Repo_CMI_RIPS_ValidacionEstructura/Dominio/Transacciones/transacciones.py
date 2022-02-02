# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as AF_Columnas
from Aplicacion.Zip import zip


class ModeloTransacciones:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 17
    __campos_opcionales = [AF_Columnas.AF.obtener_numero_contrato[zip.posicion_campo],
                           AF_Columnas.AF.obtener_plan_beneficios[zip.posicion_campo],
                           AF_Columnas.AF.obtener_numero_poliza[zip.posicion_campo],
                           AF_Columnas.AF.obtener_valor_total[zip.posicion_campo],
                           AF_Columnas.AF.obtener_valor_comision[zip.posicion_campo],
                           AF_Columnas.AF.obtener_valor_descuentos[zip.posicion_campo]]
    __campos_numericos = [AF_Columnas.AF.obtener_valor_comision[zip.posicion_campo],
                          AF_Columnas.AF.obtener_valor_descuentos[zip.posicion_campo],
                          AF_Columnas.AF.obtener_valor_neto[zip.posicion_campo],
                          AF_Columnas.AF.obtener_valor_total[zip.posicion_campo]]
                          
    __campos_fecha = [AF_Columnas.AF.obtener_fecha_expedicion[zip.posicion_campo],
                      AF_Columnas.AF.obtener_fecha_inicio[zip.posicion_campo],
                      AF_Columnas.AF.obtener_fecha_final[zip.posicion_campo]]
    
    __lista_posiciones_con_longitudes = AF_Columnas.AF.obtener_lista

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

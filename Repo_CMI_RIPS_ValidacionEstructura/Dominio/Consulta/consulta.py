from Utilidades.Enumerados.Archivo.consulta_enum import ArchivosConsultaColumnasEnum as Columnas
from Aplicacion.Zip import zip


class ModeloConsulta:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 17
    __campos_opcionales = [Columnas.AC.obtener_diagnostico_relacionado_1[zip.posicion_campo],
                           Columnas.AC.obtener_diagnostico_relacionado_2[zip.posicion_campo],
                           Columnas.AC.obtener_diagnostico_relacionado_3[zip.posicion_campo],
                           Columnas.AC.obtener_valor_cuota_moderadora[zip.posicion_campo]]

    __campos_fecha = [Columnas.AC.obtener_fecha_consulta[zip.posicion_campo]]

    __campos_numericos = [Columnas.AC.obtener_valor_consulta[zip.posicion_campo],
                          Columnas.AC.obtener_valor_cuota_moderadora[zip.posicion_campo],
                          Columnas.AC.obtener_valor_neto[zip.posicion_campo]]

    __lista_posiciones_con_longitudes = Columnas.AC.obtener_lista

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

from Utilidades.Enumerados.Archivo import control_enum as CT_columnas
from Aplicacion.Zip import zip


class ModeloControl:
    __instance = None
    __lista_registros = []
    __cantidad_columnas = 4
    __tipos_archivos_opcionales = ['AC', 'AH',
                                   'AM', 'AP',
                                   'AT', 'AU']
    __tipos_archivos_obligatorios = ['AF', 'US']
    __nombres_archivos = []
    __CT_archivos_presentes = []
    __lista_posiciones_con_longitudes = CT_columnas.ControlColumnasEnum.CT.obtener_lista
    __campos_opcionales = []

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
    
    def asignar_archvos_presentes(self, lista_registros):
        self.__CT_archivos_presentes = lista_registros
    
    def obtener_archivos_presentes(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__CT_archivos_presentes

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

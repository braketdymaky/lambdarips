from Dominio.Base.modelo_base import ModeloBase


class ModeloProcedimiento(ModeloBase):
    def asignar_lista_af(self, lista_registros):
        """
        asigna los valores para la lista de registros de af
        :return:
        """
        self.__lista_registros_af = lista_registros

    def obtener_lista_af(self):
        """
        Retorna la lista de archivos af
        :return:
        """
        return self.__lista_registros_af

    def asignar_lista_us(self, lista_registros):
        """
        asigna los valores para la lista de registros de us
        :return:
        """
        self.__lista_registros_us = lista_registros

    def obtener_lista_us(self):
        """
        Retorna la lista de archivos us
        :return:
        """
        return self.__lista_registros_us
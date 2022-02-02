from Dominio.Base.modelo_base import ModeloBase


class ModeloUrgencias(ModeloBase):

    def asignar_lista_af(self, lista_af):
        """
        asigna los valores para la lista de registros de af
        :return:
        """
        self.__lista_af = lista_af

    def obtener_lista_af(self):
        """
        Retorna la lista de archivos af
        :return:
        """
        return self.__lista_af

    def asignar_lista_us(self, lista_us):
        """
        asigna los valores para la lista de registros de us
        :return:
        """
        self.__lista_us = lista_us

    def obtener_lista_us(self):
        """
        Retorna la lista de archivos us
        :return:
        """
        return self.__lista_us

    def asignar_lista_ah(self, lista_ah):
        """
        asigna los valores para la lista de registros de ah
        :return:
        """
        self.__lista_ah = lista_ah

    def obtener_lista_ah(self):
        """
        Retorna la lista de archivos ah
        :return:
        """
        return self.__lista_ah

from Dominio.Base.modelo_base import ModeloBase


class ModeloOtrosServicios(ModeloBase):

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
    
    def asignar_lista_ac(self, lista_registros):
        """
        asigna los valores para la lista de registros de us
        :return:
        """
        self.__lista_registros_ac = lista_registros

    def obtener_lista_ap(self):
        """
        Retorna la lista de archivos us
        :return:
        """
        return self.__lista_registros_ap
    
    def asignar_lista_ap(self, lista_registros):
        """
        asigna los valores para la lista de registros de us
        :return:
        """
        self.__lista_registros_ap = lista_registros

    def obtener_lista_ac(self):
        """
        Retorna la lista de archivos us
        :return:
        """
        return self.__lista_registros_ac

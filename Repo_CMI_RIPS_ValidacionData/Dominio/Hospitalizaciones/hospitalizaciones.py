from Dominio.Base.modelo_base import ModeloBase


class ModeloHospitalizacion(ModeloBase):
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

    def asignar_lista_ap(self, lista_ap):
        """
        asigna los valores para la lista de registros de ap
        :return:
        """
        self.__lista_ap = lista_ap

    def obtener_lista_ap(self):
        """
        Retorna la lista de archivos ap
        :return:
        """
        return self.__lista_ap

    def asignar_lista_au(self, lista_au):
        """
        asigna los valores para la lista de registros de au
        :return:
        """
        self.__lista_au = lista_au

    def obtener_lista_au(self):
        """
        Retorna la lista de archivos au
        :return:
        """
        return self.__lista_au

    def asignar_lista_ac(self, lista_ac):
        """
        asigna los valores para la lista de registros de ac
        :return:
        """
        self.__lista_ac = lista_ac

    def obtener_lista_ac(self):
        """
        Retorna la lista de archivos ac
        :return:
        """
        return self.__lista_ac
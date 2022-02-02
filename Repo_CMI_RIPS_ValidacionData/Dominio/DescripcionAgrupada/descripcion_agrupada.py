from Dominio.Base.modelo_base import ModeloBase


class ModeloDescripcionAgrupada(ModeloBase):
    
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
    
    
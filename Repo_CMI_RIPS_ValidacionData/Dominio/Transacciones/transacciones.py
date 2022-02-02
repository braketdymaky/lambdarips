from Dominio.Base.modelo_base import ModeloBase


class ModeloTransacciones(ModeloBase):

    def asignar_listas(self, lista_registros):
        """
        asigna los valores para el diccionario de listas
        :return:
        """
        self.__listas_registros = dict(lista_registros)

    def obtener_listas(self,lista):
        """
        Retorna la lista de archivos af
        :return:
        """
        return self.__listas_registros[lista]

    def asignar_id_cliente(self,id_cliente):
        
        self.__id_cliente = id_cliente
    
    def obtener_id_cliente(self):
        
        return self.__id_cliente
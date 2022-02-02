from Dominio.Base.modelo_base import ModeloBase


class ModeloUsuarios(ModeloBase):
    
    def asignar_listas(self, lista_archivos):
        self.listas_archivos_registros = dict(lista_archivos)
    
    def asignar_id_cliente(self,id_cliente):
        
        self.__id_cliente = id_cliente
    
    def obtener_id_cliente(self):
        
        return self.__id_cliente

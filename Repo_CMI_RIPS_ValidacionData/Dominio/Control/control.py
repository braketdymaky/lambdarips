from Dominio.Base.modelo_base import ModeloBase


class ModeloControl(ModeloBase):
    listas_archivos_registros = dict()
    def asignar_listas(self, lista_archivos):
        self.listas_archivos_registros = dict(lista_archivos)
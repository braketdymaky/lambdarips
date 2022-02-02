from enum import Enum


class EstadoLambda(Enum):
    ESTRUCTURA = 'Validación de estructura'
    DATOS = 'Validación de datos'
    GUARDADO = 'Guardado de datos'
    FINALIZADO = 'Finalizado'

    def obtener_descripcion(self):
        return self.value

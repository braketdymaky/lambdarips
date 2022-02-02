from enum import Enum
from collections import namedtuple

ControlColumnas = namedtuple('Control', ['codigo_prestador_posicion', 'fecha_remision_posicion',
                                         'archivo_codigo_posicion', 'archivo_total_registros_posicion', ])


class ControlColumnasEnum(Enum):
    CT = ControlColumnas(0, 1, 2, 3)

    @property
    def obtener_lista(self):
        lista = [0, 1, 2, 3]
        return lista

    @property
    def obtener_codigo_prestador_posicion(self):
        """
        Metodo para obtenerla posicion de la columna codigo prestador del archivo de control
        :return:
        """
        return self.value.codigo_prestador_posicion

    @property
    def obtener_fecha_remision_posicion(self):
        """
        Metodo para obtenerla posicion de la columna fecha de remision del archivo de control
        :return:
        """
        return self.value.fecha_remision_posicion

    @property
    def obtener_archivo_codigo_posicion(self):
        """
        Metodo para obtener la posicion de la columna codigo de los archivos registrados en el archivo de control
        :return:
        """
        return self.value.archivo_codigo_posicion

    @property
    def obtener_archivo_total_registros_posicion(self):
        """
        Metodo para obtener la posicion de la columna cantidad de registros del archivo de control
        :return:
        """
        return self.value.archivo_total_registros_posicion

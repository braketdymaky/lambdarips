# enum necesarios para las constantes pertenecientes al archivo de control CT
# 21/05/2019 ANDERSON ARIZA

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado

ControlColumnas = namedtuple('ControlArchivo',
                             ['codigo_prestador_posicion', 'codigo_prestador_longitud',
                              'fecha_remision_posicion', 'fecha_remision_longitud',
                              'archivo_codigo_posicion', 'archivo_codigo_logitud',
                              'archivo_total_registros_posicion', 'archivo_total_registros_longitud'])


class ControlColumnasEnum(Enum):
    CT = ControlColumnas(0, 12, 1, 10, 2, 8, 3, 10)


    @property
    def obtener_lista(self):
        lista = [[0, 12], [1, 10], [2, 8], [3, 10]]
        return lista

    # Método para obtenerla posicion de la columna codigo prestador del archivo de control
    @property
    def obtener_codigo_prestador_posicion(self):
        return self.value.codigo_prestador_posicion

    # Método para obtenerla longitud de la columna codigo prestador del archivo de control
    @property
    def obtener_codigo_prestador_longitud(self):
        return self.value.codigo_prestador_longitud

    # Método para obtenerla posicion de la columna fecha de remision del archivo de control
    @property
    def obtener_fecha_remision_posicion(self):
        return self.value.fecha_remision_posicion

    # Método para obtenerla longitud de la columna fecha de remision del archivo de control
    @property
    def obtener_fecha_remision_longitud(self):
        return self.value.fecha_remision_longitud

    # Método para obtener la posicion de la columna codigo de archivo del archivo de control
    @property
    def obtener_archivo_codigo_posicion(self):
        return self.value.archivo_codigo_posicion

    # Método para obtener la posicion de la longitud codigo de archivo del archivo de control
    @property
    def obtener_archivo_codigo_logitud(self):
        return self.value.archivo_codigo_logitud

    # Método para obtener la posicion de la columna cantidad de registros del archivo de control
    @property
    def obtener_archivo_total_registros_posicion(self):
        return self.value.archivo_total_registros_posicion

    # Método para obtener la longitud de la columna cantidad de registros del archivo de control
    @property
    def obtener_archivo_total_registros_longitud(self):
        return self.value.archivo_total_registros_longitud

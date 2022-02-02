# enum necesarios para las constantes pertenecientes al archivo de DESCRIPCION AGRUPADA

# 21/05/2019 ANDERSON ARIZA
# Los metodos retorna una lista con dos valores, siendo la primera posición
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado

DescripcionAgrupadaColumnas = namedtuple('DescripcionAgrupadaArchivo',
                                         ['n_factura_posicion', 'n_factura_longitud',
                                          'codigo_prestador_posicion', 'codigo_prestador_longitud',
                                          'codigo_concepto_posicion', 'codigo_concepto_longitud',
                                          'cantidad_servicios_posicion', 'cantidad_servicios_longitud',
                                          'valor_unitario_posicion', 'valor_unitario_longitud',
                                          'valor_total_posicion', 'valor_total_logitud'])


class DescripcionAgrupadaColumnasEnum(Enum):
    AD = DescripcionAgrupadaColumnas(0, 20, 1, 12, 2, 2, 3, 15, 4, 15, 5, 15)

    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_archivo= [[0, 20], [1, 12], [2, 2], [3, 15], [4, 15], [5, 15]]
        return lista_archivo
    # Método para obtenerla posicion y longitud de la columna codigo del prestador dewl archivo de descripcion agrupada
    @property
    def obtener_codigo_prestador(self):
        response = (self.value.codigo_prestador_posicion, self.value.codigo_prestador_longitud)
        return response

    # Método para obtenerla posicion y longitud de la columna codigo del prestador dewl archivo de descripcion agrupada
    @property
    def obtener_codigo_concepto(self):
        response = (self.value.codigo_concepto_posicion, self.value.codigo_concepto_longitud)
        return response

    # Método para obtenerla posicion y longitud de la columna numero de factura dewl archivo de descripcion agrupada
    @property
    def obtener_numero_factura(self):
        response = (self.value.n_factura_posicion, self.value.n_factura_longitud)
        return response

    # Método para obtenerla posicion y longitud de la columna cantidad de servicios del archivo de descripcion agrupada
    @property
    def obtener_cantidad_de_servicios(self):
        response = (self.value.cantidad_servicios_posicion, self.value.cantidad_servicios_longitud)
        return response

    # Método para obtenerla posicion y longitud de la columna valor unitario del servicio del archivo de descripcion agrupada
    @property
    def obtener_valor_unitario(self):
        response = (self.value.valor_unitario_posicion, self.value.valor_unitario_longitud)
        return response

    # Método para obtenerla posicion y longitud de la columna valor total del servicio del archivo de descripcion agrupada
    @property
    def obtener_valor_total(self):
        response = (self.value.valor_total_posicion, self.value.valor_total_logitud)
        return response

from enum import Enum
from collections import namedtuple

DescripcionAgrupadaColumnas = namedtuple('DescripcionAgrupada',
                                         ['n_factura_posicion', 'codigo_prestador_posicion',
                                          'codigo_concepto_posicion', 'cantidad_servicios_posicion',
                                          'valor_unitario_posicion', 'valor_total_posicion'])


class DescripcionAgrupadaColumnasEnum(Enum):
    AD = DescripcionAgrupadaColumnas(0, 1, 2, 3, 4, 5)

    @property
    def obtener_lista(self):
        """
        Metodo para obtener la lista con las posiciones y longitudes
        :return:
        """
        lista_archivo = [0, 1, 2, 3, 4, 5]
        return lista_archivo

    @property
    def obtener_codigo_prestador(self):
        """
        Metodo para obtenerla posicion y longitud de la columna codigo del prestador dewl archivo
        de descripcion agrupada
        :return:
        """
        response = self.value.codigo_prestador_posicion
        return response

    @property
    def obtener_codigo_concepto(self):
        """
        Metodo para obtenerla posicion y longitud de la columna codigo del prestador dewl archivo
        de descripcion agrupada
        :return:
        """
        response = self.value.codigo_concepto_posicion
        return response

    @property
    def obtener_numero_factura(self):
        """
        Metodo para obtenerla posicion y longitud de la columna numero de factura dewl archivo de descripcion agrupada
        :return:
        """
        response = self.value.n_factura_posicion
        return response

    @property
    def obtener_cantidad_de_servicios(self):
        """
        Metodo para obtenerla posicion y longitud de la columna cantidad de servicios del archivo
        de descripcion agrupada
        :return:
        """
        response = self.value.cantidad_servicios_posicion
        return response

    @property
    def obtener_valor_unitario(self):
        """
        Metodo para obtenerla posicion y longitud de la columna valor unitario del servicio del archivo
        de descripcion agrupada
        :return:
        """
        response = self.value.valor_unitario_posicion
        return response

    @property
    def obtener_valor_total(self):
        """
        Metodo para obtenerla posicion y longitud de la columna valor total del servicio del archivo
        de descripcion agrupada
        :return:
        """
        response = self.value.valor_total_posicion
        return response

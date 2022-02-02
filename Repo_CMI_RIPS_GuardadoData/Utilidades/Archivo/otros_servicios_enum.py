from enum import Enum
from collections import namedtuple

OtrosServiciosColumnas = namedtuple('OtrosServicios',
                                    ['n_factura_posicion', 'codigo_prestador_posicion', 'tipo_id_posicion',
                                     'id_posicion', 'n_autorizacion_posicion', 'tipo_p', 'codigo_p', 'nombre_p',
                                     'numero_unidades_p', 'valor_unitario_p', 'valor_total_p'])


class OtrosServiciosColumnasEnum(Enum):
    AT = OtrosServiciosColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    @property
    def obtener_lista(self):
        """
        Metodo para obtener la lista con las posiciones y longitudes
        :return:
        """
        lista_archivo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return lista_archivo

    @property
    def obtener_codigo_prestador(self):
        """
        Metodo para obtenerla posicion y longitud de la columna codigo prestador del archivo de procedimiento
        :return:
        """
        response = self.value.codigo_prestador_posicion
        return response

    @property
    def obtener_tipo_id(self):
        """
        Metodo para obtener el tipo de id del procedimiento
        :return:
        """
        response = self.value.tipo_id_posicion
        return response

    @property
    def obtener_numero_id(self):
        """
        Metodo para obtener el numero de id del procedimiento
        :return:
        """
        response = self.value.id_posicion
        return response

    @property
    def obtener_numero_factura(self):
        """
        Metodo para obtener de numero de factura del procedimiento
        :return:
        """
        response = self.value.n_factura_posicion
        return response

    @property
    def obtener_numero_autorizacion(self):
        """
        Metodo para obtener la posicion y longitud  numero de autorizacion
        :return:
        """
        response = self.value.n_autorizacion_posicion
        return response

    @property
    def obtener_codigo_servicio(self):
        """
        Metodo para obtener la posicion y longitud  de la columna codigo del medicamento para el archivo de medicamentos
        :return:
        """
        response = self.value.codigo_p
        return response

    @property
    def obtener_tipo_servicio(self):
        """
        Metodo para obtener la posicion y longitud  de la columna tipo del medicamento para el archivo de medicamentos
        :return:
        """
        response = self.value.tipo_p
        return response

    @property
    def obtener_nombre_servicio(self):
        """
        Metodo para obtener la posicion y longitud  de la columna nombre generico del medicamento para el archivo
         de medicamentos
        :return:
        """
        response = self.value.nombre_p
        return response

    @property
    def obtener_numero_unidades(self):
        """
        Metodo para obtener la posicion y longitud  de la columna  unidades unidad del medicamento para el archivo
         de medicamentos
        :return:
        """
        response = self.value.numero_unidades_p
        return response

    @property
    def obtener_valor_unitario(self):
        """
        Metodo para obtener la posicion y longitud  de la columna  valor unitario del medicamento para el archivo
         de medicamentos
        :return:
        """
        response = self.value.valor_unitario_p
        return response

    @property
    def obtener_valor_total(self):
        """
        Metodo para obtener la posicion y longitud  de la columna  valor total del medicamento para el archivo
         de medicamentos
        :return:
        """
        response = self.value.valor_total_p
        return response

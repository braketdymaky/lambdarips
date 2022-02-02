# enum necesarios para las constantes pertenecientes al archivo de medicamentos
# 22/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion 
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
OtrosServiciosColumnas = namedtuple('ProcedimientosArchivo',
                                    ['n_factura_posicion', 'n_factura_longitud',
                                     'codigo_prestador_posicion', 'codigo_prestador_longitud',
                                     'tipo_id_posicion', 'tipo_id_logitud',
                                     'id_posicion', 'id_longitud',
                                     'n_autorizacion_posicion', 'n_autorizacion_longitud',
                                     'tipo_p', 'tipo_l',
                                     'codigo_p', 'codigo_l',
                                     'nombre_p', 'nombre_l',
                                     'numero_unidades_p', 'numero_unidades_l',
                                     'valor_unitario_p', 'valor_unitario_l',
                                     'valor_total_p', 'valor_total_l'])


class OtrosServiciosColumnasEnum(Enum):
    AT = OtrosServiciosColumnas(0, 20, 1, 12, 2, 2, 3, 16, 4, 20, 5, 1, 6, 20, 7, 60, 8, 5, 9, 15, 10, 15)

    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_archivo = [[0, 20], [1, 12], [2, 2], [3, 16], [4, 20], [5, 1], [6, 20], [7, 60], [8, 5], [9, 15], [10, 15]]
        return lista_archivo


    # Metodo para obtenerla posicion y longitud de la columna codigo prestador del archivo de procedimiento
    @property
    def obtener_codigo_prestador(self):
        response = (self.value.codigo_prestador_posicion, self.value.codigo_prestador_longitud)
        return response

    # metodo para obtener el tipo de id del procedimiento
    @property
    def obtener_tipo_id(self):
        response = (self.value.tipo_id_posicion, self.value.tipo_id_logitud)
        return response

    # metodo para obtener el numero de id del procedimiento
    @property
    def obtener_numero_id(self):
        response = (self.value.id_posicion, self.value.id_longitud)
        return response

    # metodo para obtener de numero de factura del procedimiento
    @property
    def obtener_numero_factura(self):
        response = (self.value.n_factura_posicion, self.value.n_factura_longitud)
        return response

    # metodo para obtener la posicion y longitud  numero de autorizacion
    @property
    def obtener_numero_autorizacion(self):
        response = (self.value.n_autorizacion_posicion, self.value.n_autorizacion_longitud)
        return response

    # metodo para obtener la posicion y longitud  de la columna codigo del medicamento para el archivo de medicamentos
    @property
    def obtener_codigo_servicio(self):
        response = (self.value.codigo_p, self.value.codigo_l)
        return response

    # metodo para obtener la posicion y longitud  de la columna tipo del medicamento para el archivo de medicamentos
    @property
    def obtener_tipo_servicio(self):
        response = (self.value.tipo_p, self.value.tipo_l)
        return response

    # metodo para obtener la posicion y longitud  de la columna nombre generico del medicamento para el archivo de medicamentos
    @property
    def obtener_nombre_servicio(self):
        response = (self.value.nombre_p, self.value.nombre_l)
        return response

    # metodo para obtener la posicion y longitud  de la columna  unidades unidad del medicamento para el archivo de medicamentos
    @property
    def obtener_numero_unidades(self):
        response = (self.value.numero_unidades_p, self.value.numero_unidades_l)
        return response

    # metodo para obtener la posicion y longitud  de la columna  valor unitario del medicamento para el archivo de medicamentos
    @property
    def obtener_valor_unitario(self):
        response = (self.value.valor_unitario_p, self.value.valor_unitario_l)
        return response

    # metodo para obtener la posicion y longitud  de la columna  valor total del medicamento para el archivo de medicamentos
    @property
    def obtener_valor_total(self):
        response = (self.value.valor_total_p, self.value.valor_total_l)
        return response

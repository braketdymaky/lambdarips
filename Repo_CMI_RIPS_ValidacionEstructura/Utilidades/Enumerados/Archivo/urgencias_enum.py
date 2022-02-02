# enum necesarios para las constantes pertenecientes al archivo de urgencias
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion 
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
UrgenciasColumnas = namedtuple('UrgenciasArchivo',
                               ['n_factura_posicion', 'n_factura_longitud',
                                'codigo_prestador_posicion', 'codigo_prestador_longitud',
                                'tipo_id_posicion', 'tipo_id_logitud',
                                'id_posicion', 'id_longitud',
                                'fecha_ingreso_posicion', 'fecha_ingreso_longitud',
                                'hora_ingreso_posicion', 'hora_ingreso_longitud',
                                'n_autorizacion_posicion', 'n_autorizacion_longitud',
                                'causa_externa_posicion', 'causa_externa_longitud',
                                'co_diagnostico_princ_posicion', 'co_diagnostico_pirnc_longitud',
                                'co_diagnostico1_posicion', 'co_diagnostico1_longitud',
                                'co_diagnostico2_posicion', 'co_diagnostico2_longitud',
                                'co_diagnostico3_posicion', 'co_diagnostico3_longitud',
                                'destino_usuario_posicion', 'destino_usuario_longitud',
                                'estado_salida_posicion', 'estado_salida_longitud',
                                'causa_muerte_posicion', 'causa_muerte_longitud',
                                'fecha_salida_poscion', 'fecha_salida_longitud',
                                'hora_salida_posicion', 'hora_salida_longitud'])


class UrgenciasColumnasEnum(Enum):
    AU = UrgenciasColumnas(0, 20, 1, 10, 2, 2, 3, 16, 4, 10, 5, 5, 6, 20, 7, 2, 8, 4, 9, 4, 10, 4, 11, 4, 12, 1, 13, 1,
                           14, 4, 15, 10, 16, 5)

    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_transacciones = [[0, 20], [1, 12], [2, 2], [3, 16], [4, 10], [5, 5], [6, 20], [7, 2], [8, 4], [9, 4],
                               [10, 4], [11, 4], [12, 1], [13, 1], [14, 4], [15, 10], [16, 5]]
        return lista_transacciones

    # Metodo para obtenerla posicion y longitud de la columna codigo prestador del archivo de Transacciones
    @property
    def obtener_codigo_prestador(self):
        response = (self.value.codigo_prestador_posicion, self.value.codigo_prestador_longitud)
        return response

    # metodo para obtener el tipo de id
    @property
    def obtener_tipo_id(self):
        response = (self.value.tipo_id_posicion, self.value.tipo_id_logitud)
        return response

    # metodo para obtener el numero de id
    @property
    def obtener_numero_id(self):
        response = (self.value.id_posicion, self.value.id_longitud)
        return response

    # metodo para obtener de numero de factura
    @property
    def obtener_numero_factura(self):
        response = (self.value.n_factura_posicion, self.value.n_factura_longitud)
        return response

    # metodo para obtener la posicion y longitud  feha de consulta
    @property
    def obtener_fecha_ingreso(self):
        response = (self.value.fecha_ingreso_posicion, self.value.fecha_ingreso_longitud)
        return response

    # metodo para obtener la posicion y longitud  feha de consulta
    @property
    def obtener_numero_autorizacion(self):
        response = (self.value.n_autorizacion_posicion, self.value.n_autorizacion_longitud)
        return response

    # metodo para obtener la posicion y longitud  causa externa de la consulta
    @property
    def obtener_causa_externa(self):
        response = (self.value.causa_externa_posicion, self.value.causa_externa_longitud)
        return response

    # metodo para obtener la posicion y longitud  causa externa de la consulta
    @property
    def obtener_causa_muerte(self):
        response = (self.value.causa_muerte_posicion, self.value.causa_muerte_longitud)
        return response

    # metodo para obtener la posicion y longitud  diagnostico principal de la consulta
    @property
    def obtener_diagnostico_principal(self):
        response = (self.value.co_diagnostico_princ_posicion, self.value.co_diagnostico_pirnc_longitud)
        return response

    # metodo para obtener la posicion y longitud  diagnostico relacionado 1 de la consulta
    @property
    def obtener_diagnostico_relacionado_1(self):
        response = (self.value.co_diagnostico1_posicion, self.value.co_diagnostico1_longitud)
        return response

    # metodo para obtener la posicion y longitud  diagnostico relacionado 2 de la consulta
    @property
    def obtener_diagnostico_relacionado_2(self):
        response = (self.value.co_diagnostico2_posicion, self.value.co_diagnostico2_longitud)
        return response

    # metodo para obtener la posicion y longitud  diagnostico relacionado 3 de la consulta
    @property
    def obtener_diagnostico_relacionado_3(self):
        response = (self.value.co_diagnostico3_posicion, self.value.co_diagnostico3_longitud)
        return response

    # metodo para obtener la posicion y longitud  hora de ingreso a urgencias
    @property
    def obtener_hora_ingreso(self):
        response = (self.value.hora_ingreso_posicion, self.value.hora_ingreso_longitud)
        return response

    # metodo para obtener la posicion y longitud  el destino del usuario al salir de urgencias
    @property
    def obtener_destino_usuario(self):
        response = (self.value.destino_usuario_posicion, self.value.destino_usuario_longitud)
        return response

    # metodo para obtener la posicion y longitud  estado de salida de urgencias
    @property
    def obtener_destino_usuario(self):
        response = (self.value.estado_salida_posicion, self.value.estado_salida_longitud)
        return response

    # metodo para obtener la posicion y longitud  de la fecha de salida de urgencias
    @property
    def obtener_fecha_salida(self):
        response = (self.value.fecha_salida_poscion, self.value.fecha_salida_longitud)
        return response

    # metodo para obtener la posicion y longitud  de la hora de salida de urgencias
    @property
    def obtener_hora_salida(self):
        response = (self.value.hora_salida_posicion, self.value.hora_salida_longitud)
        return response

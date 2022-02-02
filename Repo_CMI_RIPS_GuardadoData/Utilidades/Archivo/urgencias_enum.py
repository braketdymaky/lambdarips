# enum necesarios para las constantes pertenecientes al archivo de urgencias
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion 
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
UrgenciasColumnas = namedtuple('UrgenciasArchivo',
                               ['n_factura_posicion', 'codigo_prestador_posicion', 'tipo_id_posicion', 'id_posicion',
                                'fecha_ingreso_posicion', 'hora_ingreso_posicion', 'n_autorizacion_posicion',
                                'causa_externa_posicion', 'co_diagnostico_princ_posicion', 'co_diagnostico1_posicion',
                                'co_diagnostico2_posicion', 'co_diagnostico3_posicion', 'destino_usuario_posicion',
                                'estado_salida_posicion', 'causa_muerte_posicion', 'fecha_salida_poscion',
                                'hora_salida_posicion'])


class UrgenciasColumnasEnum(Enum):
    AU = UrgenciasColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                           13, 14, 15, 16)

    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_transacciones = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9],
                               [10], [11], [12], [13], [14], [15], [16]]
        return lista_transacciones

    # Metodo para obtenerla posicion y longitud de la columna codigo prestador del archivo de Transacciones
    @property
    def obtener_codigo_prestador(self):
        response = self.value.codigo_prestador_posicion
        return response

    # metodo para obtener el tipo de id
    @property
    def obtener_tipo_id(self):
        response = self.value.tipo_id_posicion
        return response

    # metodo para obtener el numero de id
    @property
    def obtener_numero_id(self):
        response = self.value.id_posicion
        return response

    # metodo para obtener de numero de factura
    @property
    def obtener_numero_factura(self):
        response = self.value.n_factura_posicion
        return response

    # metodo para obtener la posicion y longitud  feha de consulta
    @property
    def obtener_fecha_ingreso(self):
        response = self.value.fecha_ingreso_posicion
        return response

    # metodo para obtener la posicion y longitud  feha de consulta
    @property
    def obtener_numero_autorizacion(self):
        response = self.value.n_autorizacion_posicion
        return response

    # metodo para obtener la posicion y longitud  causa externa de la consulta
    @property
    def obtener_causa_externa(self):
        response = self.value.causa_externa_posicion
        return response

    # metodo para obtener la posicion y longitud  causa externa de la consulta
    @property
    def obtener_causa_muerte(self):
        response = self.value.causa_muerte_posicion
        return response

    # metodo para obtener la posicion y longitud  diagnostico principal de la consulta
    @property
    def obtener_diagnostico_principal(self):
        response = self.value.co_diagnostico_princ_posicion
        return response

    # metodo para obtener la posicion y longitud  diagnostico relacionado 1 de la consulta
    @property
    def obtener_diagnostico_relacionado_1(self):
        response = self.value.co_diagnostico1_posicion
        return response

    # metodo para obtener la posicion y longitud  diagnostico relacionado 2 de la consulta
    @property
    def obtener_diagnostico_relacionado_2(self):
        response = self.value.co_diagnostico2_posicion
        return response

    # metodo para obtener la posicion y longitud  diagnostico relacionado 3 de la consulta
    @property
    def obtener_diagnostico_relacionado_3(self):
        response = self.value.co_diagnostico3_posicion
        return response

    # metodo para obtener la posicion y longitud  hora de ingreso a urgencias
    @property
    def obtener_hora_ingreso(self):
        response = self.value.hora_ingreso_posicion
        return response

    # metodo para obtener la posicion y longitud  el destino del usuario al salir de urgencias
    @property
    def obtener_destino_usuario(self):
        response = self.value.destino_usuario_posicion
        return response

    # metodo para obtener la posicion y longitud  estado de salida de urgencias
    @property
    def obtener_hdestino_usuario(self):
        response = self.value.estado_salida_posicion
        return response

    # metodo para obtener la posicion y longitud  de la fecha de salida de urgencias
    @property
    def obtener_fecha_salida(self):
        response = self.value.fecha_salida_poscion
        return response

    # metodo para obtener la posicion y longitud  de la hora de salida de urgencias
    @property
    def obtener_hora_salida(self):
        response = self.value.hora_salida_posicion
        return response

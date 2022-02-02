# enum necesarios para las constantes pertenecientes al archivo de hospitlizaciones
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion 
# $ la ubicacion de la columna y la segunda su longitud esperada
# la letra p al final denota posicion y la l longitud

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
HospitalizacionesColumnas = namedtuple('UrgenciasArchivo',
                                       ['n_factura_posicion', 'n_factura_longitud',
                                        'codigo_prestador_posicion', 'codigo_prestador_longitud',
                                        'tipo_id_posicion', 'tipo_id_logitud',
                                        'id_posicion', 'id_longitud',
                                        'via_ingreso_p', 'via_ingreso_l',
                                        'fch_ingreso_p', 'fch_ingreso_l',
                                        'hora_ingreso_p', 'hora_ingreso_l',
                                        'n_autorizacion_p', 'n_autorizacion_l',
                                        'causa_ext_p', 'causa_ext_l',
                                        'diagnostico_princ_ingreso_p', 'diagnostico_princ_ingreso_l',
                                        'diagnostico_princ_egreso_p', 'diagnostico_princ_egreso_l',
                                        'diagnostico_rela1_p', 'diagnostico_rela1_l',
                                        'diagnostico_rela2_p', 'diagnostico_rela2_l',
                                        'diagnostico_rela3_p', 'diagnostico_rela3_l',
                                        'complicacion_p', 'complicacion_l',
                                        'estado_salida_p', 'estado_salida_l',
                                        'causa_muerte_p', 'causa_muerte_l',
                                        'fch_egreso_p', 'fch_egreso_l',
                                        'hora_egreso_p', 'hora_egreso_l'])


class HospitalizacionesColumnasEnum(Enum):
    AH = HospitalizacionesColumnas(0, 20, 1, 12, 2, 2, 3, 16, 4, 1, 5, 10, 6, 5, 7, 20, 8, 2, 9, 4, 10, 4, 11, 4, 12, 4,
                                   13, 4, 14, 4, 15, 1, 16, 4, 17, 10, 18, 5)
    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_archivo = [[0, 20], [1, 12], [2, 2], [3, 20], [4, 1], [5, 10], [6, 5], [7, 15], [8, 2], [9, 4], [10, 4], [11, 4], [12, 4],[13, 4], [14, 4], [15, 1], [16, 4], [17, 10], [18, 5]]
        return lista_archivo

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

    # metodo para obtener el numero de id hospitalizacion
    @property
    def obtener_numero_id(self):
        response = (self.value.id_posicion, self.value.id_longitud)
        return response

    # metodo para obtener la posicion y la longitud de numero de factura para hospitalizacion
    @property
    def obtener_numero_factura(self):
        response = (self.value.n_factura_posicion, self.value.n_factura_longitud)
        return response

    # metodo para obtener la posicion y la longitud de la via de ingreso para hospitalizacion
    @property
    def obtener_via_ingreso(self):
        response = (self.value.via_ingreso_p, self.value.via_ingreso_l)
        return response

    # metodo para obtener la posicion y la longitud de la fecha de ingreso para hospitalizacion
    @property
    def obtener_fecha_ingreso(self):
        response = (self.value.fch_ingreso_p, self.value.fch_ingreso_l)
        return response

    # metodo para obtener la posicion y la longitud de la hora de ingreso para hospitalizacion
    @property
    def obtener_hora_ingreso(self):
        response = (self.value.hora_ingreso_p, self.value.hora_ingreso_l)
        return response

    # metodo para obtener la posicion y la longitud del numero de autorizacion para hospitalizacion
    @property
    def obtener_numero_autorizacion(self):
        response = (self.value.n_autorizacion_p, self.value.n_autorizacion_l)
        return response

    # metodo para obtener la posicion y la longitud de la causa externa para hospitalizacion
    @property
    def obtener_causa_externa(self):
        response = (self.value.causa_ext_p, self.value.causa_ext_l)
        return response

    # metodo para obtener la posicion y la longitud de la columna estado a la salida  para hospitalizacion
    @property
    def obtener_estado_salida(self):
        response = (self.value.estado_salida_p, self.value.estado_salida_l)
        return response

    # metodo para obtener la posicion y la longitud del diagnostico principal para ingreso para hospitalizacion
    @property
    def obtener_diagnostico_principal_ingreso(self):
        response = (self.value.diagnostico_princ_ingreso_p, self.value.diagnostico_princ_ingreso_l)
        return response

    # metodo para obtener la posicion y la longitud del diagnostico principal de egreso para hospitalizacion
    @property
    def obtener_diagnostico_principal_egreso(self):
        response = (self.value.diagnostico_princ_egreso_p, self.value.diagnostico_princ_egreso_l)
        return response

    # metodo para obtener la posicion y la longitud del diagnostico relacionado para hospitalizacion
    @property
    def obtener_diagnostico_relacionado_1(self):
        response = (self.value.diagnostico_rela1_p, self.value.diagnostico_rela1_l)
        return response

    # metodo para obtener la posicion y la longitud del diagnostico relacionado para hospitalizacion
    @property
    def obtener_diagnostico_relacionado_2(self):
        response = (self.value.diagnostico_rela2_p, self.value.diagnostico_rela2_l)
        return response

    # metodo para obtener la posicion y la longitud del diagnostico relacionado para hospitalizacion
    @property
    def obtener_diagnostico_relacionado_3(self):
        response = (self.value.diagnostico_rela3_p, self.value.diagnostico_rela3_l)
        return response

    # metodo para obtener la posicion y la longitud de la columna complicacion para hospitalizacion
    @property
    def obtener_complicacion(self):
        response = (self.value.complicacion_p, self.value.complicacion_l)
        return response

    # metodo para obtener la posicion y la longitud de la columna complicacion para hospitalizacion
    @property
    def obtener_causa_muerte(self):
        response = (self.value.causa_muerte_p, self.value.causa_muerte_l)
        return response

    # metodo para obtener la posicion y la longitud de la columna fecha egreso para hospitalizacion
    @property
    def obtener_fecha_egreso(self):
        response = (self.value.fch_egreso_p, self.value.fch_egreso_l)
        return response

    # metodo para obtener la posicion y la longitud de la columna fecha egreso para hospitalizacion
    @property
    def obtener_hora_egreso(self):
        response = (self.value.hora_egreso_p, self.value.hora_egreso_l)
        return response

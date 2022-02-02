from enum import Enum
from collections import namedtuple

HospitalizacionesColumnas = namedtuple('Hospitalizaciones',
                                       ['n_factura_posicion', 'codigo_prestador_posicion', 'tipo_id_posicion',
                                        'id_posicion', 'via_ingreso_p', 'fch_ingreso_p', 'hora_ingreso_p',
                                        'n_autorizacion_p', 'causa_ext_p', 'diagnostico_princ_ingreso_p',
                                        'diagnostico_princ_egreso_p', 'diagnostico_rela1_p', 'diagnostico_rela2_p',
                                        'diagnostico_rela3_p', 'complicacion_p', 'estado_salida_p', 'causa_muerte_p',
                                        'fch_egreso_p', 'hora_egreso_p'])


class HospitalizacionesColumnasEnum(Enum):
    AH = HospitalizacionesColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)

    @property
    def obtener_lista(self):
        """
        Metodo para obtener la lista con las posiciones y longitudes
        :return:
        """
        lista_archivo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        return lista_archivo

    @property
    def obtener_codigo_prestador(self):
        """
        Metodo para obtenerla posicion y longitud de la columna codigo prestador del archivo de Transacciones
        :return:
        """
        response = self.value.codigo_prestador_posicion
        return response

    @property
    def obtener_tipo_id(self):
        """
        Metodo para obtener el tipo de id
        :return:
        """
        response = self.value.tipo_id_posicion
        return response

    @property
    def obtener_numero_id(self):
        """
        Metodo para obtener el numero de id hospitalizacion
        :return:
        """
        response = self.value.id_posicion
        return response

    @property
    def obtener_numero_factura(self):
        """
        Metodo para obtener la posicion y la longitud de numero de factura para hospitalizacion
        :return:
        """
        response = self.value.n_factura_posicion
        return response

    @property
    def obtener_via_ingreso(self):
        """
        Metodo para obtener la posicion y la longitud de la via de ingreso para hospitalizacion
        :return:
        """
        response = self.value.via_ingreso_p
        return response

    @property
    def obtener_fecha_ingreso(self):
        """
        Metodo para obtener la posicion y la longitud de la fecha de ingreso para hospitalizacion
        :return:
        """
        response = self.value.fch_ingreso_p
        return response

    @property
    def obtener_hora_ingreso(self):
        """
        Metodo para obtener la posicion y la longitud de la hora de ingreso para hospitalizacion
        :return:
        """
        response = self.value.hora_ingreso_p
        return response

    @property
    def obtener_numero_autorizacion(self):
        """
        Metodo para obtener la posicion y la longitud del numero de autorizacion para hospitalizacion
        :return:
        """
        response = self.value.n_autorizacion_p
        return response

    @property
    def obtener_causa_externa(self):
        """
        Metodo para obtener la posicion y la longitud de la causa externa para hospitalizacion
        :return:
        """
        response = self.value.causa_ext_p
        return response

    @property
    def obtener_estado_salida(self):
        """
        Metodo para obtener la posicion y la longitud de la columna estado a la salida  para hospitalizacion
        :return:
        """
        response = self.value.estado_salida_p
        return response

    @property
    def obtener_diagnostico_principal_ingreso(self):
        """
        Metodo para obtener la posicion y la longitud del diagnostico principal para ingreso para hospitalizacion
        :return:
        """
        response = self.value.diagnostico_princ_ingreso_p
        return response

    @property
    def obtener_diagnostico_principal_egreso(self):
        """
        Metodo para obtener la posicion y la longitud del diagnostico principal de egreso para hospitalizacion
        :return:
        """
        response = self.value.diagnostico_princ_egreso_p
        return response

    @property
    def obtener_diagnostico_relacionado_1(self):
        """
        Metodo para obtener la posicion y la longitud del diagnostico relacionado para hospitalizacion
        :return:
        """
        response = self.value.diagnostico_rela1_p
        return response

    @property
    def obtener_diagnostico_relacionado_2(self):
        """
        Metodo para obtener la posicion y la longitud del diagnostico relacionado para hospitalizacion
        :return:
        """
        response = self.value.diagnostico_rela2_p
        return response

    @property
    def obtener_diagnostico_relacionado_3(self):
        """
        Metodo para obtener la posicion y la longitud del diagnostico relacionado para hospitalizacion
        :return:
        """
        response = self.value.diagnostico_rela3_p
        return response

    @property
    def obtener_complicacion(self):
        """
        Metodo para obtener la posicion y la longitud de la columna complicacion para hospitalizacion
        :return:
        """
        response = self.value.complicacion_p
        return response

    @property
    def obtener_causa_muerte(self):
        """
        Metodo para obtener la posicion y la longitud de la columna complicacion para hospitalizacion
        :return:
        """
        response = self.value.causa_muerte_p
        return response

    @property
    def obtener_fecha_egreso(self):
        """
        Metodo para obtener la posicion y la longitud de la columna fecha egreso para hospitalizacion
        :return:
        """
        response = self.value.fch_egreso_p
        return response

    @property
    def obtener_hora_egreso(self):
        """
        Metodo para obtener la posicion y la longitud de la columna fecha egreso para hospitalizacion
        :return:
        """
        response = self.value.hora_egreso_p
        return response

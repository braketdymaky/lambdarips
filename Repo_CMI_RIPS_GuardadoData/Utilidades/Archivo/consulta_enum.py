from enum import Enum
from collections import namedtuple

ConsultaColumnas = namedtuple('Consulta',
                              ['n_factura_posicion', 'codigo_prestador_posicion', 'tipo_id_posicion',
                               'id_posicion', 'fecha_consulta_posicion', 'n_autorizacion_posicion',
                               'codigo_consulta_posicion', 'finalidad_consulta_posicion',
                               'causa_externa_posicion', 'co_diagnostico_princ_posicion',
                               'co_diagnostico1_posicion', 'co_diagnostico2_posicion',
                               'co_diagnostico3_posicion', 'tp_diagnostico_princ_posicion',
                               'valor_consulta_posicion', 'valor_cuota_moderadora_posicion',
                               'valor_neto_posicon'])


class ConsultaColumnasEnum(Enum):
    AC = ConsultaColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

    @property
    def obtener_lista(self):
        lista_archivo_consulta = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        return lista_archivo_consulta

    @property
    def obtener_codigo_prestador(self):
        """
        Metodo para obtener la posicion de la columna codigo prestador
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
        Metodo para obtener el numero de id
        :return:
        """
        response = self.value.id_posicion
        return response

    @property
    def obtener_numero_factura(self):
        """
        Metodo para obtener de numero de factura
        :return:
        """
        response = self.value.n_factura_posicion
        return response

    @property
    def obtener_fecha_consulta(self):
        """
        Metodo para obtener la posicion y longitud  feha de consulta
        :return:
        """
        response = self.value.fecha_consulta_posicion
        return response

    @property
    def obtener_numero_autorizacion(self):
        """
        Metodo para obtener la posicion y longitud  feha de consulta
        :return:
        """
        response = self.value.n_autorizacion_posicion
        return response

    @property
    def obtener_codigo_consulta(self):
        """
        Metodo para obtener la posicion y longitud  codigo de la consulta
        :return:
        """
        response = self.value.codigo_consulta_posicion
        return response

    @property
    def obtener_finalidad_consulta(self):
        """
        Metodo para obtener la posicion y longitud  finalidad de la consulta
        :return:
        """
        response = self.value.finalidad_consulta_posicion
        return response

    @property
    def obtener_causa_externa(self):
        """
        Metodo para obtener la posicion y longitud  causa externa de la consulta
        :return:
        """
        response = self.value.causa_externa_posicion
        return response

    @property
    def obtener_diagnostico_principal(self):
        """
        Metodo para obtener la posicion y longitud  diagnostico principal de la consulta
        :return:
        """
        response = self.value.co_diagnostico_princ_posicion
        return response

    @property
    def obtener_diagnostico_relacionado_1(self):
        """
        Metodo para obtener la posicion y longitud  diagnostico relacionado 1 de la consulta
        :return:
        """
        response = self.value.co_diagnostico1_posicion
        return response

    @property
    def obtener_diagnostico_relacionado_2(self):
        """
        Metodo para obtener la posicion y longitud  diagnostico relacionado 2 de la consulta
        :return:
        """
        response = self.value.co_diagnostico2_posicion
        return response

    @property
    def obtener_diagnostico_relacionado_3(self):
        """
        Metodo para obtener la posicion y longitud  diagnostico relacionado 3 de la consulta
        :return:
        """
        response = self.value.co_diagnostico3_posicion
        return response

    @property
    def obtener_tipo_diagnostico(self):
        """
        Metodo para obtener la posicion y longitud tipo diagnostico principal de la consulta
        :return:
        """
        response = self.value.tp_diagnostico_princ_posicion
        return response

    @property
    def obtener_valor_consulta(self):
        """
        Metodo para obtener la posicion y longitud del valor de la consulta
        :return:
        """
        response = self.value.valor_consulta_posicion
        return response

    @property
    def obtener_valor_cuota_moderadora(self):
        """
        Metodo para obtener la posicion y longitud del valor la cuota moderadora de la consulta
        :return:
        """
        response = self.value.valor_cuota_moderadora_posicion
        return response

    @property
    def obtener_valor_neto(self):
        """
        Metodo para obtener la posicion y longitud del valor neto de la consulta
        :return:
        """
        response = self.value.valor_neto_posicon
        return response

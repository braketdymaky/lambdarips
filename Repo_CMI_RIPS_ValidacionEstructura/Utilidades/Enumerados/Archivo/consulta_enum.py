# enum necesarios para las constantes pertenecientes al archivo de consultas
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion 
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
ArchivosConsultaColumnas = namedtuple('ArchivosConsultaArchivo',
                                      ['n_factura_posicion', 'n_factura_longitud',
                                       'codigo_prestador_posicion', 'codigo_prestador_longitud',
                                       'tipo_id_posicion', 'tipo_id_logitud',
                                       'id_posicion', 'id_longitud',
                                       'fecha_consulta_posicion', 'fecha_consulta_longitud',
                                       'n_autorizacion_posicion', 'n_autorizacion_longitud',
                                       'codigo_consulta_posicion', 'codigo_consulta_longitud',
                                       'finalidad_consulta_posicion', 'finalidad_consulta_longitud',
                                       'causa_externa_posicion', 'causa_externa_longitud',
                                       'co_diagnostico_princ_posicion', 'co_diagnostico_pirnc_longitud',
                                       'co_diagnostico1_posicion', 'co_diagnostico1_longitud',
                                       'co_diagnostico2_posicion', 'co_diagnostico2_longitud',
                                       'co_diagnostico3_posicion', 'co_diagnostico3_longitud',
                                       'tp_diagnostico_princ_posicion', 'tp_diagnostico_pirnc_longitud',
                                       'valor_consulta_posicion', 'valor_consulta_longitud',
                                       'valor_cuota_moderadora_posicion', 'valor_cuota_moderadora_longitud',
                                       'valor_neto_posicon', 'valor_neto_longitud'])


class ArchivosConsultaColumnasEnum(Enum):
    AC = ArchivosConsultaColumnas(0, 20, 1, 12, 2, 2, 3, 20, 4, 10, 5, 20, 6, 8, 7, 2, 8, 2, 9, 4, 10, 4, 11, 4, 12, 4,
                                  13, 1, 14, 15, 15, 15, 16, 15)

    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_archivo_consulta = [[0, 20], [1, 12], [2, 2], [3, 16], [4, 10], [5, 20], [6, 8], [7, 2], [8, 2], [9, 4],
                                  [10, 4], [11, 4], [12, 4], [13, 1], [14, 15], [15, 15], [16, 15]]
        return lista_archivo_consulta

    # Metodo para obtener la posicion y longitud de la columna codigo prestador del archivo de Transacciones
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
    def obtener_fecha_consulta(self):
        response = (self.value.fecha_consulta_posicion, self.value.fecha_consulta_longitud)
        return response

    # metodo para obtener la posicion y longitud  feha de consulta
    @property
    def obtener_numero_autorizacion(self):
        response = (self.value.n_autorizacion_posicion, self.value.n_autorizacion_longitud)
        return response

    # metodo para obtener la posicion y longitud  codigo de la consulta
    @property
    def obtener_codigo_consulta(self):
        response = (self.value.codigo_consulta_posicion, self.value.codigo_consulta_longitud)
        return response

    # metodo para obtener la posicion y longitud  finalidad de la consulta
    @property
    def obtener_finalidad_consulta(self):
        response = (self.value.finalidad_consulta_posicion, self.value.finalidad_consulta_longitud)
        return response

    # metodo para obtener la posicion y longitud  causa externa de la consulta
    @property
    def obtener_causa_externa(self):
        response = (self.value.causa_externa_posicion, self.value.causa_externa_longitud)
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

    # metodo para obtener la posicion y longitud tipo diagnostico principal de la consulta
    @property
    def obtener_tipo_diagnostico(self):
        response = (self.value.tp_diagnostico_princ_posicion, self.value.tp_diagnostico_pirnc_longitud)
        return response

    # metodo para obtener la posicion y longitud del valor de la consulta
    @property
    def obtener_valor_consulta(self):
        response = (self.value.valor_consulta_posicion, self.value.valor_consulta_longitud)
        return response

    # metodo para obtener la posicion y longitud del valor la cuota moderadora de la consulta
    @property
    def obtener_valor_cuota_moderadora(self):
        response = (self.value.valor_cuota_moderadora_posicion, self.value.valor_cuota_moderadora_longitud)
        return response

    # metodo para obtener la posicion y longitud del valor neto de la consulta
    @property
    def obtener_valor_neto(self):
        response = (self.value.valor_neto_posicon, self.value.valor_neto_longitud)
        return response

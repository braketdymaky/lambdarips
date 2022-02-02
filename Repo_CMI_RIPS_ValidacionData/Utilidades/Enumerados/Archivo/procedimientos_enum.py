from enum import Enum
from collections import namedtuple

ProcedimientosColumnas = namedtuple('Procedimientos',
                                    ['n_factura_posicion', 'codigo_prestador_posicion', 'tipo_id_posicion',
                                     'id_posicion', 'fecha_procedimiento_posicion', 'n_autorizacion_posicion',
                                     'codigo_procedimiento_posicion', 'ambito_posicion', 'finalidad_posicion',
                                     'personal_posicion', 'co_diagnostico_princ_posicion', 'co_diagnostico1_posicion',
                                     'complicacion_posicion', 'act_quirurgico_posicion', 'valor_posicion'])


class ProcedimientosColumnasEnum(Enum):
    AP = ProcedimientosColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    @property
    def obtener_lista(self):
        """
        Metodo para obtener la lista con las posiciones y longitudes
        :return: 
        """
        lista_archivo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
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
    def obtener_fecha_procedimiento(self):
        """
        Metodo para obtener la posicion
        :return:
        """
        response = self.value.fecha_procedimiento_posicion
        return response

    @property
    def obtener_numero_autorizacion(self):
        """
        Metodo para obtener la posicion y longitud  feha del procedimiento
        :return:
        """
        response = self.value.n_autorizacion_posicion
        return response

    @property
    def obtener_codigo_procedimiento(self):
        """
        Metodo para obtener la posicion y longitud  codigo del procedimiento
        :return:
        """
        response = self.value.codigo_procedimiento_posicion
        return response

    @property
    def obtener_finalidad_procedimiento(self):
        """
        Metodo para obtener la posicion y longitud  finalidad del procedimiento
        :return:
        """
        response = self.value.finalidad_posicion
        return response

    @property
    def obtener_diagnostico_principal(self):
        """
        Metodo para obtener la posicion y longitud  diagnostico principal del procedimiento
        :return:
        """
        response = self.value.co_diagnostico_princ_posicion
        return response

    @property
    def obtener_diagnostico_relacionado_1(self):
        """
        Metodo para obtener la posicion y longitud  diagnostico relacionado 1 del procedimiento
        :return:
        """
        response = self.value.co_diagnostico1_posicion
        return response

    @property
    def obtener_ambito(self):
        """
        Metodo para obtener la posicion y longitud  ambito del procedimiento
        :return:
        """
        response = self.value.ambito_posicion
        return response

    @property
    def obtener_personal_que_atendio(self):
        """
        Metodo para obtener la posicion y longitud  ambito del procedimiento
        :return:
        """
        response = self.value.personal_posicion
        return response

    @property
    def obtener_complicacion(self):
        """
        Metodo para obtener la posicion y longitud  complicacion del procedimiento
        :return:
        """
        response = self.value.complicacion_posicion
        return response

    @property
    def obtener_realizacion_act_quirurgico(self):
        """
        Metodo para obtener la posicion y longitud  ambito del procedimiento
        :return:
        """
        response = self.value.act_quirurgico_posicion
        return response

    @property
    def obtener_valor(self):
        """
        Metodo para obtener la posicion y longitud  ambito del procedimiento
        :return:
        """
        response = self.value.valor_posicion
        return response

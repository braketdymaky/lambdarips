# enum necesarios para las constantes pertenecientes al archivo de procedimientos
# 22/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion 
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
ProcedimientosColumnas = namedtuple('ProcedimientosArchivo',
                                    ['n_factura_posicion', 'n_factura_longitud',
                                     'codigo_prestador_posicion', 'codigo_prestador_longitud',
                                     'tipo_id_posicion', 'tipo_id_logitud',
                                     'id_posicion', 'id_longitud',
                                     'fecha_procedimiento_posicion', 'fecha_procedimiento_longitud',
                                     'n_autorizacion_posicion', 'n_autorizacion_longitud',
                                     'codigo_procedimiento_posicion', 'codigo_procedimiento_longitud',
                                     'ambito_posicion', 'ambito_longitud',
                                     'finalidad_posicion', 'finalidad_longitud',
                                     'personal_posicion', 'personal_longitud',
                                     'co_diagnostico_princ_posicion', 'co_diagnostico_pirnc_longitud',
                                     'co_diagnostico1_posicion', 'co_diagnostico1_longitud',
                                     'complicacion_posicion', 'complicacion_longitud',
                                     'act_quirurgico_posicion', 'act_quirurgico_longitud',
                                     'valor_posicion', 'valor_longitud'])


class ProcedimientosColumnasEnum(Enum):
    AP = ProcedimientosColumnas(0, 20, 1, 10, 2, 2, 3, 16, 4, 10, 5, 20, 6, 8, 7, 1, 8, 1, 9, 1, 10, 4, 11, 4, 12, 4,
                                13, 1, 14, 15)

    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_archivo =[[0, 20], [1, 12], [2, 2], [3, 16], [4, 10], [5, 20], [6, 8], [7, 1], [8, 1], [9, 1], [10, 4], [11, 4], [12, 4],[13, 1], [14, 15]]
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

    # metodo para obtener la posicion y longitud  feha del procedimiento
    @property
    def obtener_fecha_procedimiento(self):
        response = (self.value.fecha_procedimiento_posicion, self.value.fecha_procedimiento_longitud)
        return response

    # metodo para obtener la posicion y longitud  feha del procedimiento
    @property
    def obtener_numero_autorizacion(self):
        response = (self.value.n_autorizacion_posicion, self.value.n_autorizacion_longitud)
        return response

    # metodo para obtener la posicion y longitud  codigo del procedimiento
    @property
    def obtener_codigo_procedimiento(self):
        response = (self.value.codigo_procedimiento_posicion, self.value.codigo_procedimiento_longitud)
        return response

    # metodo para obtener la posicion y longitud  finalidad del procedimiento
    @property
    def obtener_finalidad_procedimiento(self):
        response = (self.value.finalidad_posicion, self.value.finalidad_longitud)
        return response

    # metodo para obtener la posicion y longitud  diagnostico principal del procedimiento
    @property
    def obtener_diagnostico_principal(self):
        response = (self.value.co_diagnostico_princ_posicion, self.value.co_diagnostico_pirnc_longitud)
        return response

    # metodo para obtener la posicion y longitud  diagnostico relacionado 1 del procedimiento
    @property
    def obtener_diagnostico_relacionado_1(self):
        response = (self.value.co_diagnostico1_posicion, self.value.co_diagnostico1_longitud)
        return response

    # metodo para obtener la posicion y longitud  ambito del procedimiento
    @property
    def obtener_ambito(self):
        response = (self.value.ambito_posicion, self.value.ambito_longitud)
        return response

    # metodo para obtener la posicion y longitud  ambito del procedimiento
    @property
    def obtener_personal_que_atendio(self):
        response = (self.value.personal_posicion, self.value.personal_longitud)
        return response

    # metodo para obtener la posicion y longitud  complicacion del procedimiento
    @property
    def obtener_complicacion(self):
        response = (self.value.complicacion_posicion, self.value.complicacion_longitud)
        return response

    # metodo para obtener la posicion y longitud  ambito del procedimiento
    @property
    def obtener_realizacion_act_quirurgico(self):
        response = (self.value.act_quirurgico_posicion, self.value.act_quirurgico_longitud)
        return response

    # metodo para obtener la posicion y longitud  ambito del procedimiento
    @property
    def obtener_valor(self):
        response = (self.value.valor_posicion, self.value.valor_longitud)
        return response

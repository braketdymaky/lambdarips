# enum necesarios para las constantes pertenecientes al archivo de recien nacidos
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion 
# $ la ubicacion de la columna y la segunda su longitud esperada
# la letra p al final denota posicion y la l longitud

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
RecienNacidosColumnas = namedtuple('UrgenciasArchivo',
                                   ['n_factura_posicion', 'n_factura_longitud',
                                    'codigo_prestador_posicion', 'codigo_prestador_longitud',
                                    'tipo_id_posicion', 'tipo_id_logitud',
                                    'id_posicion', 'id_longitud',
                                    'fch_nacimiento_p', 'fch_nacimiento_l',
                                    'hora_nacimiento_p', 'hora_nacimiento_l',
                                    'edad_gestacional_p', 'edad_gestacional_l',
                                    'ctrl_prenatal_p', 'ctrl_prenatal_l',
                                    'sexo_nacido_p', 'sexo_nacido_l',
                                    'peso_nacido_p', 'peso_nacido_l',
                                    'diagnostico_p', 'diagnostico_l',
                                    'causa_muerte_p', 'causa_muerte_l',
                                    'fch_muerte_p', 'fch_muerte_l',
                                    'hora_muerte_p', 'hora_muerte_l'])


class RecienNacidosColumnaEnum(Enum):
    AN = RecienNacidosColumnas(0, 20, 1, 12, 2, 2, 3, 20, 4, 10, 5, 5, 6, 2, 7, 1, 8, 1, 9, 4, 10, 4, 11, 4, 12, 10, 13,
                               5)
    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_archivo =[[0, 20], [1, 12], [2, 2], [3, 20], [4, 10], [5, 5], [6, 2], [7, 1], [8, 1], [9, 4], [10, 4], [11, 4], [12, 10], [13,5]]
        return lista_archivo

    # Metodo para obtenerla posicion y longitud de la columna codigo prestador
    def obtener_codigo_prestador(self):
        response = (self.value.codigo_prestador_posicion, self.value.codigo_prestador_longitud)
        return response

    # metodo para obtener el tipo de id de la madre en el archivo recien nacidos
    @property
    def obtener_tipo_id_madre(self):
        response = (self.value.tipo_id_posicion, self.value.tipo_id_logitud)
        return response

    # metodo para obtener la longitud y posicion para la columna de numero id de la madre en el archivo recien nacidos
    @property
    def obtener_numero_id_madre(self):
        response = (self.value.id_posicion, self.value.id_longitud)
        return response

    # metodo para obtener la longitud y posicion para la columna de fecha de nacimiento en el archivo recien nacidos
    @property
    def obtener_fecha_nacimiento(self):
        response = (self.value.fch_nacimiento_p, self.value.fch_nacimiento_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de hora de nacimiento en el archivo recien nacidos
    @property
    def obtener_hora_nacimiento(self):
        response = (self.value.hora_nacimiento_p, self.value.hora_nacimiento_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de edad gestacional en el archivo recien nacidos
    @property
    def obtener_edad_gestacional(self):
        response = (self.value.edad_gestacional_p, self.value.edad_gestacional_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de control prenatal en el archivo recien nacidos
    @property
    def obtener_control_prenatal(self):
        response = (self.value.ctrl_prenatal_p, self.value.ctrl_prenatal_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de sexo del recien nacido en el archivo recien nacidos
    @property
    def obtener_sexo_nacido(self):
        response = (self.value.sexo_nacido_p, self.value.sexo_nacido_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de sexo del peso nacido en el archivo recien nacidos
    @property
    def obtener_peso_nacido(self):
        response = (self.value.peso_nacido_p, self.value.peso_nacido_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de sdiagnositco del nacido en el archivo recien nacidos
    @property
    def obtener_diagnostico_de_nacido(self):
        response = (self.value.diagnostico_p, self.value.diagnostico_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de causa de muerte del nacido en el archivo recien nacidos
    @property
    def obtener_causa_de_muerte(self):
        response = (self.value.causa_muerte_p, self.value.causa_muerte_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de fecha de muerte del nacido en el archivo recien nacidos
    @property
    def obtener_fecha_de_muerte(self):
        response = (self.value.fch_muerte_p, self.value.fch_muerte_l)
        return response

    # metodo para obtener la longitud y posicion para la columna de hora de muerte del nacido en el archivo recien nacidos
    @property
    def obtener_hora_de_muerte(self):
        response = (self.value.hora_muerte_p, self.value.hora_muerte_l)
        return response

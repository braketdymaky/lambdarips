# enum necesarios para las constantes pertenecientes al archivo de Transacciones
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posición
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado

UsuariosColumnas = namedtuple('TransaccionesArchivo',
                              ['tipo_id_posicion', 'tipo_id_logitud',
                               'id_posicion', 'id_longitud',
                               'codigo_prestador_posicion', 'codigo_prestador_longitud',
                               'tipo_usuario_posicion', 'tipo_usuario_longitud',
                               'p_apellido_posicion', 'p_apellido_longitud',
                               's_apellido_posicon', 's_apellido_longitud',
                               'p_nombre_posicion', 'p_nombre_longitud',
                               's_nombre_posicion', 's_nombre_longitud',
                               'edad_poscion', 'edad_longitud',
                               'u_medida_edad_posicion', 'u_medida_edad_longitud',
                               'sexo_posicion', 'sexo_longitud',
                               'c_dpto_residencia_posicion', 'c_dpto_residencia_longitud',
                               'c_municipio_residencia_posicion', 'c_municipio_residencia_longitud',
                               'zona_residencial_posicion', 'zona_residencial_longitud'])


class UsuariosColumnasEnum(Enum):
    US = UsuariosColumnas(0, 2, 1, 16, 2, 6, 3, 1, 4, 30, 5, 30, 6, 20, 7, 20, 8, 3, 9, 1, 10, 1, 11, 2, 12, 3, 13, 1)
    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista = [[0, 2], [1, 16], [2, 6], [3, 1], [4, 30], [5, 30], [6, 20], [7, 20], [8, 3], [9, 1], [10, 1], [11, 2], [12, 3], [13, 1]]
        return lista

    # Método para obtenerla posición y longitud de la columna codigo prestador del archivo de Transacciones
    @property
    def obtener_codigo_prestador(self):
        response = (self.value.codigo_prestador_posicion, self.value.codigo_prestador_longitud)
        return response

    # Método para obtener el tipo de id
    @property
    def obtener_tipo_id(self):
        response = (self.value.tipo_id_posicion, self.value.tipo_id_logitud)
        return response

    # Método para obtener la posición y longitud del numero de id
    @property
    def obtener_numero_id(self):
        response = (self.value.id_posicion, self.value.id_longitud)
        return response

    # Método para obtener la posición y longitud del tipo del usuario
    @property
    def obtener_tipo_usuario(self):
        response = (self.value.tipo_usuario_posicion, self.value.tipo_usuario_longitud)
        return response

    # Método para obtener la posición y longitud del primer apellido
    @property
    def obtener_primer_apellido(self):
        response = (self.value.p_apellido_posicion, self.value.p_apellido_longitud)
        return response

    # Método para obtener la posición y longitud el segundo apellido del usuario
    @property
    def obtener_segundo_apellido(self):
        response = (self.value.s_apellido_posicon, self.value.s_apellido_longitud)
        return response

    # Método para obtener la posición y longitud el primer nombre del usuario
    @property
    def obtener_primer_nombre(self):
        response = (self.value.p_nombre_posicion, self.value.p_nombre_longitud)
        return response

    # Método para obtener la posición y longitud el segundo nombre del usuario
    @property
    def obtener_segundo_nombre(self):
        response = (self.value.s_nombre_posicion, self.value.s_nombre_longitud)
        return response

    # Método para obtener la posición y longitud la edad del usuario
    @property
    def obtener_edad(self):
        response = (self.value.edad_poscion, self.value.edad_longitud)
        return response

    # Método para obtener la posición y longitud la unidad de medida de edad del usuario
    @property
    def obtener_medida_de_edad(self):
        response = (self.value.u_medida_edad_posicion, self.value.u_medida_edad_longitud)
        return response

    # Método para obtener la posición y longitud el departamento del usuario
    @property
    def obtener_departamento_residencia(self):
        response = (self.value.c_dpto_residencia_posicion, self.value.c_dpto_residencia_longitud)
        return response

    # Método para obtener la posición y longitud el municipio de residencia del usuario
    @property
    def obtener_municipio_residencia(self):
        response = (self.value.c_municipio_residencia_posicion, self.value.c_municipio_residencia_longitud)
        return response

    # Método para obtener la posición y longitud el zona residencial del usuario
    @property
    def obtener_zona_residencial(self):
        response = (self.value.zona_residencial_posicion, self.value.zona_residencial_longitud)
        return response



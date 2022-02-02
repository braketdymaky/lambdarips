# enum necesarios para las constantes pertenecientes al archivo de Transacciones
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado

UsuariosColumnas = namedtuple('Usuarios', ['tipo_id_posicion', 'id_posicion', 'codigo_prestador_posicion',
                                           'tipo_usuario_posicion', 'p_apellido_posicion',
                                           's_apellido_posicon', 'p_nombre_posicion', 's_nombre_posicion',
                                           'edad_poscion', 'u_medida_edad_posicion', 'sexo_posicion',
                                           'c_dpto_residencia_posicion', 'c_municipio_residencia_posicion',
                                           'zona_residencial_posicion'])


class UsuariosColumnasEnum(Enum):
    US = UsuariosColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    @property
    def obtener_lista(self):
        """
        Metodo para obtener la lista con las posiciones
        :return:
        """
        lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        return lista

    @property
    def obtener_codigo_prestador(self):
        """
        Metodo para obtenerla posicion de la columna codigo prestador del archivo
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
        Metodo para obtener la posicion y longitud del numero de id
        :return:
        """
        response = self.value.id_posicion
        return response

    @property
    def obtener_tipo_usuario(self):
        """
        Metodo para obtener la posicion y longitud del tipo del usuario
        :return:
        """
        response = self.value.tipo_usuario_posicion
        return response

    @property
    def obtener_primer_apellido(self):
        """
        Metodo para obtener la posicion y longitud del primer apellido
        :return:
        """
        response = self.value.p_apellido_posicion
        return response

    @property
    def obtener_segundo_apellido(self):
        """
        Metodo para obtener la posicion y longitud el segundo apellido del usuario
        :return:
        """
        response = self.value.s_apellido_posicon
        return response

    @property
    def obtener_primer_nombre(self):
        """
        Metodo para obtener la posicion y longitud el primer nombre del usuario
        :return:
        """
        response = self.value.p_nombre_posicion
        return response

    @property
    def obtener_segundo_nombre(self):
        """
        Metodo para obtener la posicion y longitud el segundo nombre del usuario
        :return:
        """
        response = self.value.s_nombre_posicion
        return response

    @property
    def obtener_edad(self):
        """
        Metodo para obtener la posicion y longitud la edad del usuario
        :return:
        """
        response = self.value.edad_poscion
        return response

    @property
    def obtener_medida_de_edad(self):
        """
        Metodo para obtener la posicion y longitud la unidad de medida de edad del usuario
        :return:
        """
        response = self.value.u_medida_edad_posicion
        return response

    @property
    def obtener_sexo(self):
        """
        Metodo para obtener la posicion y longitud de sexo
        :return:
        """
        response = self.value.sexo_posicion
        return response

    @property
    def obtener_departamento_residencia(self):
        """
        Metodo para obtener la posicion y longitud el departamento del usuario
        :return:
        """
        response = self.value.c_dpto_residencia_posicion
        return response

    @property
    def obtener_municipio_residencia(self):
        """
        Metodo para obtener la posicion y longitud el municipio de residencia del usuario
        :return:
        """
        response = self.value.c_municipio_residencia_posicion
        return response

    @property
    def obtener_zona_residencial(self):
        """
        Metodo para obtener la posicion y longitud el zona residencial del usuario
        :return:
        """
        response = self.value.zona_residencial_posicion
        return response

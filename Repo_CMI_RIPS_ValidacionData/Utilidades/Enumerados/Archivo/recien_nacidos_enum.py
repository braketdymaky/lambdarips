from enum import Enum
from collections import namedtuple

RecienNacidosColumnas = namedtuple('RecienNacidos',
                                   ['n_factura_posicion', 'codigo_prestador_posicion', 'tipo_id_posicion',
                                    'id_posicion', 'fch_nacimiento_p', 'hora_nacimiento_p', 'edad_gestacional_p',
                                    'ctrl_prenatal_p', 'sexo_nacido_p', 'peso_nacido_p', 'diagnostico_p',
                                    'causa_muerte_p', 'fch_muerte_p', 'hora_muerte_p'])


class RecienNacidosColumnaEnum(Enum):
    AN = RecienNacidosColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    @property
    def obtener_lista(self):
        """
        Metodo para obtener la lista con las posiciones y longitudes
        :return: 
        """
        lista_archivo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        return lista_archivo
        
    @property
    def obtener_numero_factura(self):
        """
        Metodo para obtenerla posicion de la columna numero factura
        :return:
        """
        response = self.value.n_factura_posicion
        return response
        
    @property
    def obtener_codigo_prestador(self):
        """
        Metodo para obtenerla posicion de la columna codigo prestador
        :return:
        """
        response = self.value.codigo_prestador_posicion
        return response

    @property
    def obtener_tipo_id_madre(self):
        """
        Metodo para obtener el tipo de id de la madre en el archivo recien nacidos
        :return:
        """
        response = self.value.tipo_id_posicion
        return response

    @property
    def obtener_numero_id_madre(self):
        """
        Metodo para obtener la longitud y posicion para la columna de numero id de la madre en el archivo recien nacidos
        :return:
        """
        response = self.value.id_posicion
        return response

    @property
    def obtener_fecha_nacimiento(self):
        """
        Metodo para obtener la longitud y posicion para la columna de fecha de nacimiento en el archivo recien nacidos
        :return:
        """
        response = self.value.fch_nacimiento_p
        return response

    @property
    def obtener_hora_nacimiento(self):
        """
        Metodo para obtener la longitud y posicion para la columna de hora de nacimiento en el archivo recien nacidos
        :return:
        """
        response = self.value.hora_nacimiento_p
        return response

    @property
    def obtener_edad_gestacional(self):
        """
        Metodo para obtener la longitud y posicion para la columna de edad gestacional en el archivo recien nacidos
        :return:
        """
        response = self.value.edad_gestacional_p
        return response

    @property
    def obtener_control_prenatal(self):
        """
        Metodo para obtener la longitud y posicion para la columna de control prenatal en el archivo recien nacidos
        :return:
        """
        response = self.value.ctrl_prenatal_p
        return response

    @property
    def obtener_sexo_nacido(self):
        """
        Metodo para obtener la longitud y posicion para la columna de sexo del recien nacido en el archivo recien
         nacidos
        :return:
        """
        response = self.value.sexo_nacido_p
        return response

    @property
    def obtener_peso_nacido(self):
        """
        Metodo para obtener la longitud y posicion para la columna de sexo del peso nacido en el archivo recien nacidos
        :return:
        """
        response = self.value.peso_nacido_p
        return response

    @property
    def obtener_diagnostico_de_nacido(self):
        """
        Metodo para obtener la longitud y posicion para la columna de sdiagnositco del nacido en el archivo recien
        nacidos
        :return:
        """
        response = self.value.diagnostico_p
        return response

    @property
    def obtener_causa_de_muerte(self):
        """
        Metodo para obtener la longitud y posicion para la columna de causa de muerte del nacido en el archivo recien
        nacidos
        :return:
        """
        response = self.value.causa_muerte_p
        return response

    @property
    def obtener_fecha_de_muerte(self):
        """
        Metodo para obtener la longitud y posicion para la columna de fecha de muerte del nacido en el archivo recien
         nacidos
        :return:
        """
        response = self.value.fch_muerte_p
        return response

    @property
    def obtener_hora_de_muerte(self):
        """
        Metodo para obtener la longitud y posicion para la columna de hora de muerte del nacido en el archivo recien
         nacidos
        :return:
        """
        response = self.value.hora_muerte_p
        return response

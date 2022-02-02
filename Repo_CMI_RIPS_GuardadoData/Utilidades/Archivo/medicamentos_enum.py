# enum necesarios para las constantes pertenecientes al archivo de medicamentos
# 22/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posicion 
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
MedicamentosColumnas = namedtuple('ProcedimientosArchivo',
                                  ['n_factura_posicion', 'codigo_prestador_posicion', 'tipo_id_posicion', 'id_posicion',
                                   'n_autorizacion_posicion', 'codigo_p', 'tipo_p', 'nombre_generico_p',
                                   'formula_farmaceutica_p', 'concentracion_p', 'unidad_p', 'numero_unidades_p',
                                   'valor_unitario_p', 'valor_total_p', ])


class MedicamentosColumnasEnum(Enum):
    AM = MedicamentosColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    @property
    def obtener_lista(self):
        """
        Metodo para obtener la lista con las posiciones y longitudes
        :return:
        """
        lista_archivo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        return lista_archivo

    @property
    def obtener_codigo_prestador(self):
        """
        Metodo para obtenerla posicion y longitud de la columna codigo prestador del archivo de procedimiento
        :return:
        """
        response = self.value.codigo_prestador_posicion
        return response

    # metodo para obtener el tipo de id del procedimiento
    @property
    def obtener_tipo_id(self):
        response = self.value.tipo_id_posicion
        return response

    # metodo para obtener el numero de id del procedimiento
    @property
    def obtener_numero_id(self):
        response = self.value.id_posicion
        return response

    # metodo para obtener de numero de factura del procedimiento
    @property
    def obtener_numero_factura(self):
        response = self.value.n_factura_posicion
        return response

    # metodo para obtener la posicion y longitud  numero de autorizacion
    @property
    def obtener_numero_autorizacion(self):
        response = self.value.n_autorizacion_posicion
        return response

    # metodo para obtener la posicion y longitud  de la columna codigo del medicamento para el archivo de medicamentos
    @property
    def obtener_codigo_medicamento(self):
        response = self.value.codigo_p
        return response

    # metodo para obtener la posicion y longitud  de la columna tipo del medicamento para el archivo de medicamentos
    @property
    def obtener_tipo_medicamento(self):
        response = self.value.tipo_p
        return response

    # metodo para obtener la posicion y longitud  de la columna nombre generico del medicamento para el archivo de medicamentos
    @property
    def obtener_nombre_generico_medicamento(self):
        response = self.value.nombre_generico_p
        return response

    # metodo para obtener la posicion y longitud  de la columna formula farmaceutica para el archivo de medicamentos
    @property
    def obtener_formula_farmaceutica(self):
        response = self.value.formula_farmaceutica_p
        return response

    # metodo para obtener la posicion y longitud  de la columna concentracion medicamento para el archivo de medicamentos
    @property
    def obtener_concentracion_medicamento(self):
        response = self.value.concentracion_p
        return response

    # metodo para obtener la posicion y longitud  de la columna unidad de medida del medicamento medicamento para el archivo de medicamentos
    @property
    def obtener_unidad_medida_medicamento(self):
        response = self.value.unidad_p
        return response

    # metodo para obtener la posicion y longitud  de la columna  unidades unidad del medicamento para el archivo de medicamentos
    @property
    def obtener_numero_unidades(self):
        response = self.value.numero_unidades_p
        return response

    # metodo para obtener la posicion y longitud  de la columna  valor unitario del medicamento para el archivo de medicamentos
    @property
    def obtener_valor_unitario(self):
        response = self.value.valor_unitario_p
        return response

    # metodo para obtener la posicion y longitud  de la columna  valor total del medicamento para el archivo de medicamentos
    @property
    def obtener_valor_total(self):
        response = self.value.valor_total_p
        return response

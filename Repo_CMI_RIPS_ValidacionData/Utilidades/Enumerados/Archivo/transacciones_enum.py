# enum necesarios para las constantes pertenecientes al archivo de Transacciones
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posición
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado

TransaccionesColumnas = namedtuple('TransaccionesArchivo',
                                   ['codigo_prestador_posicion',
                                    'razon_social_posicion',
                                    'tipo_id_posicion',
                                    'id_posicion',
                                    'n_factura_posicion',
                                    'fecha_expedicion_posicion',
                                    'fecha_inicio_posicion',
                                    'fecha_final_posicion',
                                    'codigo_entidad_posicion',
                                    'nombre_entidad_posicion',
                                    'n_contrato_posicion',
                                    'plan_beneficios_posicion',
                                    'n_pliza_posicion',
                                    'valor_total_posicion',
                                    'valor_comision_posicion',
                                    'valor_descuentos_posicion',
                                    'valor_neto_posicion'])


class TransaccionesColumnasEnum(Enum):
    AF = TransaccionesColumnas(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                               13, 14, 15, 16)

    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_transacciones = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9],
                               [10], [11], [12], [13], [14], [15], [16]]
        return lista_transacciones

    # Método para obtenerla posición y longitud de la columna codigo prestador del archivo de Transacciones
    @property
    def obtener_codigo_prestador(self):
        response = self.value.codigo_prestador_posicion
        return response

    # Método para obtener la razón social
    @property
    def obtener_razon_social(self):
        response = self.value.razon_social_posicion
        return response

    # Método para obtener el tipo de id
    @property
    def obtener_tipo_id(self):
        response = self.value.tipo_id_posicion
        return response

    # Método para obtener el número de id
    @property
    def obtener_numero_id(self):
        response = self.value.id_posicion
        return response

    # Método para obtener de número de factura
    @property
    def obtener_numero_factura(self):
        response = self.value.n_factura_posicion
        return response

    # Método para obtener la feha de expedición
    @property
    def obtener_fecha_expedicion(self):
        response = self.value.fecha_expedicion_posicion
        return response

    # Método para obtener la fecha inicio
    @property
    def obtener_fecha_inicio(self):
        response = self.value.fecha_inicio_posicion
        return response

    # Método para obtener la fecha final
    @property
    def obtener_fecha_final(self):
        response = self.value.fecha_final_posicion
        return response

    # Método para obtener el código de la entidad
    @property
    def obtener_codigo_entidad(self):
        response = self.value.codigo_entidad_posicion
        return response

    # Método para obtener el nombre de la entidad
    @property
    def obtener_nombre_entidad(self):
        response = self.value.nombre_entidad_posicion
        return response

    # Método par abtener el número de contrato de la entidad
    @property
    def obtener_numero_contrato(self):
        response = self.value.n_contrato_posicion
        return response

    # Método para obtener el codigo del plan de beneficios de la entidad
    @property
    def obtener_plan_beneficios(self):
        response = self.value.plan_beneficios_posicion
        return response

    # Método par aobtener el número de poliza del contrato
    @property
    def obtener_numero_poliza(self):
        response = self.value.n_pliza_posicion
        return response

    # Método para obtener el valor total del contrato
    @property
    def obtener_valor_total(self):
        response = self.value.valor_total_posicion
        return response

    # Método par aobtener el valor de la comision por las Transacciones
    @property
    def obtener_valor_comision(self):
        response = self.value.valor_comision_posicion
        return response

    # Método para obtener el valor de descuento para la transacción
    @property
    def obtener_valor_descuentos(self):
        response = self.value.valor_descuentos_posicion
        return response

    # Método para obtener el valor neto de la transacción
    @property
    def obtener_valor_neto(self):
        response = self.value.valor_neto_posicion
        return response

# enum necesarios para las constantes pertenecientes al archivo de Transacciones
# 21/05/2019 ANDERSON ARIZA
# los metodos retorna una lista con dos valores, siendo la primera posición
# $ la ubicacion de la columna y la segunda su longitud esperada

from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado

TransaccionesColumnas = namedtuple('TransaccionesArchivo',
                                   ['codigo_prestador_posicion', 'codigo_prestador_longitud',
                                    'razon_social_posicion', 'razon_social_longitud',
                                    'tipo_id_posicion', 'tipo_id_logitud',
                                    'id_posicion', 'id_longitud',
                                    'n_factura_posicion', 'n_factura_longitud',
                                    'fecha_expedicion_posicion', 'fecha_expedicion_longitud',
                                    'fecha_inicio_posicion', 'fecha_inicio_longitud',
                                    'fecha_final_posicion', 'fecha_final_longitud',
                                    'codigo_entidad_posicion', 'codigo_entidad_longitud',
                                    'nombre_entidad_posicion', 'nombre_entidad_longitud',
                                    'n_contrato_posicion', 'n_contrato_longitud',
                                    'plan_beneficios_posicion', 'plan_beneficios_longitud',
                                    'n_pliza_posicion', 'n_poliza_longitud',
                                    'valor_total_posicion', 'valor_total_longitud',
                                    'valor_comision_posicion', 'valor_comision_longitud',
                                    'valor_descuentos_posicion', 'valor_descuentos_longitud',
                                    'valor_neto_posicion', 'valor_neto_longitud'])


class TransaccionesColumnasEnum(Enum):
    AF = TransaccionesColumnas(0, 12, 1, 60, 2, 2, 3, 16, 4, 20, 5, 10, 6, 10, 7, 10, 8, 6, 9, 60, 10, 15,
                               11, 30, 12, 10, 13, 15, 14, 15, 15, 15, 16, 15)

    # Metodo para obtener la lista con las posiciones y longitudes
    @property
    def obtener_lista(self):
        lista_transacciones = [[0, 12], [1, 60], [2, 2], [3, 16], [4, 20], [5, 10], [6, 10],[7, 10], [8, 6], [9, 60], [10, 15], [11, 30], [12,10], [13, 15], [14, 15], [15, 15],[16, 15]]
        return lista_transacciones

    # Método para obtenerla posición y longitud de la columna codigo prestador del archivo de Transacciones
    @property
    def obtener_codigo_prestador(self):
        response = (self.value.codigo_prestador_posicion, self.value.codigo_prestador_longitud)
        return response

    # Método para obtener la razón social
    @property
    def obtener_razon_social(self):
        response = (self.value.razon_social_posicion, self.value.razon_social_longitud)
        return response

    # Método para obtener el tipo de id
    @property
    def obtener_tipo_id(self):
        response = (self.value.tipo_id_posicion, self.value.tipo_id_logitud)
        return response

    # Método para obtener el número de id
    @property
    def obtener_numero_id(self):
        response = (self.value.id_posicion, self.value.id_longitud)
        return response

    # Método para obtener de número de factura
    @property
    def obtener_numero_factura(self):
        response = (self.value.n_factura_posicion, self.value.n_factura_longitud)
        return response

    # Método para obtener la feha de expedición
    @property
    def obtener_fecha_expedicion(self):
        response = (self.value.fecha_expedicion_posicion, self.value.fecha_expedicion_longitud)
        return response

    # Método para obtener la fecha inicio
    @property
    def obtener_fecha_inicio(self):
        response = (self.value.fecha_inicio_posicion, self.value.fecha_inicio_longitud)
        return response

    # Método para obtener la fecha final
    @property
    def obtener_fecha_final(self):
        response = (self.value.fecha_final_posicion, self.value.fecha_final_longitud)
        return response

    # Método para obtener el código de la entidad
    @property
    def obtener_codigo_entidad(self):
        response = (self.value.codigo_entidad_posicion, self.value.codigo_entidad_longitud)
        return response

    # Método para obtener el nombre de la entidad
    @property
    def obtener_nombre_entidad(self):
        response = (self.value.nombre_entidad_posicion, self.value.nombre_entidad_longitud)
        return response

    # Método par abtener el número de contrato de la entidad
    @property
    def obtener_numero_contrato(self):
        response = (self.value.n_contrato_posicion, self.value.n_contrato_longitud)
        return response

    # Método para obtener el codigo del plan de beneficios de la entidad
    @property
    def obtener_plan_beneficios(self):
        response = (self.value.plan_beneficios_posicion, self.value.plan_beneficios_longitud)
        return response

    # Método par aobtener el número de poliza del contrato
    @property
    def obtener_numero_poliza(self):
        response = (self.value.n_pliza_posicion, self.value.n_poliza_longitud)
        return response

    # Método para obtener el valor total del contrato
    @property
    def obtener_valor_total(self):
        response = (self.value.valor_total_posicion, self.value.valor_total_longitud)
        return response

    # Método par aobtener el valor de la comision por las Transacciones
    @property
    def obtener_valor_comision(self):
        response = (self.value.valor_comision_posicion, self.value.valor_comision_longitud)
        return response

    # Método para obtener el valor de descuento para la transacción
    @property
    def obtener_valor_descuentos(self):
        response = (self.value.valor_descuentos_posicion, self.value.valor_descuentos_longitud)
        return response

    # Método para obtener el valor neto de la transacción
    @property
    def obtener_valor_neto(self):
        response = (self.value.valor_neto_posicion, self.value.valor_neto_longitud)
        return response

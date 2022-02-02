# -*- coding: utf-8 -*-
from Aplicacion.Base.validacion_base import ValidacionBase
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Utilidades.Enumerados.Archivo.medicamentos_enum import MedicamentosColumnasEnum as ME
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as UE
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as TSE
from Dominio.Medicamentos.medicamentos import ModeloMedicamentos


class ValidacionMedicamentos(ValidacionBase):

    def __init__(self,lista_af,lista_us,af,us):
        super().__init__()
        self.nombre_archivo = 'AM'
        self.model = ModeloMedicamentos.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.lista_af = lista_af
        self.lista_us = lista_us
        self.dic_af=af
        self.dic_us=us

    def validar_numero_factura(self, am_fila, linea_fila):
        """
        Función para validar que el numero de factura, este contenido en el archivo de transacciones
        :param am_fila:
        :param linea_fila:
        :return:
        """
        numero_factura =  am_fila[ME.AM.obtener_numero_factura]
        encontrado =  self.dic_af.get(numero_factura)
        if encontrado is None:
                self.detectar_error(TE.AM_FACTURA_NO_ENCONTRADA.obtener_descripcion, ME.AM.obtener_numero_factura,
                                    linea=linea_fila)
       

    def validar_tipo_identificacion(self, am_fila, linea_fila):
        """
        Función para validar que el tipo de identificación, este contenido en el rango de valores permitidos
        :param am_fila:
        :param linea_fila:
        :return:
        """
        try:
            valores_permitidos = self.model_fichero.obtener_tipo_id_usuario()

            encontrado = [am_fila[ME.AM.obtener_tipo_id]] in valores_permitidos

            if not encontrado:
                self.detectar_error(TE.AM_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, ME.AM.obtener_tipo_id,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AM_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, ME.AM.obtener_tipo_id,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AM_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, ME.AM.obtener_tipo_id,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AM_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, ME.AM.obtener_tipo_id,
                                linea=linea_fila)

    def validar_tipo_numero_identificacion(self, am_fila, linea_fila):
        """
        Función para validar que el tipo y numero de identificación, coincida con el archivo de usuarios
        :param am_fila:
        :param linea_fila:
        :return:
        """
        numero_id = am_fila[ME.AM.obtener_numero_id]
        encontrado =  self.dic_us.get(numero_id)
        
        if encontrado is None:
            self.detectar_error(TE.AM_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, ME.AM.obtener_numero_id,
                                    linea=linea_fila)
        elif not encontrado[UE.US.obtener_tipo_id] == am_fila[ME.AM.obtener_tipo_id]:
            self.detectar_error(TE.AM_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, ME.AM.obtener_tipo_id,
                                    linea=linea_fila)
        
    def validar_guion_numero_autorizacion(self, am_fila, linea_fila):
        """
        :param am_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico().validar_guiones_numero_autorizacion(am_fila[ME.AM.obtener_numero_autorizacion], ''):
                self.detectar_error(TE.AM_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                    ME.AM.obtener_numero_autorizacion,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AM_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                ME.AM.obtener_numero_autorizacion,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AM_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                ME.AM.obtener_numero_autorizacion,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AM_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                ME.AM.obtener_numero_autorizacion,
                                linea=linea_fila)

    def validar_nombre_generico_del_medicamento_no_nulo(self, am_fila, linea_fila):
        """
        Función para validar que el nombre genérico del medicamento este diligenciado
        :param am_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not am_fila[ME.AM.obtener_nombre_generico_medicamento]:
                self.detectar_error(TE.AM_NOMBRE_GENERICO_VACIO.obtener_descripcion,
                                    ME.AM.obtener_nombre_generico_medicamento, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AM_NOMBRE_GENERICO_VACIO.obtener_descripcion,
                                ME.AM.obtener_nombre_generico_medicamento, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AM_NOMBRE_GENERICO_VACIO.obtener_descripcion,
                                ME.AM.obtener_nombre_generico_medicamento, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AM_NOMBRE_GENERICO_VACIO.obtener_descripcion,
                                ME.AM.obtener_nombre_generico_medicamento, linea=linea_fila)

    def validar_concentracion_del_medicamento_no_nulo(self, am_fila, linea_fila):
        """
        Función para validar que la concentración del medicamento este diligenciado
        :param am_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not am_fila[ME.AM.obtener_concentracion_medicamento]:
                self.detectar_error(TE.AM_CONCENTRACION_VACIO.obtener_descripcion,
                                    ME.AM.obtener_concentracion_medicamento,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AM_CONCENTRACION_VACIO.obtener_descripcion, ME.AM.obtener_concentracion_medicamento,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AM_CONCENTRACION_VACIO.obtener_descripcion, ME.AM.obtener_concentracion_medicamento,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AM_CONCENTRACION_VACIO.obtener_descripcion, ME.AM.obtener_concentracion_medicamento,
                                linea=linea_fila)

    def validar_forma_farmaceutica_no_nulo(self, am_fila, linea_fila):
        """
        Función para validar que la forma farmaceutica del medicamento este diligenciada
        :param am_fila:
        :param linea_fila:
        :return:
        """
        if not am_fila[ME.AM.obtener_formula_farmaceutica]:
            self.detectar_error(TE.AM_FORMA_FARMACEUTICA_VACIO.obtener_descripcion, ME.AM.obtener_formula_farmaceutica,
                                linea=linea_fila)

    def validar_unidad_de_medida_del_medicamento_no_nulo(self, am_fila, linea_fila):
        """
        Función para validar que la unidad de medida del medicamento este diligenciada
        :param am_fila:
        :param linea_fila:
        :return:
        """

        if not am_fila[ME.AM.obtener_unidad_medida_medicamento]:
            self.detectar_error(TE.AM_UNIDAD_MEDIDA_VACIO.obtener_descripcion, ME.AM.obtener_unidad_medida_medicamento,
                                linea=linea_fila)

    def validar_numero_de_unidades_no_nulo(self, am_fila, linea_fila):
        """
        Función para validar que el número de unidades del medicamento este diligenciado
        :param am_fila:
        :param linea_fila:
        :return:
        """

        if not am_fila[ME.AM.obtener_numero_unidades]:
            self.detectar_error(TE.AM_NUMERO_UNIDADES_VACIO.obtener_descripcion, ME.AM.obtener_numero_unidades,
                                linea=linea_fila)

    def validar_valor_unitario_de_medicamento_no_nulo(self, am_fila, linea_fila):
        """
        Función para validar que el valor unitario del medicamento este diligenciado
        :param am_fila:
        :param linea_fila:
        :return:
        """

        if am_fila[ME.AM.obtener_numero_unidades]:
            if not am_fila[ME.AM.obtener_valor_unitario]:
                self.detectar_error(TE.AM_VALOR_UNITARIO_VACIO.obtener_descripcion, ME.AM.obtener_valor_unitario,
                                    linea=linea_fila)

    def validar_valor_total_de_medicamento(self, am_fila, linea_fila):
        """
        Función para validar que el valor total del medicamento corresponda al producto de
        valor_unitario * numero_unidades
        :param am_fila:
        :param linea_fila:
        :return:
        """
        try:
            numero_unidades = float(am_fila[ME.AM.obtener_numero_unidades])
            valor_unitario = float(am_fila[ME.AM.obtener_valor_unitario])
            total = float(am_fila[ME.AM.obtener_valor_total])
            total_cantidad = numero_unidades*valor_unitario
            if not Generico()._redondear_decimales(total_cantidad) == total:
                self.detectar_error(TE.AM_VALOR_TOTAL_INCORRECTO.obtener_descripcion, ME.AM.obtener_valor_total,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AM_VALOR_TOTAL_INCORRECTO.obtener_descripcion, ME.AM.obtener_valor_total,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AM_VALOR_TOTAL_INCORRECTO.obtener_descripcion, ME.AM.obtener_valor_total,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AM_VALOR_TOTAL_INCORRECTO.obtener_descripcion, ME.AM.obtener_valor_total,
                                linea=linea_fila)

    def validar_tipo_medicamento(self, am_fila, linea_fila):
        """
        Función para validar que el tipo de medicamento, este contenido en el rango de valores permitidos
        :param am_fila:
        :param linea_fila:
        :return:
        """
        try:
            fichero_tipo_medicamento = self.model_fichero.obtener_tipo_medicamento()
            encontrado = list(
                filter(lambda fichero: fichero[0] == am_fila[ME.AM.obtener_tipo_medicamento], fichero_tipo_medicamento))

            if not encontrado:
                self.detectar_error(TE.AM_TIPO_MEDICAMENTO_INCORRECTO.obtener_descripcion,
                                    ME.AM.obtener_tipo_medicamento, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AM_TIPO_MEDICAMENTO_INCORRECTO.obtener_descripcion, ME.AM.obtener_tipo_medicamento,
                                linea=linea_fila)

        except ValueError:
            self.detectar_error(TE.AM_TIPO_MEDICAMENTO_INCORRECTO.obtener_descripcion, ME.AM.obtener_tipo_medicamento,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AM_TIPO_MEDICAMENTO_INCORRECTO.obtener_descripcion, ME.AM.obtener_tipo_medicamento,
                                linea=linea_fila)

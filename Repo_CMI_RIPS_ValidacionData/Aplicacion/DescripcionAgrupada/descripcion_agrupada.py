# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.descripcion_agrupada_enum import DescripcionAgrupadaColumnasEnum as Columnas
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.DescripcionAgrupada.descripcion_agrupada import ModeloDescripcionAgrupada
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as Transacciones
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico


class ValidacionDescripcionAgrupada(ValidacionBase):

    def __init__(self,lista_af):
        super().__init__()
        self.nombre_archivo = 'AD'
        self.model = ModeloDescripcionAgrupada.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.lista_af = lista_af

    def validar_codigo_del_concepto(self, ad_fila, linea_fila):
        """
        función que valida que el codigo de concepto se encuentre registrado en la lista aestra correspondiente
        :param ad_fila:
        :param linea_fila:
        :return:
        """
        try:
            codigo_concepto = self.model_fichero.obtener_codigo_concepto()
            codigo_en_ad_fila = [ad_fila[Columnas.AD.obtener_codigo_concepto]]
            encontrado = list(filter(lambda codigo: codigo == codigo_en_ad_fila, codigo_concepto))
            if not encontrado:
                self.detectar_error(TE.AD_CODIGO_CONCEPTO.obtener_descripcion,
                                    Columnas.AD.obtener_codigo_concepto, linea_fila)

        except AssertionError:
            self.detectar_error(TE.AD_CODIGO_CONCEPTO.obtener_descripcion,
                                Columnas.AD.obtener_codigo_concepto, linea_fila)
        except ValueError:
            self.detectar_error(TE.AD_CODIGO_CONCEPTO.obtener_descripcion,
                                Columnas.AD.obtener_codigo_concepto, linea_fila)
        except IndexError:
            self.detectar_error(TE.AD_CODIGO_CONCEPTO.obtener_descripcion,
                                Columnas.AD.obtener_codigo_concepto, linea_fila)

    def validar_numero_factura(self, ad_fila, linea_fila):
        """
        Función para validar que el numero de factura, este contenido en el archivo de transacciones
        :param ad_fila:
        :param linea_fila:
        :return:
        """
        try:
            lista_af = self.lista_af
            encontrado = list(filter(lambda campo_af: campo_af[Transacciones.AF.obtener_numero_factura] == ad_fila[
                Columnas.AD.obtener_numero_factura], lista_af))

            if not encontrado:
                self.detectar_error(TE.AD_NUMERO_FACTURA.obtener_descripcion,
                                    Columnas.AD.obtener_numero_factura, linea_fila)

        except AssertionError:
            self.detectar_error(TE.AD_NUMERO_FACTURA.obtener_descripcion,
                                Columnas.AD.obtener_numero_factura, linea_fila)
        except ValueError:
            self.detectar_error(TE.AD_NUMERO_FACTURA.obtener_descripcion,
                                Columnas.AD.obtener_numero_factura, linea_fila)
        except IndexError:
            self.detectar_error(TE.AD_NUMERO_FACTURA.obtener_descripcion,
                                Columnas.AD.obtener_numero_factura, linea_fila)

    def validar_valor_unitario_cantidad(self, ad_fila, linea_fila):
        """
        función para validar que si el valor unitario esta diligenciado la cantidad del producto tambien debe estarlo
        :param ad_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ad_fila[Columnas.AD.obtener_valor_unitario] == "" \
                    and ad_fila[Columnas.AD.obtener_cantidad_de_servicios] != "":
                self.detectar_error(TE.AD_VALOR_UNITARIO_CANTIDAD.obtener_descripcion,
                                    Columnas.AD.obtener_numero_factura, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AD_VALOR_UNITARIO_CANTIDAD.obtener_descripcion,
                                Columnas.AD.obtener_numero_factura, linea_fila)
        except ValueError:
            self.detectar_error(TE.AD_VALOR_UNITARIO_CANTIDAD.obtener_descripcion,
                                Columnas.AD.obtener_numero_factura, linea_fila)
        except IndexError:
            self.detectar_error(TE.AD_VALOR_UNITARIO_CANTIDAD.obtener_descripcion,
                                Columnas.AD.obtener_numero_factura, linea_fila)

    def validar_valor_total_segun_unitario(self, ad_fila, linea_fila):
        """
        función para validar que la multipliación del valor unitario por la cantidad sea igual al valor total
        :param ad_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ad_fila[Columnas.AD.obtener_valor_unitario] != ""\
                    and ad_fila[Columnas.AD.obtener_cantidad_de_servicios] != "":
                total_estimado = (float(ad_fila[Columnas.AD.obtener_valor_unitario]) * float(
                    ad_fila[Columnas.AD.obtener_cantidad_de_servicios]))
                total = Generico()._redondear_decimales(total_estimado)
                if not total == float(ad_fila[Columnas.AD.obtener_valor_total]):
                    self.detectar_error(TE.AD_VALOR_TOTAL.obtener_descripcion,
                                        Columnas.AD.obtener_valor_total, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AD_VALOR_TOTAL.obtener_descripcion,
                                Columnas.AD.obtener_valor_total, linea_fila)
        except ValueError:
            self.detectar_error(TE.AD_VALOR_TOTAL.obtener_descripcion,
                                Columnas.AD.obtener_valor_total, linea_fila)
        except IndexError:
            self.detectar_error(TE.AD_VALOR_TOTAL.obtener_descripcion,
                                Columnas.AD.obtener_valor_total, linea_fila)

# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.otros_servicios_enum import OtrosServiciosColumnasEnum as Columnas
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Aplicacion.Base.validacion_base import ValidacionBase
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Dominio.OtrosServicios.otros_servicios import ModeloOtrosServicios
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as Transacciones
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as USE
from Utilidades.Enumerados.Archivo.procedimientos_enum import ProcedimientosColumnasEnum as PE
from Utilidades.Enumerados.Archivo.consulta_enum import ConsultaColumnasEnum as CE


class ValidacionOtrosServicios(ValidacionBase):

    def __init__(self,lista_ac,lista_ap,lista_us,lista_af,cups,af,us):
        super().__init__()
        self.nombre_archivo = 'AT'
        self.model = ModeloOtrosServicios.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.cups_dic = cups
        self.lista_ap=lista_ap
        self.lista_ac=lista_ac
        self.lista_us = lista_us
        self.lista_af=lista_af
        self.dic_us=us
        self.dic_af=af




    def validar_tipo_identificacion(self, at_fila, linea_fila):
        """
        función que valida que el tipo de identificación del usuario sea valido

        :param at_fila:
        :param linea_fila:
        :return:
        """
        tipos_identificacion = self.model_fichero.obtener_tipo_id_usuario()
        tipo_id_en_at_fila = [at_fila[Columnas.AT.obtener_tipo_id]]
        encontrado = list(filter(lambda tipo_id: tipo_id == tipo_id_en_at_fila, tipos_identificacion))
        if not encontrado:
            self.detectar_error(TE.AT_TIPO_ID.obtener_descripcion,
                                Columnas.AT.obtener_tipo_id, linea_fila)

    def validar_numero_factura(self, at_fila, linea_fila):
        """
        Función para validar que el numero de factura, este contenido en el archivo de transacciones
        :param at_fila:
        :param linea_fila:
        :return:
        """
        numero_factura = at_fila[Columnas.AT.obtener_numero_factura]
        encontrado =  self.dic_af.get(numero_factura)
        if encontrado is None:
            self.detectar_error(TE.AT_NUMERO_FACTURA.obtener_descripcion,
                                Columnas.AT.obtener_numero_factura, linea_fila)

    def validar_tipo_numero_identificacion(self, at_fila, linea_fila):
        """
        función que valida que el tipo y numero de identificación en AT conincida con los de US
        :param at_fila:
        :param linea_fila:
        :return:
        """
        
        numero_id = at_fila[Columnas.AT.obtener_numero_id]
        encontrado =  self.dic_us.get(numero_id)
        
        if encontrado is None:
            self.detectar_error(TE.AT_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                posicion_columna=Columnas.AT.obtener_numero_id, linea=linea_fila)
        elif not encontrado[USE.US.obtener_tipo_id] == at_fila[Columnas.AT.obtener_tipo_id]:
            self.detectar_error(TE.AT_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                posicion_columna=Columnas.AT.obtener_numero_id, linea=linea_fila)

    def validar_tipo_servicio(self, at_fila, linea_fila):
        """
        función que valida que el tipo de servicio este entre los permitidos
        :param at_fila:
        :param linea_fila:
        :return:
        """

        tipos_servicios = self.model_fichero.obtener_tipo_servicio()
        tipo_servicio_at = [at_fila[Columnas.AT.obtener_tipo_servicio]]
        encontrado = list(filter(lambda tipo_servicio: tipo_servicio == tipo_servicio_at, tipos_servicios))
        if not encontrado:
            self.detectar_error(TE.AT_TIPO_SERVICIO.obtener_descripcion,
                                Columnas.AT.obtener_tipo_servicio, linea_fila)

    def validar_guion_numero_autorizacion(self, at_fila, linea_fila):
        """
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico().validar_guiones_numero_autorizacion(at_fila[Columnas.AT.obtener_numero_autorizacion],
                                                                  at_fila[Columnas.AT.obtener_codigo_servicio]):
                self.detectar_error(TE.AT_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                    Columnas.AT.obtener_numero_autorizacion,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AT_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                Columnas.AT.obtener_numero_autorizacion,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AT_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                Columnas.AT.obtener_numero_autorizacion,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AT_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                Columnas.AT.obtener_numero_autorizacion,
                                linea=linea_fila)

    def validar_nombre_servico(self, at_fila, linea_fila):
        """
        funcion que valida que el campo nombre del servicio siempre este diligenciado
        :param at_fila:
        :param linea_fila:
        :return:
        """
        if not at_fila[Columnas.AT.obtener_nombre_servicio]:
            self.detectar_error(TE.AT_NOMBRE_SERVICIO.obtener_descripcion,
                                Columnas.AT.obtener_nombre_servicio, linea_fila)

    def validar_cantidad_servicio(self, at_fila, linea_fila):
        """
        función que valida que la cantidad del servicio este diligenciada si el nombre o el codigo de este lo estan
        :param at_fila:
        :param linea_fila:
        :return:
        """

        if at_fila[Columnas.AT.obtener_nombre_servicio] or at_fila[Columnas.AT.obtener_codigo_servicio]:
            if not at_fila[Columnas.AT.obtener_numero_unidades]:
                self.detectar_error(TE.AT_CANTIDAD_SERVICIO.obtener_descripcion,
                                    Columnas.AT.obtener_numero_unidades, linea_fila)

    def validar_valor_unitario(self, at_fila, linea_fila):
        """
        función que valida que el valor unitario este diligenciado si la cantidad lo esta
        :param at_fila:
        :param linea_fila:
        :return:
        """

        if at_fila[Columnas.AT.obtener_numero_unidades]:
            if not at_fila[Columnas.AT.obtener_valor_unitario]:
                self.detectar_error(TE.AT_VALOR_UNITARIO.obtener_descripcion,
                                    Columnas.AT.obtener_valor_unitario, linea_fila)

    def validar_valor_total_segun_unitario(self, at_fila, linea_fila):
        """
        función para validar que la multipliación del valor unitario por la cantidad sea igual al valor total
        :param at_fila:
        :param linea_fila:
        :return:
        """

        if at_fila[Columnas.AT.obtener_valor_unitario] != "" and at_fila[Columnas.AT.obtener_numero_unidades] != "":
            total_estimado = Generico()._redondear_decimales((float(at_fila[Columnas.AT.obtener_valor_unitario]) * float(
                at_fila[Columnas.AT.obtener_numero_unidades])))
            if not total_estimado == float(at_fila[Columnas.AT.obtener_valor_total]):
                self.detectar_error(TE.AT_VALOR_TOTAL.obtener_descripcion,
                                    Columnas.AT.obtener_valor_total, linea_fila)

    def validar_tipo_servicio_codigo_cups(self,at_fila,linea_fila):
        """
        función que valida que el tipo de servicio este entre los permitidos
        :param at_fila:
        :param linea_fila:
        :return:
        """

        tipo_servicio_at=at_fila[Columnas.AT.obtener_tipo_servicio]

        if tipo_servicio_at == '2':
            if at_fila[Columnas.AT.obtener_codigo_servicio]!="":
                cod_servicio_atfila = at_fila[Columnas.AT.obtener_codigo_servicio]
                encontrado_cups =  self.cups_dic.get(cod_servicio_atfila)
                if encontrado_cups is not None:
                    if encontrado_cups[3]=='AT':
                        if not ('TRASLADO' in encontrado_cups[2]) and not ('TRANSPORTE' in encontrado_cups[2]):
                            self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_TRANSLADO.obtener_descripcion,
                                        Columnas.AT.obtener_codigo_servicio, linea_fila)
                    else:
                        self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_CUPS.obtener_descripcion,
                                        Columnas.AT.obtener_codigo_servicio, linea_fila)
                else:
                        self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_CUPS.obtener_descripcion,
                                        Columnas.AT.obtener_codigo_servicio, linea_fila)
            else:
                self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_VACIO.obtener_descripcion,Columnas.AT.obtener_codigo_servicio, linea_fila)

        if tipo_servicio_at == '3':
            if at_fila[Columnas.AT.obtener_codigo_servicio]!="":
                cod_servicio_atfila = at_fila[Columnas.AT.obtener_codigo_servicio]
                encontrado_cups =  self.cups_dic.get(cod_servicio_atfila)
                if encontrado_cups is not None:
                    if encontrado_cups[3]=='AT':
                        if  ('TRASLADO' in encontrado_cups[2]) or ('TRANSPORTE' in encontrado_cups[2]):
                            self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_ESTANCIA.obtener_descripcion,
                                        Columnas.AT.obtener_codigo_servicio, linea_fila)
                    else:
                        self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_CUPS.obtener_descripcion,
                                        Columnas.AT.obtener_codigo_servicio, linea_fila)
                else:
                        self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_CUPS.obtener_descripcion,
                                        Columnas.AT.obtener_codigo_servicio, linea_fila)
            else:
                self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_VACIO.obtener_descripcion,Columnas.AT.obtener_codigo_servicio, linea_fila)


        if tipo_servicio_at == '4':
            if at_fila[Columnas.AT.obtener_codigo_servicio]!="":
                lista_ac = self.lista_ac
                lista_ap = self.lista_ap
                cod_servicio_atfila = at_fila[Columnas.AT.obtener_codigo_servicio]
                encontrado_cups =  self.cups_dic.get(cod_servicio_atfila)
                if encontrado_cups is not None:
                    if encontrado_cups[3]=='AT':
                        encontrado_en_ap = list(
                            filter(lambda campo_ap: campo_ap[PE.AP.obtener_numero_id] == at_fila[Columnas.AT.obtener_numero_id], lista_ap))

                        encontrado_en_ac = list(
                            filter(lambda campo_ac: campo_ac[CE.AC.obtener_numero_id] == at_fila[Columnas.AT.obtener_numero_id], lista_ac))

                        if  encontrado_en_ac!=[]:
                            ac=False
                            for encontrado in encontrado_en_ac:
                                if encontrado[CE.AC.obtener_codigo_consulta] == at_fila[Columnas.AT.obtener_codigo_servicio]:
                                    ac=True
                            if ac:
                                self.detectar_error(TE.AT_CODIGO_SERVICIO_EN_AP_AC.obtener_descripcion,
                                             posicion_columna=Columnas.AT.obtener_codigo_servicio, linea=linea_fila,archivo="AC")

                        if  encontrado_en_ap!=[]:
                            ap=False
                            for encontrado in encontrado_en_ap:
                                if encontrado[PE.AP.obtener_codigo_procedimiento] == at_fila[Columnas.AT.obtener_codigo_servicio]:
                                    ap=True
                            if ap:
                                self.detectar_error(TE.AT_CODIGO_SERVICIO_EN_AP_AC.obtener_descripcion,
                                            posicion_columna=Columnas.AT.obtener_codigo_servicio, linea=linea_fila,archivo="AP")

                    else:
                        self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_CUPS.obtener_descripcion,
                                        Columnas.AT.obtener_codigo_servicio, linea_fila)
                else:
                        self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_CUPS.obtener_descripcion,
                                        Columnas.AT.obtener_codigo_servicio, linea_fila)
            else:
                self.detectar_error(TE.AT_CODIGO_SERVICIO_NO_VACIO.obtener_descripcion,Columnas.AT.obtener_codigo_servicio, linea_fila)



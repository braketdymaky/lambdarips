# -*- coding: utf-8 -*-
from datetime import date

from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.Procedimientos.procedimientos import ModeloProcedimiento
from Utilidades.Enumerados.Archivo.procedimientos_enum import ProcedimientosColumnasEnum as Columnas
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as TSE
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as UE
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico


class ValidacionProcedimiento(ValidacionBase):

    def __init__(self,lista_af,lista_us,cups,af,us,cie10):
        super().__init__()
        self.nombre_archivo = 'AP'
        self.model = ModeloProcedimiento.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.codigo_habilitacion = ''
        self.cie10 = self.model_fichero.obtener_cie10()
        self.cups=self.model_fichero.obtener_cups()
        self.fichero_tipo_id = self.model_fichero.obtener_tipo_id_usuario()
        self.lista_af = lista_af
        self.lista_us = lista_us
        self.cups_dic = cups
        self.dic_us=us
        self.dic_af=af
        self.cie10_dic=cie10

    def validar_codigo_habilitacion(self, ap_fila, linea_fila):
        """
        Función para validar que el código de habilitación, este contenido en todos los registros de CT
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        if not ap_fila[Columnas.AP.obtener_codigo_prestador] == self.codigo_habilitacion:
            self.detectar_error(TE.AP_CODIGO_HABILITACION.obtener_descripcion,
                                Columnas.AP.obtener_codigo_prestador, linea_fila)


    def validar_numero_factura(self, ap_fila, linea_fila):
        """
        Función para validar que el numero de factura, este contenido en el archivo de transacciones
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        # opt_aariza
        numero_factura = ap_fila[Columnas.AP.obtener_numero_factura]
        encontrado =  self.dic_af.get(numero_factura)
        if encontrado is None:
            self.detectar_error(TE.AP_FACTURA_NO_ENCONTRADA.obtener_descripcion, Columnas.AP.obtener_numero_factura,
                                linea_fila)

    def validar_tipo_id(self, ap_fila, linea_fila):
        tipo_id = [ap_fila[Columnas.AP.obtener_tipo_id]]
        fichero_tipo_id = self.fichero_tipo_id
        if tipo_id not in fichero_tipo_id:
            self.detectar_error(TE.AP_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                Columnas.AP.obtener_tipo_id, linea_fila)

    def validar_tipo_numero_identificacion(self, ap_fila, linea_fila):
        """
        Función para validar que el tipo y numero de identificación, coincida con el archivo de usuarios
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        numero_id = ap_fila[Columnas.AP.obtener_numero_id]
        encontrado =  self.dic_us.get(numero_id)
        

        if encontrado is None:
            self.detectar_error(TE.AP_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, Columnas.AP.obtener_numero_id,
                                linea_fila)
        elif not encontrado[UE.US.obtener_tipo_id] == ap_fila[Columnas.AP.obtener_tipo_id]:
            self.detectar_error(TE.AP_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, Columnas.AP.obtener_numero_id,
                                linea_fila)

    def validar_fecha_procedimiento(self, ap_fila, linea_fila):
        if not Generico().validar_fecha_menor_actual(ap_fila[Columnas.AP.obtener_fecha_procedimiento]):
            self.detectar_error(TE.AP_FECHA_PROCEDIMIENTO.obtener_descripcion, Columnas.AP.obtener_fecha_procedimiento,
                                linea_fila)

    def validar_codigo_procedimiento(self, ap_fila, linea_fila):
        #apt aariza
        cod_procedimiento_apfila = ap_fila[Columnas.AP.obtener_codigo_procedimiento]
        encontrado_cups =  self.cups_dic.get(cod_procedimiento_apfila)
        if not encontrado_cups:
            self.detectar_error(TE.AP_CUPS_INVALIDO.obtener_descripcion, Columnas.AP.obtener_codigo_procedimiento,
                                linea_fila)

    def validar_ambito_realizacion_procedimiento(self, ap_fila, linea_fila):
        ambito = [ap_fila[Columnas.AP.obtener_ambito]]
        fichero_ambito = self.model_fichero.obtener_ambito_procedimiento()
        if ambito not in fichero_ambito and ambito!=[""]:
            self.detectar_error(TE.AP_AMBITO_INVALIDO.obtener_descripcion, Columnas.AP.obtener_ambito,
                                linea_fila)

    def validar_finalidad_procedimiento(self, ap_fila, linea_fila):
        ambito = [ap_fila[Columnas.AP.obtener_finalidad_procedimiento]]
        fichero_finalidad_prodecimiento = self.model_fichero.obtener_finalidad_procedimiento()
        if ambito not in fichero_finalidad_prodecimiento:
            self.detectar_error(TE.AP_FINALIDAD_PROCEDIMIENTO.obtener_descripcion,
                                Columnas.AP.obtener_finalidad_procedimiento, linea_fila)

    def validar_personal_atiende(self, ap_fila, linea_fila):
        personal_atiende = [ap_fila[Columnas.AP.obtener_personal_que_atendio]]
        fichero_personal_atiende = self.model_fichero.obtener_personal_atiende()
        if personal_atiende not in fichero_personal_atiende and personal_atiende != [""]:
            self.detectar_error(TE.AP_PERSONAL_ATIENDE.obtener_descripcion, Columnas.AP.obtener_personal_que_atendio,
                                linea_fila)

    def validar_forma_quirurgico(self, ap_fila, linea_fila):
        forma_quirurgico = [ap_fila[Columnas.AP.obtener_realizacion_act_quirurgico]]
        fichero_forma_quirurgico = self.model_fichero.obtener_forma_acto_quirurjico()
        if forma_quirurgico not in fichero_forma_quirurgico and forma_quirurgico != [""]:
            self.detectar_error(TE.AP_FORMA_QUIRURGICO.obtener_descripcion,
                                Columnas.AP.obtener_realizacion_act_quirurgico, linea_fila)

    def validar_diagnostico_principal(self, ap_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        if ap_fila[Columnas.AP.obtener_diagnostico_principal] != "":
            diagnostico_apfila = ap_fila[Columnas.AP.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_apfila)
            if encontrado is not None:
                self.detectar_error(TE.AP_DIAGNOSTICO_NO_ENCONTRADO.obtener_descripcion,
                                    Columnas.AP.obtener_diagnostico_principal,
                                    linea=linea_fila)

    def validar_diagnostico_principal_sexo(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ap_fila:
        :param linea_fila:
        :return:
        """


        if ap_fila[Columnas.AP.obtener_diagnostico_principal] != "":
            diagnostico_apfila = ap_fila[Columnas.AP.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_apfila)
            if encontrado is not None:
                if not encontrado[1] == 'A':
                    numero_id = ap_fila[Columnas.AP.obtener_numero_id]
                    encontrado2 =  self.dic_us.get(numero_id)

                    if encontrado2 is not None:
                        if not Generico().validar_sexo(encontrado2[UE.US.obtener_sexo],encontrado[1]):
                            self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion,
                                                Columnas.AP.obtener_diagnostico_principal,
                                                linea=linea_fila)

    def validar_diagnostico_principal_edad(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        if ap_fila[Columnas.AP.obtener_diagnostico_principal] != "":
            diagnostico_ahfila = ap_fila[Columnas.AP.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)
            if encontrado is not None:
                numero_id = ap_fila[Columnas.AP.obtener_numero_id]
                encontrado2 =  self.dic_us.get(numero_id)
                if encontrado2 is None:
                    self.detectar_error(TE.AP_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, Columnas.AP.obtener_numero_id,
                                        linea=linea_fila)
                else:
                    if not Generico().validar_edad_con_unidad_de_medida(encontrado2[UE.US.obtener_edad],
                                                                        encontrado2[UE.US.obtener_medida_de_edad],
                                                                        encontrado[2], encontrado[3]):
                        self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_diagnostico_principal,
                                            linea=linea_fila)

    def validar_diagnostico_rel_1_sexo(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        try:
            if ap_fila[Columnas.AP.obtener_diagnostico_relacionado_1] != "":
                diagnostico_ahfila = ap_fila[Columnas.AP.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        numero_id = ap_fila[Columnas.AP.obtener_numero_id]
                        encontrado2 =  self.dic_us.get(numero_id)

                        if encontrado2 is not None:
                            if not Generico().validar_sexo(encontrado2[UE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion,
                                                    Columnas.AP.obtener_diagnostico_relacionado_1,
                                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion, Columnas.AP.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion, Columnas.AP.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion, Columnas.AP.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)


    def validar_diagnostico_rel_1_edad(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        try:
            if ap_fila[Columnas.AP.obtener_diagnostico_relacionado_1] != "":

                diagnostico_ahfila = ap_fila[Columnas.AP.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    numero_id = ap_fila[Columnas.AP.obtener_numero_id]
                    encontrado2 =  self.dic_us.get(numero_id)

                    if encontrado2 is not None:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[UE.US.obtener_edad],
                                                                            encontrado2[
                                                                                UE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion,
                                                Columnas.AP.obtener_diagnostico_relacionado_1,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)

    def validar_complicacion_sexo(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ap_fila:
        :param linea_fila:
        :return:
        """


        try:
            if ap_fila[Columnas.AP.obtener_complicacion] != "":
                
                diagnostico_ahfila = ap_fila[Columnas.AP.obtener_complicacion]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                
                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        numero_id = ap_fila[Columnas.AP.obtener_numero_id]
                        encontrado2 =  self.dic_us.get(numero_id)

                        if encontrado2 is not None:
                            if not Generico().validar_sexo(encontrado2[UE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion,
                                                    Columnas.AP.obtener_complicacion,
                                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion, Columnas.AP.obtener_complicacion,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion, Columnas.AP.obtener_complicacion,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AP_SEXO_INCORRECTO.obtener_descripcion, Columnas.AP.obtener_complicacion,
                                linea=linea_fila)


    def validar_complicacion_edad(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        try:
            if ap_fila[Columnas.AP.obtener_complicacion] != "":

                diagnostico_ahfila = ap_fila[Columnas.AP.obtener_complicacion]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    numero_id = ap_fila[Columnas.AP.obtener_numero_id]
                    encontrado2 =  self.dic_us.get(numero_id)

                    if encontrado2 is not None:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[UE.US.obtener_edad],
                                                                            encontrado2[UE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion,
                                                Columnas.AP.obtener_complicacion,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_complicacion,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_complicacion,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AP_EDAD_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_complicacion,
                                linea=linea_fila)

    def validar_codigo_quirurgico(self, ap_fila, linea_fila):
        """
        Se valida que si el código de procedimiento CUPS es quirúrgico,
        el campo código de diagnóstico principal no sea nulo
        y encuentre dentro de la tabla de la (cie10)
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        #apt aariza
        cod_procedimiento_apfila = ap_fila[Columnas.AP.obtener_codigo_procedimiento]
        encontrado_cups =  self.cups_dic.get(cod_procedimiento_apfila)

        if encontrado_cups is not None:
            if '00' in encontrado_cups[1]:
                if ap_fila[Columnas.AP.obtener_diagnostico_principal] !="":
                    encontrado = any(ap_fila[Columnas.AP.obtener_diagnostico_principal] in x for x in self.cie10)
                    if not encontrado:
                        self.detectar_error(TE.AP_CODIGO_QUIRURGICO.obtener_descripcion,
                                            Columnas.AP.obtener_codigo_procedimiento,
                                             linea=linea_fila)
                else:
                    self.detectar_error(TE.AP_CODIGO_QUIRURGICO.obtener_descripcion,
                                            Columnas.AP.obtener_codigo_procedimiento,
                                             linea=linea_fila)


    def validar_diagnostico_rel1(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        if ap_fila[Columnas.AP.obtener_diagnostico_relacionado_1] != "":
            #apt aariza
            cod_procedimiento_apfila = ap_fila[Columnas.AP.obtener_codigo_procedimiento]
            encontrado_cups =  self.cups_dic.get(cod_procedimiento_apfila)

            if encontrado_cups is not None:
                if '00' in encontrado_cups[1]:

                    encontrado = any(ap_fila[Columnas.AP.obtener_diagnostico_relacionado_1] in x for x in self.cie10)

                    if not encontrado:
                        self.detectar_error(TE.AP_DIAGNOSTICO_REL1_NO_ENCONTRADO.obtener_descripcion,
                                            Columnas.AP.obtener_diagnostico_relacionado_1,
                                            linea=linea_fila)
                else:
                    self.detectar_error(TE.AP_DIAGNOSTICO_REL1_NO_ENCONTRADO.obtener_descripcion,
                                            Columnas.AP.obtener_diagnostico_relacionado_1,
                                            linea=linea_fila)

    def validar_complicacion(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param ap_fila:
        :param linea_fila:
        :return:
        """

        if ap_fila[Columnas.AP.obtener_complicacion] != "":
            #apt aariza
            cod_procedimiento_apfila = ap_fila[Columnas.AP.obtener_codigo_procedimiento]
            encontrado_cups =  self.cups_dic.get(cod_procedimiento_apfila)

            if encontrado_cups is not None:
                if '00' in encontrado_cups[1]:
                    encontrado = any(ap_fila[Columnas.AP.obtener_complicacion] in x for x in self.cie10)
                    if not encontrado:
                        self.detectar_error(TE.AP_COMPLICACION_NO_ENCCONTRADO.obtener_descripcion,
                                            Columnas.AP.obtener_complicacion,
                                            linea=linea_fila)
                else:
                    self.detectar_error(TE.AP_COMPLICACION_NO_ENCCONTRADO.obtener_descripcion,
                                        Columnas.AP.obtener_complicacion,
                                        linea=linea_fila)
            else:
                self.detectar_error(TE.AP_COMPLICACION_NO_ENCCONTRADO.obtener_descripcion,
                                    Columnas.AP.obtener_complicacion,
                                    linea=linea_fila)

    def validar_forma_realizacion(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        if ap_fila[Columnas.AP.obtener_realizacion_act_quirurgico] != "":
            forma_quirurgico = self.model_fichero.obtener_forma_acto_quirurjico()
            #apt aariza
            cod_procedimiento_apfila = ap_fila[Columnas.AP.obtener_codigo_procedimiento]
            encontrado_cups =  self.cups_dic.get(cod_procedimiento_apfila)
            if [ap_fila[Columnas.AP.obtener_realizacion_act_quirurgico]] not in forma_quirurgico:
                self.detectar_error(TE.AP_FORMA_QUIRURGICO.obtener_descripcion,
                                                Columnas.AP.obtener_realizacion_act_quirurgico, linea_fila)
            
            elif encontrado_cups is not None:
                if '00' not in encontrado_cups[1]:
                    self.detectar_error(TE.AP_FORMA_QUIRURGICO.obtener_descripcion,
                                                Columnas.AP.obtener_realizacion_act_quirurgico, linea_fila)
            

    def validar_no_quirurgico(self, ap_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        if ap_fila[Columnas.AP.obtener_codigo_procedimiento]!="":
            #apt aariza
            cod_procedimiento_apfila = ap_fila[Columnas.AP.obtener_codigo_procedimiento]
            encontrado_cups =  self.cups_dic.get(cod_procedimiento_apfila)

            if encontrado_cups is not None:
                if '01' in encontrado_cups[1]:
                    if ap_fila[Columnas.AP.obtener_complicacion]!="" or ap_fila[
                        Columnas.AP.obtener_diagnostico_relacionado_1]!="" or ap_fila[
                        Columnas.AP.obtener_diagnostico_principal]!="" or ap_fila[Columnas.AP.obtener_realizacion_act_quirurgico]!="":
                        self.detectar_error(TE.AP_NO_QUIRURGICO_CAMPO.obtener_descripcion,
                                            Columnas.AP.obtener_codigo_procedimiento,
                                            linea=linea_fila)


    def validar_guion_numero_autorizacion(self, ap_fila, linea_fila):
        """
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        try:
            guiones = Generico().validar_guiones_numero_autorizacion_ap(ap_fila[Columnas.AP.obtener_numero_autorizacion],ap_fila[Columnas.AP.obtener_codigo_procedimiento])
            if str(guiones) == '2':
                self.detectar_error(TE.AP_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_numero_autorizacion,
                                                linea=linea_fila)

            if str(guiones) == '3':
                self.detectar_error(TE.AP_NUMERO_AUTORIZACION_VACIA.obtener_descripcion, Columnas.AP.obtener_numero_autorizacion,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AP_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion, Columnas.AP.obtener_numero_autorizacion,
                                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AP_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,Columnas.AP.obtener_numero_autorizacion,
                                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AP_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,Columnas.AP.obtener_numero_autorizacion,
                                                linea=linea_fila)

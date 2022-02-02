# -*- coding: utf-8 -*-
from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.Urgencias.urgencias import ModeloUrgencias
from Utilidades.Enumerados.Archivo.urgencias_enum import UrgenciasColumnasEnum as UE
from Utilidades.Enumerados.Archivo.hospitalizaciones_enum import HospitalizacionesColumnasEnum as HE
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as USE
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as TSE
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE


class ValidacionUrgencias(ValidacionBase):

    def __init__(self,lista_af,lista_ah,lista_us,cie10,af,us):
        super().__init__()
        self.nombre_archivo = 'AU'
        self.model = ModeloUrgencias.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.lista_af = lista_af
        self.lista_ah = lista_ah
        self.lista_us = lista_us
        self.cie10_dic= cie10
        self.dic_us=us
        self.dic_af=af



    def validar_numero_factura(self, au_fila, linea_fila):
        """
        Función para validar que el numero de factura, este contenido en el archivo de transacciones
        :param au_fila:
        :param linea_fila:
        :return:
        """
        numero_factura = au_fila[UE.AU.obtener_numero_factura]
        encontrado =  self.dic_af.get(numero_factura)
        if encontrado is None:
            self.detectar_error(TE.AU_FACTURA_NO_ENCONTRADA.obtener_descripcion, UE.AU.obtener_numero_factura,
                                linea=linea_fila)

    def validar_tipo_identificacion(self, au_fila, linea_fila):
        """
        Función para validar que el tipo de identificación, este contenido en el rango de valores permitidos
        :param au_fila:
        :param linea_fila:
        :return:
        """
        valores_permitidos = self.model_fichero.obtener_tipo_id_usuario()

        encontrado = [au_fila[UE.AU.obtener_tipo_id]] in valores_permitidos

        if not encontrado:
            self.detectar_error(TE.AU_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, UE.AU.obtener_tipo_id,
                                linea=linea_fila)

    def validar_tipo_numero_identificacion(self, au_fila, linea_fila):
        """
        Función para validar que el tipo y numero de identificación, coincida con el archivo de usuarios
        :param au_fila:
        :param linea_fila:
        :return:
        """
        numero_id = au_fila[UE.AU.obtener_numero_id]
        encontrado =  self.dic_us.get(numero_id)
        
        if encontrado is None:
            self.detectar_error(TE.AU_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, UE.AU.obtener_numero_id,
                                    linea=linea_fila)
        elif not encontrado[USE.US.obtener_tipo_id] == au_fila[UE.AU.obtener_tipo_id]:
            self.detectar_error(TE.AU_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, UE.AU.obtener_numero_id,
                                    linea=linea_fila)

    def validar_guion_numero_autorizacion(self, au_fila, linea_fila):
        """
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        try:
            
            if not Generico().validar_guiones_numero_autorizacion(au_fila[UE.AU.obtener_numero_autorizacion],''):
                self.detectar_error(TE.AU_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion, UE.AU.obtener_numero_autorizacion,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion, UE.AU.obtener_numero_autorizacion,
                                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,UE.AU.obtener_numero_autorizacion,
                                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,UE.AU.obtener_numero_autorizacion,
                                                linea=linea_fila)        

    def validar_fecha_ingreso_usuario_a_observacion(self, au_fila, linea_fila):
        """
        Función para validar que la fecha de ingreso no sea mayor a la actual
        :param au_fila:
        :param linea_fila:
        :return:
        """
        
        if not Generico().validar_fecha_menor_actual(au_fila[UE.AU.obtener_fecha_ingreso]):
            self.detectar_error(TE.AU_FECHA_INGRESO_INCORRECTA.obtener_descripcion, UE.AU.obtener_fecha_ingreso,
                                linea=linea_fila)

    def validar_causa_externa(self, am_fila, linea_fila):
        """
        Función para validar que la causa externa, este contenido en el rango de valores permitidos
        :param am_fila:
        :param linea_fila:
        :return:
        """
        valores_permitidos = self.model_fichero.obtener_causa_externa()

        encontrado = [am_fila[UE.AU.obtener_causa_externa]] in valores_permitidos

        if not encontrado:
            self.detectar_error(TE.AU_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion, UE.AU.obtener_causa_externa,
                                linea=linea_fila)

    def validar_destino_usuario_salida_observacion(self, au_fila, linea_fila):
        """
        Función para validar que el destino del usuario a la salida de observación se encuentre dentro
        de los valores permitidos.
        :param au_fila:
        :param linea_fila:
        :return:
        """

        valores_permitidos = self.model_fichero.obtener_destino_usuario()

        encontrado = [au_fila[UE.AU.obtener_destino_usuario]] in valores_permitidos

        if not encontrado:
            self.detectar_error(TE.AU_DESTINO_SALIDA_OBSERVACION_INCORRECTO.obtener_descripcion,
                                UE.AU.obtener_destino_usuario,
                                linea=linea_fila)

    def validar_estado_salida(self, au_fila, linea_fila):
        """
        Función para validar que el estado se encuentre dentro de los valores permitidos.
        :param au_fila:
        :param linea_fila:
        :return:
        """

        valores_permitidos = self.model_fichero.obtener_estado_salida()

        encontrado = [au_fila[UE.AU.obtener_hdestino_usuario]] in valores_permitidos

        if not encontrado:
            self.detectar_error(TE.AU_ESTADO_SALIDA_INCORRECTA.obtener_descripcion, UE.AU.obtener_hdestino_usuario,
                                linea=linea_fila)

    def validar_causa_basica_de_muerte(self, au_fila, linea_fila):
        """
        Función para validar que la causa básica de muerte no sea nulo,
        el estado igual a 2 y que se encuentre dentro de la tabla cie10.
        :param au_fila:
        :param linea_fila:
        :return:
        """

        valores_permitidos = self.model_fichero.obtener_eapb()
        if au_fila[UE.AU.obtener_hdestino_usuario] == '2':
            if au_fila[UE.AU.obtener_causa_muerte] == '':
                self.detectar_error(TE.AU_CAUSA_BASICA_MUERTE_VACIO.obtener_descripcion, UE.AU.obtener_causa_muerte,
                                    linea=linea_fila)
            else:
                encontrado = [au_fila[UE.AU.obtener_hdestino_usuario]] in valores_permitidos
                if not encontrado:
                    self.detectar_error(TE.AU_CAUSA_BASICA_MUERTE_NO_ENCONTRADA.obtener_descripcion,
                                         UE.AU.obtener_causa_muerte, linea=linea_fila)

    def validar_causa_basica_de_muerte_2(self, au_fila, linea_fila):
        """
        Función para validar que si el campo estado a la salida es 1=Vivo,
        la variable Causa básica de muerte en urgencias debe estar vacía
        :param au_fila:
        :param linea_fila:
        :return:
        """
        if au_fila[UE.AU.obtener_causa_muerte] != '':
            if au_fila[UE.AU.obtener_hdestino_usuario] == '1':
                if au_fila[UE.AU.obtener_causa_muerte]:
                    self.detectar_error(TE.AU_CAUSA_BASICA_MUERTE_INCORRECTA.obtener_descripcion,
                                        UE.AU.obtener_causa_muerte, linea=linea_fila)

    def validar_fecha_salida_usuario_a_observacion(self, au_fila, linea_fila):
        """
        Función para validar que la fecha de salida no sea mayor a la actual
        :param au_fila:
        :param linea_fila:
        :return:
        """

        if not Generico().validar_fecha_menor_actual(au_fila[UE.AU.obtener_fecha_salida]):
            self.detectar_error(TE.AU_FECHA_SALIDA_INCORRECTA.obtener_descripcion, UE.AU.obtener_fecha_salida,
                                linea=linea_fila)

    def validar_fecha_ingreso_menor_salida_usuario_a_observacion(self, au_fila, linea_fila):
        """
        Función para validar que la fecha de ingreso sea anterior o igual a la fecha de salida
        :param au_fila:
        :param linea_fila:
        :return:
        """
        
        if not Generico().validar_fecha_menor_fecha(au_fila[UE.AU.obtener_fecha_ingreso],
                                                  au_fila[UE.AU.obtener_fecha_salida]):
            self.detectar_error(TE.AU_FECHA_INGRESO_SALIDA_INCORRECTO.obtener_descripcion, UE.AU.obtener_fecha_salida,
                                linea=linea_fila)

    def validar_hora_ingreso_menor_salida_usuario_a_observacion(self, au_fila, linea_fila):
        """
        Función para validar que si la fecha de ingreso es igual a la fecha de salida,
        la hora de ingreso debe ser anterior a la hora de salida.
        :param au_fila:
        :param linea_fila:
        :return:
        """

        if Generico().validar_fecha_igual_fecha(au_fila[UE.AU.obtener_fecha_ingreso],
                                              au_fila[UE.AU.obtener_fecha_salida]):
            if not Generico.validar_hora_menor_fecha(au_fila[UE.AU.obtener_hora_ingreso],
                                                     au_fila[UE.AU.obtener_hora_salida]):
                self.detectar_error(TE.AU_HORA_INGRESO_INCORRECTA.obtener_descripcion, UE.AU.obtener_hora_ingreso,
                                    linea=linea_fila)

    def validar_destino_salida_usuario(self, au_fila, linea_fila):
        """
        Función para validar que Si el destino del usuario a la salida es hospitalización(3),
        deberá aparecer un registro en el archivo de hospitalización.
        :param au_fila:
        :param linea_fila:
        :return:
        """

        lista_ah = self.lista_ah
        encontrado = list(
            filter(lambda campo_af: campo_af[HE.AH.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                   lista_ah))

        if au_fila[UE.AU.obtener_destino_usuario] == '2':
            if not encontrado:
                self.detectar_error(TE.AU_DESTINO_SALIDA_OBSERVACION_NO_ENCONTRADO.obtener_descripcion,
                                    UE.AU.obtener_destino_usuario, linea=linea_fila)

    def validar_diagnostico_principal_de_salida(self, au_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)
            if encontrado is None:
                self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA_NO_ENCCONTRADO.obtener_descripcion,
                                    UE.AU.obtener_diagnostico_principal,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_salida_sexo(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)
            if encontrado is not None:
                if not encontrado[1] == 'A':
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion,
                                                UE.AU.obtener_diagnostico_principal,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)


    def validar_diagnostico_principal_de_salida_edad(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param au_fila:
        :param linea_fila:
        :return:
        """

        try:
            diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)
            if encontrado is not None:
                lista_us = self.lista_us
                encontrado2 = list(
                    filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                           lista_us))

                if encontrado2:
                    if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                        encontrado2[0][USE.US.obtener_medida_de_edad],
                                                                        encontrado[2], encontrado[3]):
                        self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion,
                                            UE.AU.obtener_diagnostico_principal,
                                            linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_principal,
                                linea=linea_fila)
            

    def validar_diagnostico_principal_de_salida_rel_1(self, au_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_1] != '':
                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is None:
                    self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA1_NO_ENCCONTRADO.obtener_descripcion,
                                        UE.AU.obtener_diagnostico_relacionado_1,
                                        linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA1_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA1_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA1_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_salida_rel_1_sexo(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_1] != '':

                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    if not encontrado[0][1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(
                                lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                                lista_us))

                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion,
                                                    UE.AU.obtener_diagnostico_relacionado_1,
                                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_salida_rel_1_edad(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_1] != '':
                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion,
                                                UE.AU.obtener_diagnostico_relacionado_1,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)


    def validar_diagnostico_principal_de_salida_rel_2(self, au_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_2] != '':
                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is None:
                    self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA2_NO_ENCCONTRADO.obtener_descripcion,
                                        UE.AU.obtener_diagnostico_relacionado_2,
                                        linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA2_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA2_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA2_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_salida_rel_2_sexo(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_2] != '':

                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(
                                lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                                lista_us))

                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion,
                                                    UE.AU.obtener_diagnostico_relacionado_2,
                                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_salida_rel_2_edad(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param au_fila:
        :param linea_fila:
        :return:
        """

        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_2] != '':
                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion,
                                                UE.AU.obtener_diagnostico_relacionado_2,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_salida_rel_3(self, au_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_3] != '':
                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is None:
                    self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA3_NO_ENCCONTRADO.obtener_descripcion,
                                        UE.AU.obtener_diagnostico_relacionado_3,
                                        linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA3_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA3_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_DIAGNOSTICO_SALIDA3_NO_ENCCONTRADO.obtener_descripcion,
                                UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_salida_rel_3_sexo(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_3] != '':

                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(
                                lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                                lista_us))

                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion,
                                                    UE.AU.obtener_diagnostico_relacionado_3,
                                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_SEXO_INCORRECTO.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_salida_rel_3_edad(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[UE.AU.obtener_diagnostico_relacionado_3] != '':
                diagnostico_ahfila = au_fila[UE.AU.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion,
                                                UE.AU.obtener_diagnostico_relacionado_3,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AU_EDAD_INCORRECTA.obtener_descripcion, UE.AU.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)

    def validar_causa_muerte_sexo(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param au_fila:
        :param linea_fila:
        :return:
        """
        if au_fila[UE.AU.obtener_causa_muerte] != '':
            diagnostico_ahfila = au_fila[UE.AU.obtener_causa_muerte]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)
    
            if encontrado is None:
                self.detectar_error(TE.AU_SEXO_INCORRECTO_CM.obtener_descripcion, UE.AU.obtener_causa_muerte,
                                    linea=linea_fila)
            else:
                if not encontrado[1] == 'A':
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                               lista_us))
    
                    if encontrado2:
                        if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo],encontrado[1]):
                            self.detectar_error(TE.AU_SEXO_INCORRECTO_CM.obtener_descripcion, UE.AU.obtener_causa_muerte,
                                                linea=linea_fila)

    def validar_causa_muerte_edad(self, au_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param au_fila:
        :param linea_fila:
        :return:
        """
        if au_fila[UE.AU.obtener_causa_muerte] != '':
    
            diagnostico_ahfila = au_fila[UE.AU.obtener_causa_muerte]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)
    
            if encontrado is not None:
                lista_us = self.lista_us
                encontrado2 = list(
                    filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == au_fila[UE.AU.obtener_numero_id],
                           lista_us))
    
                if encontrado2:
                    if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                        encontrado2[0][USE.US.obtener_medida_de_edad],
                                                                        encontrado[2], encontrado[3]):
                        self.detectar_error(TE.AU_EDAD_INCORRECTA_CM.obtener_descripcion, UE.AU.obtener_causa_muerte,
                                            linea=linea_fila)

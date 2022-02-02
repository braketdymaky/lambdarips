# -*- coding: utf-8 -*-
from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.Hospitalizaciones.hospitalizaciones import ModeloHospitalizacion
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as USE
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as TSE
from Utilidades.Enumerados.Archivo.hospitalizaciones_enum import HospitalizacionesColumnasEnum as HE
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Utilidades.Enumerados.Archivo.urgencias_enum import UrgenciasColumnasEnum as UAE
from Utilidades.Enumerados.Archivo.consulta_enum import ConsultaColumnasEnum as ACE
from Utilidades.Enumerados.Archivo.procedimientos_enum import ProcedimientosColumnasEnum as APE


class ValidacionHospitalizacion(ValidacionBase):

    def __init__(self,listas,cie10,af,us,codigo_prestador):
        super().__init__()
        self.nombre_archivo = 'AH'
        self.model = ModeloHospitalizacion.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.lista_af = listas['AF']
        self.lista_ap = listas['AP']
        self.lista_us = listas['US']
        self.lista_au = listas['AU']
        self.lista_ac = listas['AC']
        self.cie10_dic= cie10
        self.dic_af=af
        self.dic_us=us
        self.fichero_eapb = self.model_fichero.obtener_eapb()
        self.fichero_eapb_aux=self.model_fichero.obtener_eapb_aux()
        self.dic_eapb = self.diccionario_eapb(self.fichero_eapb)
        self.codigo_prestador=codigo_prestador

    def diccionario_eapb(self,lista_eapb):
        dic_eapb={}
        for eapb in lista_eapb:
            codigo_eapb=eapb[1]
            dic_eapb[codigo_eapb]=eapb
        return dic_eapb

    def diccionario_eapb_aux(self,lista_eapb):
        dic_eapb={}
        for eapb in lista_eapb:
            nit=eapb[1]
            inidice=nit.index('-')
            codigo_eapb=nit[0:indice]
            dic_eapb[codigo_eapb]=eapb
        return dic_eapb

    def validar_numero_factura(self, ah_fila, linea_fila):
        """
        Función para validar que el numero de factura, este contenido en el archivo de transacciones
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        numero_factura = ah_fila[HE.AH.obtener_numero_factura]
        encontrado =  self.dic_af.get(numero_factura)
        if encontrado is None:
            self.detectar_error(TE.AH_FACTURA_NO_ENCONTRADA.obtener_descripcion, HE.AH.obtener_numero_factura,
                                    linea=linea_fila)
       

    def validar_tipo_identificacion(self, ah_fila, linea_fila):
        """
        Función para validar que el tipo de identificación, este contenido en el rango de valores permitidos
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        valores_permitidos = self.model_fichero.obtener_tipo_id_usuario()
        encontrado = [ah_fila[HE.AH.obtener_tipo_id]] in valores_permitidos
        if not encontrado:
            self.detectar_error(TE.AH_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, HE.AH.obtener_tipo_id,
                                linea=linea_fila)

    def validar_tipo_numero_identificacion(self, ah_fila, linea_fila):
        """
        Función para validar que el tipo y numero de identificación, coincida con el archivo de usuarios
        :param ah_fila:
        :param linea_fila:
        :return:
        """

        numero_id = ah_fila[HE.AH.obtener_numero_id]
        encontrado =  self.dic_us.get(numero_id)
        
        if encontrado is None:
            self.detectar_error(TE.AH_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, HE.AH.obtener_numero_id,
                                    linea=linea_fila)

        elif not encontrado[USE.US.obtener_tipo_id] == ah_fila[HE.AH.obtener_tipo_id]:
            self.detectar_error(TE.AH_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, HE.AH.obtener_numero_id,
                                    linea=linea_fila)

        

    def validar_guion_numero_autorizacion(self, ah_fila, linea_fila):
        """
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico().validar_guiones_numero_autorizacion(ah_fila[HE.AH.obtener_numero_autorizacion], ''):
                self.detectar_error(TE.AH_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                    HE.AH.obtener_numero_autorizacion,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_numero_autorizacion,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_numero_autorizacion,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_numero_autorizacion,
                                linea=linea_fila)

    def validar_via_ingreso_a_institucion(self, ah_fila, linea_fila):
        """
        Función para validar que la via de ingreso, este contenido en el rango de valores permitidos
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            valores_permitidos = self.model_fichero.obtener_via_ingreso()

            encontrado = [ah_fila[HE.AH.obtener_via_ingreso]] in valores_permitidos

            if not encontrado:
                self.detectar_error(TE.AH_VIA_INGRESO_NO_ENCONTRADA.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_VIA_INGRESO_NO_ENCONTRADA.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_VIA_INGRESO_NO_ENCONTRADA.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_VIA_INGRESO_NO_ENCONTRADA.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                linea=linea_fila)

    def validar_via_ingreso_a_institucion_1(self, ah_fila, linea_fila):
        """
        Función para validar que la via de ingreso, este contenido en el rango de valores permitidos
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        lista_au = self.lista_au
        lista_ac=self.lista_ac
        try:

            if ah_fila[HE.AH.obtener_via_ingreso] == '1':
                if lista_au !=[]:
                    encontrado = list(filter(lambda campo_au: campo_au[UAE.AU.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id], lista_au))
                    if not encontrado:
                        if lista_ac!=[]:
                            encontrado2 = list(filter(lambda campo_ac: campo_ac[ACE.AC.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id], lista_ac))
                            if encontrado2!=[]:
                                if encontrado2[0][ACE.AC.obtener_codigo_consulta] == "":
                                    self.detectar_error(TE.AH_VIA_INGRESO_1.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                              linea=linea_fila)
                            else:
                                self.detectar_error(TE.AH_VIA_INGRESO_1.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                                  linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_VIA_INGRESO_1.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_VIA_INGRESO_1.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_VIA_INGRESO_1.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
                                      
    def validar_via_ingreso_a_institucion_2(self, ah_fila, linea_fila):
        """
        Función para validar que la via de ingreso, este contenido en el rango de valores permitidos
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        lista_ac=self.lista_ac
        try:

            if ah_fila[HE.AH.obtener_via_ingreso] == '2':
                if lista_ac!=[]:
                    encontrado2 = list(filter(lambda campo_ac: campo_ac[ACE.AC.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id], lista_ac)) 
                    if encontrado2!=[]:
                        if encontrado2[0][ACE.AC.obtener_codigo_consulta] == "":
                            self.detectar_error(TE.AH_VIA_INGRESO_2.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                          linea=linea_fila)
                    else:
                        self.detectar_error(TE.AH_VIA_INGRESO_2.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                          linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_VIA_INGRESO_2.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_VIA_INGRESO_2.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_VIA_INGRESO_2.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
    
    def validar_via_ingreso_a_institucion_4(self, ah_fila, linea_fila):
        """
        Función para validar que la via de ingreso, este contenido en el rango de valores permitidos
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        lista_ap=self.lista_ap
        try:

            if ah_fila[HE.AH.obtener_via_ingreso] == '4':
                if lista_ap !=[]:
                    encontrado2 = list(filter(lambda campo_ap: campo_ap[APE.AP.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id], lista_ap)) 
                    if encontrado2!=[]:
                        if encontrado2[0][APE.AP.obtener_codigo_procedimiento] == "":
                            self.detectar_error(TE.AH_VIA_INGRESO_4.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                          linea=linea_fila)
                    else:
                        self.detectar_error(TE.AH_VIA_INGRESO_4.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                          linea=linea_fila)
                     
        except AssertionError:
            self.detectar_error(TE.AH_VIA_INGRESO_4.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_VIA_INGRESO_4.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_VIA_INGRESO_4.obtener_descripcion, HE.AH.obtener_via_ingreso,
                                      linea=linea_fila)
        

    def validar_fecha_ingreso_usuario_a_institucion(self, ah_fila, linea_fila):
        """
        Función para validar que la fecha de ingreso no sea mayor a la actual
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico.validar_fecha_menor_actual(ah_fila[HE.AH.obtener_fecha_ingreso]):
                self.detectar_error(TE.AH_FECHA_INGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_fecha_ingreso,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_FECHA_INGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_fecha_ingreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_FECHA_INGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_fecha_ingreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_FECHA_INGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_fecha_ingreso,
                                linea=linea_fila)

    def validar_causa_externa(self, ah_fila, linea_fila):
        """
        Función para validar que la causa externa, este contenido en el rango de valores permitidos
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            eapb_prestador = self.dic_eapb.get(self.codigo_prestador)

            valores_permitidos = self.model_fichero.obtener_causa_externa()

            encontrado = [ah_fila[HE.AH.obtener_causa_externa]] in valores_permitidos
            print("----------------")
            print(ah_fila[HE.AH.obtener_causa_externa])
            if not encontrado:
                self.detectar_error(TE.AH_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion, HE.AH.obtener_causa_externa,
                                    linea=linea_fila)

            if eapb_prestador[1] == "14-11" and ah_fila[HE.AH.obtener_causa_externa] == "02":
                self.detectar_error(TE.AH_CAUSA_EXTERNA_INCORRECTA_PARA_SOAP.obtener_descripcion, HE.AH.obtener_causa_externa,
                                    linea=linea_fila)

        except AssertionError:
            self.detectar_error(TE.AH_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion, HE.AH.obtener_causa_externa,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion, HE.AH.obtener_causa_externa,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion, HE.AH.obtener_causa_externa,
                                linea=linea_fila)

    def validar_estado_salida(self, ah_fila, linea_fila):
        """
        Función para validar que el estado se encuentre dentro de los valores permitidos.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            valores_permitidos = self.model_fichero.obtener_estado_salida()

            encontrado = [ah_fila[HE.AH.obtener_estado_salida]] in valores_permitidos

            if not encontrado:
                self.detectar_error(TE.AH_ESTADO_SALIDA_INCORRECTA.obtener_descripcion, HE.AH.obtener_estado_salida,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_ESTADO_SALIDA_INCORRECTA.obtener_descripcion, HE.AH.obtener_estado_salida,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_ESTADO_SALIDA_INCORRECTA.obtener_descripcion, HE.AH.obtener_estado_salida,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_ESTADO_SALIDA_INCORRECTA.obtener_descripcion, HE.AH.obtener_estado_salida,
                                linea=linea_fila)

    def validar_causa_basica_de_muerte(self, au_fila, linea_fila):
        """
        Función para validar que si el campo estado a la salida es 1=Vivo,
        la variable Causa básica de muerte en hospitalizacion debe estar vacía
        :param au_fila:
        :param linea_fila:
        :return:
        """
        try:
            if au_fila[HE.AH.obtener_estado_salida] == '1':
                if au_fila[HE.AH.obtener_causa_muerte] != "":
                    self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_INCORRECTA.obtener_descripcion,
                                          HE.AH.obtener_causa_muerte, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_INCORRECTA.obtener_descripcion,
                                          HE.AH.obtener_causa_muerte, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_INCORRECTA.obtener_descripcion,
                                          HE.AH.obtener_causa_muerte, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_INCORRECTA.obtener_descripcion,
                                          HE.AH.obtener_causa_muerte, linea=linea_fila)
        

    def validar_fecha_egreso_usuario_a_observacion(self, ah_fila, linea_fila):
        """
        Función para validar que la fecha de egreso no sea mayor a la actual
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico.validar_fecha_menor_actual(ah_fila[HE.AH.obtener_fecha_egreso]):
                self.detectar_error(TE.AH_FECHA_EGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_fecha_egreso,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_FECHA_EGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_fecha_egreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_FECHA_EGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_fecha_egreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_FECHA_EGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_fecha_egreso,
                                linea=linea_fila)

    def validar_fecha_ingreso_menor_egreso_a_institucion(self, ah_fila, linea_fila):
        """
        Función para validar que la fecha de ingreso sea anterior a la fecha de egreso
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico.validar_fecha_menor_fecha(ah_fila[HE.AH.obtener_fecha_ingreso],
                                                      ah_fila[HE.AH.obtener_fecha_egreso]):
                self.detectar_error(TE.AH_FECHA_INGRESO_MAYOR.obtener_descripcion, HE.AH.obtener_fecha_ingreso,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_FECHA_INGRESO_MAYOR.obtener_descripcion, HE.AH.obtener_fecha_ingreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_FECHA_INGRESO_MAYOR.obtener_descripcion, HE.AH.obtener_fecha_ingreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_FECHA_INGRESO_MAYOR.obtener_descripcion, HE.AH.obtener_fecha_ingreso,
                                linea=linea_fila)

    def validar_hora_ingreso_menor_salida_usuario_a_institucion(self, ah_fila, linea_fila):
        """
        Función para validar que si la fecha de ingreso es igual a la fecha de egreso,
        la hora de ingreso debe ser anterior a la hora de egreso.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if Generico().validar_fecha_igual_fecha(ah_fila[HE.AH.obtener_fecha_ingreso],
                                                    ah_fila[HE.AH.obtener_fecha_egreso]):
                if not Generico().validar_hora_menor_fecha(ah_fila[HE.AH.obtener_hora_ingreso],
                                                           ah_fila[HE.AH.obtener_hora_egreso]):
                    self.detectar_error(TE.AH_HORA_INGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_hora_ingreso,
                                        linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_HORA_INGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_hora_ingreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_HORA_INGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_hora_ingreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_HORA_INGRESO_INCORRECTA.obtener_descripcion, HE.AH.obtener_hora_ingreso,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_ingreso(self, ah_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_principal_ingreso]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)
            if encontrado is None:
                self.detectar_error(TE.AH_DIAGNOSTICO_INGRESO_NO_ENCCONTRADO.obtener_descripcion,
                                    HE.AH.obtener_diagnostico_principal_ingreso,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_INGRESO_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_INGRESO_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_INGRESO_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_ingreso_2(self, ah_fila, linea_fila):
        """
        Se valida que no sea un código “Z”.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_principal_ingreso].startswith('Z'):
                self.detectar_error(TE.AH_DIAGNOSTICO_INGRESO_INCORRECTO.obtener_descripcion,
                                    HE.AH.obtener_diagnostico_principal_ingreso,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_INGRESO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_INGRESO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_INGRESO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_ingreso_sexo(self, ah_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:

            diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_principal_ingreso]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)

            if encontrado is not None:
                if not encontrado[1] == 'A':
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                            self.detectar_error(TE.AH_SEXO_INCORRECTO.obtener_descripcion,
                                                HE.AH.obtener_diagnostico_principal_ingreso,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_SEXO_INCORRECTO.obtener_descripcion, HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_SEXO_INCORRECTO.obtener_descripcion, HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_SEXO_INCORRECTO.obtener_descripcion, HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_ingreso_edad(self, ah_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:

            diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_principal_ingreso]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)

            if encontrado is not None:
                lista_us = self.lista_us
                encontrado2 = list(
                    filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                           lista_us))

                if encontrado2:
                    if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                        encontrado2[0][USE.US.obtener_medida_de_edad],
                                                                        encontrado[2], encontrado[3]):
                        self.detectar_error(TE.AH_EDAD_INCORRECTA.obtener_descripcion,
                                            HE.AH.obtener_diagnostico_principal_ingreso,
                                            linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_diagnostico_principal_ingreso,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_1(self, ah_fila, linea_fila):
        """
        Se valida que en caso de que se registre, se encuentre dentro de la (cie10)
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_relacionado_1]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is None:
                    self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_NO_ENCCONTRADO.obtener_descripcion,
                                        HE.AH.obtener_diagnostico_relacionado_1,
                                        linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_1_sexo(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ah_fila:
        :param linea_fila:
        :return:
        """

        try:
            if ah_fila[HE.AH.obtener_diagnostico_relacionado_1]:

                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(
                                lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                                lista_us))

                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_SEXO_INCORRECTO.obtener_descripcion,
                                                    HE.AH.obtener_diagnostico_relacionado_1,
                                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_1_edad(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_relacionado_1]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][
                                                                                USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_EDAD_INCORRECTA.obtener_descripcion,
                                                HE.AH.obtener_diagnostico_relacionado_1,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_1_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_1,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_2(self, ah_fila, linea_fila):
        """
        Se valida que en caso de que se registre, se encuentre dentro de la (cie10)
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_relacionado_2]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is None:
                    self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_NO_ENCCONTRADO.obtener_descripcion,
                                        HE.AH.obtener_diagnostico_relacionado_2,
                                        linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_2_sexo(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_relacionado_2]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(
                                lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                                lista_us))

                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_SEXO_INCORRECTO.obtener_descripcion,
                                                    HE.AH.obtener_diagnostico_relacionado_2,
                                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_2_edad(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_relacionado_2]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][
                                                                                USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_EDAD_INCORRECTA.obtener_descripcion,
                                                HE.AH.obtener_diagnostico_relacionado_2,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_2_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_2,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_3(self, ah_fila, linea_fila):
        """
        Se valida que en caso de que se registre, se encuentre dentro de la (cie10)
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_relacionado_3]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is None:
                    self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_NO_ENCCONTRADO.obtener_descripcion,
                                        HE.AH.obtener_diagnostico_relacionado_3,
                                        linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_3_sexo(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_relacionado_3]:

                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(
                                lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                                lista_us))

                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_SEXO_INCORRECTO.obtener_descripcion,
                                                    HE.AH.obtener_diagnostico_relacionado_3,
                                                    linea=linea_fila)

        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)

    def validar_diagnostico_relacionado_3_edad(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:

            if ah_fila[HE.AH.obtener_diagnostico_relacionado_3]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][
                                                                                USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_EDAD_INCORRECTA.obtener_descripcion,
                                                HE.AH.obtener_diagnostico_relacionado_3,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_RELACIONADO_3_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_diagnostico_relacionado_3,
                                linea=linea_fila)

    def validar_causa_basica_de_muerte_estado_salida(self, ah_fila, linea_fila):
        """
        Se valida que el campo causa básica de muerte no sea nulo, si el estado es igual a 2
        y que se encuentre dentro de la (cie10)
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_estado_salida] == '2':
                if ah_fila[HE.AH.obtener_causa_muerte]!="":
                    cie10 = self.model_fichero.obtener_cie10()
        
                    encontrado = list(
                        filter(lambda campo_cie10: campo_cie10[0] == ah_fila[HE.AH.obtener_causa_muerte],
                               cie10))
        
                    if not encontrado:
                        self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                                      HE.AH.obtener_causa_muerte, linea=linea_fila)
                else:
                    self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                                      HE.AH.obtener_causa_muerte, linea=linea_fila)
                                                      
        except AssertionError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                                  HE.AH.obtener_causa_muerte, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                                  HE.AH.obtener_causa_muerte, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                                  HE.AH.obtener_causa_muerte, linea=linea_fila)

        

    def validar_causa_basica_de_muerte_edad(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_causa_muerte]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_causa_muerte]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                               lista_us))

                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][
                                                                                USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_EDAD_INCORRECTA.obtener_descripcion,
                                                HE.AH.obtener_causa_muerte,
                                                linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_causa_muerte,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_causa_muerte,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_EDAD_INCORRECTA.obtener_descripcion,
                                HE.AH.obtener_causa_muerte,
                                linea=linea_fila)

    def validar_causa_basica_de_muerte_sexo(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_causa_muerte]:

                diagnostico_ahfila = ah_fila[HE.AH.obtener_causa_muerte]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(
                                lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                                lista_us))

                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_SEXO_INCORRECTO.obtener_descripcion,
                                                    HE.AH.obtener_causa_muerte,
                                                    linea=linea_fila)

        except AssertionError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_causa_muerte,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_causa_muerte,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_CAUSA_BASICA_MUERTE_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_causa_muerte,
                                linea=linea_fila)

    def validar_diagnostico_principal_de_egreso(self, ah_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_principal_egreso]
            encontrado =  self.cie10_dic.get(diagnostico_ahfila)
            if encontrado is None:
                self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_NO_ENCCONTRADO.obtener_descripcion,
                                    HE.AH.obtener_diagnostico_principal_egreso,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_egreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_egreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_NO_ENCCONTRADO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_egreso,
                                linea=linea_fila)

    def validar_diagnostico_egreso_sexo(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_diagnostico_principal_egreso]:

                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_principal_egreso]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(
                                lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                                lista_us))

                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_SEXO_INCORRECTO.obtener_descripcion,
                                                    HE.AH.obtener_diagnostico_principal_egreso,
                                                    linea=linea_fila)

        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_egreso,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_egreso,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_SEXO_INCORRECTO.obtener_descripcion,
                                HE.AH.obtener_diagnostico_principal_egreso,
                                linea=linea_fila)

    def validar_diagnostico_egreso_edad(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            
            if ah_fila[HE.AH.obtener_diagnostico_principal_egreso]:
                diagnostico_ahfila = ah_fila[HE.AH.obtener_diagnostico_principal_egreso]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
    
                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                               lista_us))
                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_diagnostico_principal_egreso,
                                                  linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_diagnostico_principal_egreso,
                                                  linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_diagnostico_principal_egreso,
                                                  linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_DIAGNOSTICO_EGRESO_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_diagnostico_principal_egreso,
                                                  linea=linea_fila)
                                                  
                                                  
    def validar_diagnostico_complicacion(self, ah_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_complicacion]!="":
                diagnostico_ahfila = ah_fila[HE.AH.obtener_complicacion]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

                if encontrado is None:
                    self.detectar_error(TE.AH_COMPLICACION_MUERTE.obtener_descripcion, HE.AH.obtener_complicacion,
                                          linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE.obtener_descripcion, HE.AH.obtener_complicacion,
                                      linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE.obtener_descripcion, HE.AH.obtener_complicacion,
                                      linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE.obtener_descripcion, HE.AH.obtener_complicacion,
                                      linea=linea_fila)
                                      
    def validar_diagnostico_complicacion_sexo(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ah_fila[HE.AH.obtener_complicacion]!="":

                diagnostico_ahfila = ah_fila[HE.AH.obtener_complicacion]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)

    
                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        lista_us = self.lista_us
                        encontrado2 = list(
                            filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                                   lista_us))
    
                        if encontrado2:
                            if not Generico().validar_sexo(encontrado2[0][USE.US.obtener_sexo],encontrado[1]):
                                self.detectar_error(TE.AH_COMPLICACION_MUERTE_SEXO_INCORRECTO.obtener_descripcion, HE.AH.obtener_complicacion,
                                                      linea=linea_fila)

        except AssertionError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE_SEXO_INCORRECTO.obtener_descripcion, HE.AH.obtener_complicacion,
                                                      linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE_SEXO_INCORRECTO.obtener_descripcion, HE.AH.obtener_complicacion,
                                                      linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE_SEXO_INCORRECTO.obtener_descripcion, HE.AH.obtener_complicacion,
                                                      linea=linea_fila)

        
    def validar_diagnostico_complicacion_edad(self, ah_fila, linea_fila):
        """
        En caso de que se registre, validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        :param ah_fila:
        :param linea_fila:
        :return:
        """
        try:
            
            if ah_fila[HE.AH.obtener_complicacion] != "":
                diagnostico_ahfila = ah_fila[HE.AH.obtener_complicacion]
                encontrado =  self.cie10_dic.get(diagnostico_ahfila)
                if encontrado is not None:
                    lista_us = self.lista_us
                    encontrado2 = list(
                        filter(lambda campo_us: campo_us[USE.US.obtener_numero_id] == ah_fila[HE.AH.obtener_numero_id],
                               lista_us))
    
                    if encontrado2:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[0][USE.US.obtener_edad],
                                                                            encontrado2[0][USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AH_COMPLICACION_MUERTE_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_complicacion,
                                                  linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_complicacion,
                                                  linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_complicacion,
                                                  linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AH_COMPLICACION_MUERTE_EDAD_INCORRECTA.obtener_descripcion, HE.AH.obtener_complicacion,
                                                  linea=linea_fila)

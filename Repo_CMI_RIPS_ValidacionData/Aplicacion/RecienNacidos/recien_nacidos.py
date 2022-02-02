# -*- coding: utf-8 -*-
from datetime import date
from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.RecienNacidos.recien_nacidos import ModeloRecienNacidos
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as TSE
from Utilidades.Enumerados.Archivo.recien_nacidos_enum import RecienNacidosColumnaEnum as RNE
from Utilidades.Enumerados.Archivo.hospitalizaciones_enum import HospitalizacionesColumnasEnum as HE
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico, ValidacionGenerico
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as USE


class ValidacionRecienNacidos(ValidacionBase):

    def __init__(self,lista_af,lista_us,lista_ah,cie10,af,us):
        super().__init__()
        self.nombre_archivo = 'AN'
        self.model = ModeloRecienNacidos.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.lista_af=lista_af
        self.lista_us=lista_us
        self.lista_ah=lista_ah
        self.cie10_dic= cie10
        self.dic_af=af
        self.dic_us=us



    def validar_codigo_habilitacion(self, ac_fila, linea_fila, codigo_habilitacion):
        """
        Función para validar que el código de habilitación, este contenido en todos los registros de CT
        :param ac_fila:
        :param linea_fila:
        :param codigo_habilitacion:
        :return:
        """
        if not ac_fila[RNE.AN.obtener_codigo_prestador] == codigo_habilitacion:
            self.detectar_error(TE.CT_CODIGO_HABILITACION_INTERNO.obtener_descripcion,
                                RNE.AN.AC.obtener_codigo_prestador, linea_fila)
            self.generar_archivo_errores(self.lista_errores)

    def validar_numero_factura(self, an_fila, linea_fila):
        """
        Función para validar que el numero de factura, este contenido en el archivo de transacciones
        :param an_fila:
        :param linea_fila:
        :return:
        """
        numero_factura = an_fila[RNE.AN.obtener_numero_factura]
        encontrado =  self.dic_af.get(numero_factura)
        if encontrado is None:
            self.detectar_error(TE.AN_FACTURA_NO_ENCONTRADA.obtener_descripcion, RNE.AN.obtener_numero_factura,
                                linea=linea_fila)

    def validar_tipo_id_madre(self, an_fila, linea_fila):
        tipo_id_madre = [an_fila[RNE.AN.obtener_tipo_id_madre]]
        fichero_tipo_id = self.model_fichero.obtener_tipo_id_usuario()
        if tipo_id_madre not in fichero_tipo_id:
            self.detectar_error(TE.AN_TIPO_ID_MADRE_NO_ENCONTRADA.obtener_descripcion, RNE.AN.obtener_tipo_id_madre,
                                linea_fila)

    def validar_tipo_numero_identificacion(self, an_fila, linea_fila):
        """
        Función para validar que el tipo y numero de identificación, coincida con el archivo de usuarios
        :param an_fila:
        :param linea_fila:
        :return:
        """
        lista_ah = self.lista_ah

        try:
            numero_id =  an_fila[RNE.AN.obtener_numero_id_madre]
            encontrado =  self.dic_us.get(numero_id)

            encontrado2 = list(
                filter(
                    lambda campo_ah: campo_ah[HE.AH.obtener_numero_id] == an_fila[RNE.AN.obtener_numero_id_madre] and
                                     campo_ah[HE.AH.obtener_tipo_id] == an_fila[RNE.AN.obtener_tipo_id_madre],
                    lista_ah))
            if not encontrado or not encontrado2:
                self.detectar_error(TE.AN_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                    RNE.AN.obtener_numero_id_madre, linea=linea_fila)

        except AssertionError:
            self.detectar_error(TE.AN_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, RNE.AN.obtener_numero_id_madre,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AN_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, RNE.AN.obtener_numero_id_madre,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AN_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion, RNE.AN.obtener_numero_id_madre,
                                linea=linea_fila)

    def validar_fecha_nacimiento(self, an_fila, linea_fila):
        estado = ValidacionGenerico.validar_fecha_menor_actual(an_fila[RNE.AN.obtener_fecha_nacimiento])
        if not estado:
            self.detectar_error(TE.AN_FECHA_NACIMIENTO_INCORRECTA.obtener_descripcion, RNE.AN.obtener_fecha_nacimiento,
                                linea_fila)

    def validar_fecha_muerte_actual(self, an_fila, linea_fila):
        if an_fila[RNE.AN.obtener_fecha_de_muerte] != '':
            estado = ValidacionGenerico.validar_fecha_menor_actual(an_fila[RNE.AN.obtener_fecha_de_muerte])
            if not estado:
                self.detectar_error(TE.AN_FECHA_MUERTE_INCORRECTA.obtener_descripcion, RNE.AN.obtener_fecha_de_muerte,
                                    linea_fila)

    def validar_fecha_muerte_nacimiento(self, an_fila, linea_fila):
        fecha_muerte = an_fila[RNE.AN.obtener_fecha_de_muerte]
        fecha_nacimiento = an_fila[RNE.AN.obtener_fecha_nacimiento]
        if fecha_muerte != '':
            if fecha_muerte < fecha_nacimiento:
                self.detectar_error(TE.AN_FECHA_MUERTE_NACIMIENTO_INCORRECTA.obtener_descripcion,
                                    RNE.AN.obtener_fecha_de_muerte, linea_fila)

    def validar_control_prenatal(self, an_fila, linea_fila):
        control_prenatal = [an_fila[RNE.AN.obtener_control_prenatal]]
        fichero_control_prenatal = self.model_fichero.obtener_control_prenatal()
        if control_prenatal not in fichero_control_prenatal:
            self.detectar_error(TE.AN_CONTROL_PRENATAL_INCORRECTO.obtener_descripcion,
                                RNE.AN.obtener_control_prenatal, linea_fila)

    def validar_sexo(self, an_fila, linea_fila):
        sexo = [an_fila[RNE.AN.obtener_sexo_nacido]]
        fichero_sexo = self.model_fichero.obtener_sexo()
        if sexo not in fichero_sexo:
            self.detectar_error(TE.AN_SEXO_INVALIDO.obtener_descripcion,
                                RNE.AN.obtener_sexo_nacido, linea_fila)

    def validar_diagnostico_nacido(self, an_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param an_fila:
        :param linea_fila:
        :return:
        """

        if an_fila[RNE.AN.obtener_diagnostico_de_nacido] != "":
            diagnostico_anfila = an_fila[RNE.AN.obtener_diagnostico_de_nacido]
            encontrado =  self.cie10_dic.get(diagnostico_anfila)
            if encontrado is None:
                self.detectar_error(TE.AN_DIAGNOSTICO_NO_ENCCONTRADO.obtener_descripcion,
                                    RNE.AN.obtener_diagnostico_de_nacido,
                                    linea=linea_fila)

    def validar_diagnostico_nacido_sexo(self, an_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param an_fila:
        :param linea_fila:
        :return:
        """

        if an_fila[RNE.AN.obtener_diagnostico_de_nacido] != "":
            diagnostico_anfila = an_fila[RNE.AN.obtener_diagnostico_de_nacido]
            encontrado =  self.cie10_dic.get(diagnostico_anfila)
            if encontrado is not None:
                if not encontrado[1] == 'A':
                    if not Generico().validar_sexo(an_fila[RNE.AN.obtener_sexo_nacido], encontrado[1]):
                        self.detectar_error(TE.AN_SEXO_INCORRECTO.obtener_descripcion,
                                            RNE.AN.obtener_diagnostico_de_nacido,
                                            linea=linea_fila)

    def validar_diagnostico_nacido_edad(self, an_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param an_fila:
        :param linea_fila:
        :return:
        """
        if an_fila[RNE.AN.obtener_diagnostico_de_nacido] != "":

            diagnostico_anfila = an_fila[RNE.AN.obtener_diagnostico_de_nacido]
            encontrado =  self.cie10_dic.get(diagnostico_anfila)
            if encontrado is not None:
                edad_gestacional = int(an_fila[RNE.AN.obtener_edad_gestacional])
                edad_gestacional_dia = edad_gestacional * 7
                unidad_medida = '3'
                if not Generico().validar_edad_con_unidad_de_medida(edad_gestacional_dia, unidad_medida,
                                                                    encontrado[2],
                                                                    encontrado[3]):
                    self.detectar_error(TE.AN_EDAD_INCORRECTA.obtener_descripcion,
                                        RNE.AN.obtener_diagnostico_de_nacido,
                                        linea=linea_fila)

    def validar_causa_muerte(self, an_fila, linea_fila):
        """
        Se valida que se encuentre dentro de la tabla de la (cie10)
        :param an_fila:
        :param linea_fila:
        :return:
        """
        if an_fila[RNE.AN.obtener_causa_de_muerte] != '':
            diagnostico_anfila = an_fila[RNE.AN.obtener_causa_de_muerte]
            encontrado =  self.cie10_dic.get(diagnostico_anfila)
            if encontrado is None:
                self.detectar_error(TE.AN_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA.obtener_descripcion,
                                    RNE.AN.obtener_causa_de_muerte,
                                    linea=linea_fila)

    def validar_causa_muerte2(self, an_fila, linea_fila):
        try:
            lista_ah = self.lista_ah

            if lista_ah:
                encontrado = list(
                    filter(lambda campo_ap:
                           campo_ap[HE.AH.obtener_numero_id] == an_fila[RNE.AN.obtener_numero_id_madre], lista_ah))
                if encontrado:
                    if encontrado[0][HE.AH.obtener_estado_salida] == "2" and an_fila[
                        RNE.AN.obtener_causa_de_muerte] == "":
                        self.detectar_error(TE.AN_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                            RNE.AN.obtener_causa_de_muerte,
                                            linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AN_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                RNE.AN.obtener_causa_de_muerte,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AN_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                RNE.AN.obtener_causa_de_muerte,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AN_CAUSA_BASICA_MUERTE_VACIA_O_NO_ENCONTRADA2.obtener_descripcion,
                                RNE.AN.obtener_causa_de_muerte,
                                linea=linea_fila)

    def validar_causa_muerte_sexo(self, an_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para sexo.
        :param an_fila:
        :param linea_fila:
        :return:
        """

        if an_fila[RNE.AN.obtener_causa_de_muerte] != '':
            diagnostico_anfila = an_fila[RNE.AN.obtener_causa_de_muerte]
            encontrado =  self.cie10_dic.get(diagnostico_anfila)
            if encontrado is not None:
                if not encontrado[1] == 'A':
                    if not Generico().validar_sexo(an_fila[RNE.AN.obtener_sexo_nacido], encontrado[1]):
                        self.detectar_error(TE.AN_CAUSA_BASICA_MUERTE_SEXO_INCORRECTO.obtener_descripcion,
                                            RNE.AN.obtener_causa_de_muerte,
                                            linea=linea_fila)

    def validar_causa_muerte_edad(self, an_fila, linea_fila):
        """
        Validar referencia cruzada entre: datos de sexo y los diagnósticos de la CIE 10.
        Tabla de referencia con rangos permitidos para edad.
        :param an_fila:
        :param linea_fila:
        :return:
        """

        if an_fila[RNE.AN.obtener_causa_de_muerte] != '':
            diagnostico_anfila = an_fila[RNE.AN.obtener_causa_de_muerte]
            encontrado =  self.cie10_dic.get(diagnostico_anfila)
            if encontrado is not None:
                edad_gestacional = int(an_fila[RNE.AN.obtener_edad_gestacional])
                edad_gestacional_dia = edad_gestacional * 7
                unidad_medida = '3'
                if not Generico().validar_edad_con_unidad_de_medida(edad_gestacional_dia, unidad_medida,
                                                                    encontrado[2],
                                                                    encontrado[3]):
                    self.detectar_error(TE.AN_CAUSA_BASICA_MUERTE_EDAD_INCORRECTA.obtener_descripcion,
                                        RNE.AN.obtener_causa_de_muerte,
                                        linea=linea_fila)

    def validar_causa_fecha_muerte_hora_muerte(self, an_fila, linea_fila):
        causa_muerte = an_fila[RNE.AN.obtener_causa_de_muerte]
        fecha_muerte = an_fila[RNE.AN.obtener_fecha_de_muerte]
        hora_muerte = an_fila[RNE.AN.obtener_hora_de_muerte]
        if (causa_muerte != '' and (fecha_muerte == '' or hora_muerte == '')) or (
                fecha_muerte != '' and (causa_muerte == '' or hora_muerte == '')) or (
                hora_muerte != '' and (causa_muerte == '' or fecha_muerte == '')):
            self.detectar_error(TE.AN_INCONSISTENCIA_MUERTE.obtener_descripcion, RNE.AN.obtener_causa_de_muerte,
                                linea_fila)

    def validar_horas_fechas_iguales(self, an_fila, linea_fila):
        fecha_muerte = an_fila[RNE.AN.obtener_fecha_de_muerte]
        hora_muerte = an_fila[RNE.AN.obtener_hora_de_muerte]
        fecha_nacimiento = an_fila[RNE.AN.obtener_fecha_nacimiento]
        hora_nacimiento = an_fila[RNE.AN.obtener_hora_nacimiento]
        if fecha_muerte == fecha_nacimiento:
            if not Generico().validar_hora_menor_fecha(hora_nacimiento, hora_muerte):
                self.detectar_error(TE.AN_FECHA_HORA_MUERTE_INVALIDA.obtener_descripcion,
                                    RNE.AN.obtener_hora_nacimiento, linea_fila)

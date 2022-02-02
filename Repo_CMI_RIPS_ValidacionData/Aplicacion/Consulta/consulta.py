from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.Consulta.consulta import ModeloConsulta
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as TSE
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as USE
from Utilidades.Enumerados.Archivo.consulta_enum import ConsultaColumnasEnum as Columnas
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE


class ValidacionConsulta(ValidacionBase):

    def __init__(self,lista_af,lista_us,cups,cie10,af,us):
        super().__init__()
        self.nombre_archivo = 'AC'
        self.model = ModeloConsulta.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.codigo_habilitacion = ''
        self.lista_af=lista_af
        self.lista_us = lista_us
        self.cups_dic = cups
        self.cie10_dic= cie10
        self.dic_af=af
        self.dic_us=us

    def validar_codigo_habilitacion(self, ac_fila, linea_fila):
        """
        Función para validar que el código de habilitación, este contenido en todos los registros de CT
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not ac_fila[Columnas.AC.obtener_codigo_prestador] == self.codigo_habilitacion:
                self.detectar_error(TE.AC_CODIGO_HABILITACION_INTERNO.obtener_descripcion,
                                    Columnas.AC.obtener_codigo_prestador, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_CODIGO_HABILITACION_INTERNO.obtener_descripcion,
                                Columnas.AC.obtener_codigo_prestador, linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_CODIGO_HABILITACION_INTERNO.obtener_descripcion,
                                Columnas.AC.obtener_codigo_prestador, linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_CODIGO_HABILITACION_INTERNO.obtener_descripcion,
                                Columnas.AC.obtener_codigo_prestador, linea_fila)

    def validar_numero_factura(self, ac_fila, linea_fila):
        """
        Función para validar que el numero de factura, este contenido en el archivo de transacciones
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            numero_factura = ac_fila[Columnas.AC.obtener_numero_factura]
            encontrado =  self.dic_af.get(numero_factura)
            if encontrado is None:
                self.detectar_error(TE.AC_FACTURA_NO_ENCONTRADA.obtener_descripcion, Columnas.AC.obtener_numero_factura,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_FACTURA_NO_ENCONTRADA.obtener_descripcion, Columnas.AC.obtener_numero_factura,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_FACTURA_NO_ENCONTRADA.obtener_descripcion, Columnas.AC.obtener_numero_factura,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_FACTURA_NO_ENCONTRADA.obtener_descripcion, Columnas.AC.obtener_numero_factura,
                                linea=linea_fila)

    def validar_tipo_numero_identificacion(self, ac_fila, linea_fila):
        """
        Función para validar que el tipo y numero de identificación, coincida con el archivo de usuarios
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        
        numero_id = ac_fila[Columnas.AC.obtener_numero_id]
        encontrado =  self.dic_us.get(numero_id)
        if encontrado is None:
            self.detectar_error(TE.AC_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                posicion_columna=Columnas.AC.obtener_tipo_id,
                                linea=linea_fila)
        elif not encontrado[USE.US.obtener_tipo_id] == ac_fila[Columnas.AC.obtener_tipo_id]:
            self.detectar_error(TE.AC_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                posicion_columna=Columnas.AC.obtener_tipo_id,
                                linea=linea_fila)


    def validar_tipo_id(self, ac_fila, linea_fila):
        try:
            fichero_tipo_id = self.model_fichero.obtener_tipo_id_usuario()
            encontrado = list(
                filter(lambda fichero: fichero[0] == ac_fila[Columnas.AC.obtener_tipo_id], fichero_tipo_id))
            if not encontrado:
                self.detectar_error(TE.AC_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                    Columnas.AC.obtener_tipo_id, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                Columnas.AC.obtener_tipo_id, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                Columnas.AC.obtener_tipo_id, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                Columnas.AC.obtener_tipo_id, linea=linea_fila)

    def validar_fecha_procedimiento(self, ac_fila, linea_fila):
        try:
            if not Generico().validar_fecha_menor_actual(ac_fila[Columnas.AC.obtener_fecha_consulta]):
                self.detectar_error(TE.AC_FECHA_CONSULTA_INCORRECTA.obtener_descripcion,
                                    Columnas.AC.obtener_fecha_consulta, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_FECHA_CONSULTA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_fecha_consulta, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_FECHA_CONSULTA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_fecha_consulta, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_FECHA_CONSULTA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_fecha_consulta, linea=linea_fila)

    def validar_codigo_consulta(self, ac_fila, linea_fila):
        try:
            cod_servicio_acfila = ac_fila[Columnas.AC.obtener_codigo_consulta]
            encontrado_cups =  self.cups_dic.get(cod_servicio_acfila)
            if encontrado_cups is None:
                self.detectar_error(TE.AC_CODIGO_CONSULTA_INCORRECTO.obtener_descripcion,
                                    Columnas.AC.obtener_codigo_consulta, linea=linea_fila)
            else:
                if encontrado_cups[3]!="AC":
                    self.detectar_error(TE.AC_CODIGO_CONSULTA_INCORRECTO.obtener_descripcion,
                                    Columnas.AC.obtener_codigo_consulta, linea=linea_fila)

        except AssertionError:
            self.detectar_error(TE.AC_CODIGO_CONSULTA_INCORRECTO.obtener_descripcion,
                                    Columnas.AC.obtener_codigo_consulta, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_CODIGO_CONSULTA_INCORRECTO.obtener_descripcion,
                                    Columnas.AC.obtener_codigo_consulta, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_CODIGO_CONSULTA_INCORRECTO.obtener_descripcion,
                                    Columnas.AC.obtener_codigo_consulta, linea=linea_fila)

    def validar_finalidad_consulta(self, ac_fila, linea_fila):
        try:
            finalidad_consulta = ac_fila[Columnas.AC.obtener_finalidad_consulta]
            fichero_finalidad_consulta = self.model_fichero.obtener_finalidad_consulta()
            encontrado = list(filter(lambda fichero: fichero[0] == finalidad_consulta, fichero_finalidad_consulta))
            if not encontrado:
                self.detectar_error(TE.AC_FINALIDAD_CONSULTA_INCORRECTA.obtener_descripcion,
                                    Columnas.AC.obtener_finalidad_consulta, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_FINALIDAD_CONSULTA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_FINALIDAD_CONSULTA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_FINALIDAD_CONSULTA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea=linea_fila)

    def validar_causa_externa(self, ac_fila, linea_fila):
        try:
            fichero_causa_externa = self.model_fichero.obtener_causa_externa()
            encontrado = list(
                filter(lambda fichero: fichero[0] == ac_fila[Columnas.AC.obtener_causa_externa], fichero_causa_externa))
            if not encontrado:
                self.detectar_error(TE.AC_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion,
                                    Columnas.AC.obtener_causa_externa, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_causa_externa, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_causa_externa, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_CAUSA_EXTERNA_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_causa_externa, linea=linea_fila)

    def validar_codigo_diagnostico_principal(self, ac_fila, linea_fila):
        try:
            diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_acfila)

            if encontrado is None:
                self.detectar_error(TE.AC_CODIGO_DIAGNOSTICO_PRINCIPAL_NO_ENCONTRADO.obtener_descripcion,
                                    Columnas.AC.obtener_diagnostico_principal, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_CODIGO_DIAGNOSTICO_PRINCIPAL_NO_ENCONTRADO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_principal, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_CODIGO_DIAGNOSTICO_PRINCIPAL_NO_ENCONTRADO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_principal, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_CODIGO_DIAGNOSTICO_PRINCIPAL_NO_ENCONTRADO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_principal, linea=linea_fila)

    def validar_tipo_diagnostico_principal(self, ac_fila, linea_fila):
        try:
            fichero_tipo_diagnostico_principal = self.model_fichero.obtener_diagnostico_principal()
            encontrado = list(filter(lambda fichero: fichero[0] == ac_fila[Columnas.AC.obtener_tipo_diagnostico],
                                     fichero_tipo_diagnostico_principal))
            if not encontrado:
                self.detectar_error(TE.AC_TIPO_DIAGNOSTICO_INCORRECTO.obtener_descripcion,
                                    Columnas.AC.obtener_tipo_diagnostico, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_TIPO_DIAGNOSTICO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_tipo_diagnostico, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_TIPO_DIAGNOSTICO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_tipo_diagnostico, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_TIPO_DIAGNOSTICO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_tipo_diagnostico, linea=linea_fila)

    def validar_diagnostico_principal_sexo(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_acfila)
            if encontrado is not None:
                if not encontrado[1] == 'A':
                    numero_id = ac_fila[Columnas.AC.obtener_numero_id]
                    encontrado2 =  self.dic_us.get(numero_id)

                    if encontrado2 is not None:
                        if not Generico().validar_sexo(encontrado2[USE.US.obtener_sexo], encontrado[1]):
                            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                                Columnas.AC.obtener_diagnostico_principal, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_principal, linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_principal, linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_principal, linea_fila)

    def validar_diagnostico_principal_edad(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_principal]
            encontrado =  self.cie10_dic.get(diagnostico_acfila)

            if encontrado is not None:
                numero_id = ac_fila[Columnas.AC.obtener_numero_id]
                encontrado2 =  self.dic_us.get(numero_id)

                if encontrado2 is not None:
                    if not Generico().validar_edad_con_unidad_de_medida(encontrado2[USE.US.obtener_edad],
                                                                        encontrado2[USE.US.obtener_medida_de_edad],
                                                                        encontrado[2], encontrado[3]):
                        self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                            Columnas.AC.obtener_diagnostico_principal, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, Columnas.AC.obtener_diagnostico_principal,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, Columnas.AC.obtener_diagnostico_principal,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, Columnas.AC.obtener_diagnostico_principal,
                                linea=linea_fila)

    def validar_finalidad_diagnostico_1(self, ac_fila, linea_fila):
        try:
            finalidad = ac_fila[Columnas.AC.obtener_finalidad_consulta]
            diagnostico = ac_fila[Columnas.AC.obtener_diagnostico_principal]
            fichero_finalidad = self.model_fichero.obtener_finalidad_consulta()
            encontrado = list(filter(lambda fichero: fichero[0] == finalidad, fichero_finalidad))
            if encontrado and finalidad != '10':
                if diagnostico[0] != 'Z':
                    self.detectar_error(TE.AC_FINALIDAD_DIAGNOSTICO_1.obtener_descripcion,
                                        Columnas.AC.obtener_finalidad_consulta, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_FINALIDAD_DIAGNOSTICO_1.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_FINALIDAD_DIAGNOSTICO_1.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_FINALIDAD_DIAGNOSTICO_1.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea_fila)

    def validar_finalidad_diagnostico_2(self, ac_fila, linea_fila):
        try:
            finalidad = ac_fila[Columnas.AC.obtener_finalidad_consulta]
            diagnostico = ac_fila[Columnas.AC.obtener_diagnostico_principal]
            fichero_finalidad = self.model_fichero.obtener_finalidad_consulta()
            encontrado = list(filter(lambda fichero: fichero[0] == finalidad, fichero_finalidad))
            if encontrado:
                if finalidad == '10' and diagnostico[0] == 'Z':
                    self.detectar_error(TE.AC_FINALIDAD_DIAGNOSTICO_2.obtener_descripcion,
                                        Columnas.AC.obtener_finalidad_consulta, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_FINALIDAD_DIAGNOSTICO_2.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_FINALIDAD_DIAGNOSTICO_2.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_FINALIDAD_DIAGNOSTICO_2.obtener_descripcion,
                                Columnas.AC.obtener_finalidad_consulta, linea_fila)

    def validar_diagnostico_relacionado_1(self, ac_fila, linea_fila):
        try:

            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_1] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is None:
                    self.detectar_error(TE.AC_DIAGNOSTICO_R1_NO_ENCCONTRADO.obtener_descripcion,
                                        Columnas.AC.obtener_diagnostico_relacionado_1, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, USE.US.obtener_numero_id,
                                linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, USE.US.obtener_numero_id,
                                linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, USE.US.obtener_numero_id,
                                linea_fila)

    def validar_diagnostico_relacionado_1_sexo(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_1] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        numero_id = ac_fila[Columnas.AC.obtener_numero_id]
                        encontrado2 =  self.dic_us.get(numero_id)

                        if encontrado2 is not None:
                            if not Generico().validar_sexo(encontrado2[USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                                    Columnas.AC.obtener_diagnostico_relacionado_1, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_1, linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_1, linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_1, linea_fila)

    def validar_diagnostico_relacionado_1_edad(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_1] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_1]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is not None:
                    numero_id = ac_fila[Columnas.AC.obtener_numero_id]
                    encontrado2 =  self.dic_us.get(numero_id)

                    if encontrado2 is not None:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[USE.US.obtener_edad],
                                                                            encontrado2[
                                                                                USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                                Columnas.AC.obtener_diagnostico_relacionado_1, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_1, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_1, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_1, linea=linea_fila)

    def validar_diagnostico_relacionado_2(self, ac_fila, linea_fila):
        try:
            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_2] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is None:
                    self.detectar_error(TE.AC_DIAGNOSTICO_R2_NO_ENCCONTRADO.obtener_descripcion,
                                        Columnas.AC.obtener_diagnostico_relacionado_2, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_DIAGNOSTICO_R2_NO_ENCCONTRADO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_DIAGNOSTICO_R2_NO_ENCCONTRADO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_DIAGNOSTICO_R2_NO_ENCCONTRADO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea_fila)

    def validar_diagnostico_relacionado_2_sexo(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_2] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is not None:
                    if not encontrado[1] == 'A':
                        numero_id = ac_fila[Columnas.AC.obtener_numero_id]
                        encontrado2 =  self.dic_us.get(numero_id)
                        if encontrado2 is not None:
                            if not Generico().validar_sexo(encontrado2[USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                                    Columnas.AC.obtener_diagnostico_relacionado_2, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea_fila)

    def validar_diagnostico_relacionado_2_edad(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_2] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_2]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is not None:
                    numero_id = ac_fila[Columnas.AC.obtener_numero_id]
                    encontrado2 =  self.dic_us.get(numero_id)

                    if encontrado2 is not None:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[USE.US.obtener_edad],
                                                                            encontrado2[
                                                                                USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                                Columnas.AC.obtener_diagnostico_relacionado_2, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_2, linea=linea_fila)

    def validar_diagnostico_relacionado_3(self, ac_fila, linea_fila):
        try:
            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_3] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is None:
                    self.detectar_error(TE.AC_DIAGNOSTICO_R3_NO_ENCCONTRADO.obtener_descripcion,
                                        Columnas.AC.obtener_diagnostico_relacionado_3, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, USE.US.obtener_numero_id,
                                linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, USE.US.obtener_numero_id,
                                linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion, USE.US.obtener_numero_id,
                                linea_fila)

    def validar_diagnostico_relacionado_3_sexo(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_3] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is not None:
                    if not encontrado[0][1] == 'A':
                        numero_id = ac_fila[Columnas.AC.obtener_numero_id]
                        encontrado2 =  self.dic_us.get(numero_id)

                        if encontrado2 is not None:
                            if not Generico().validar_sexo(encontrado2[USE.US.obtener_sexo], encontrado[1]):
                                self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                                    Columnas.AC.obtener_diagnostico_relacionado_3, linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_3, linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_3, linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_SEXO_INCORRECTO.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_3, linea_fila)

    def validar_diagnostico_relacionado_3_edad(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            if ac_fila[Columnas.AC.obtener_diagnostico_relacionado_3] != "":
                diagnostico_acfila = ac_fila[Columnas.AC.obtener_diagnostico_relacionado_3]
                encontrado =  self.cie10_dic.get(diagnostico_acfila)
                if encontrado is not None:
                    numero_id = ac_fila[Columnas.AC.obtener_numero_id]
                    encontrado2 =  self.dic_us.get(numero_id)

                    if encontrado2 is not None:
                        if not Generico().validar_edad_con_unidad_de_medida(encontrado2[USE.US.obtener_edad],
                                                                            encontrado2[
                                                                                USE.US.obtener_medida_de_edad],
                                                                            encontrado[2], encontrado[3]):
                            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                                Columnas.AC.obtener_diagnostico_relacionado_3, linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_3, linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_3, linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_EDAD_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_diagnostico_relacionado_3, linea=linea_fila)

    def validar_guion_numero_autorizacion(self, ac_fila, linea_fila):
        """
        :param ac_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico().validar_guiones_numero_autorizacion(ac_fila[Columnas.AC.obtener_numero_autorizacion],
                                                                  ac_fila[Columnas.AC.obtener_codigo_consulta]):
                self.detectar_error(TE.AC_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                    Columnas.AC.obtener_numero_autorizacion,
                                    linea=linea_fila)
        except AssertionError:
            self.detectar_error(TE.AC_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_numero_autorizacion,
                                linea=linea_fila)
        except ValueError:
            self.detectar_error(TE.AC_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_numero_autorizacion,
                                linea=linea_fila)
        except IndexError:
            self.detectar_error(TE.AC_NUMERO_AUTORIZACION_INCORRECTA.obtener_descripcion,
                                Columnas.AC.obtener_numero_autorizacion,
                                linea=linea_fila)

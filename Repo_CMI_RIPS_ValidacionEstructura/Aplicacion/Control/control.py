from Utilidades.Enumerados.Archivo.control_enum import ControlColumnasEnum as CT_columnas
from Dominio.Control.control import ModeloControl
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Utilidades.Enumerados.Ficheros.fichero_enum import FicheroEnum
from Aplicacion.Zip import zip


class ValidacionControl:
    nombre_archivo = 'CT'
    ct_model = ModeloControl.obtener_instancia()
    ct_model.asignar_valores([])
    metodos_de_validacion_a_ignorar = []
    lista_errores = []
    fichero_archivos = Generico().lista_fichero(FicheroEnum.TIPO_ARCHIVO.obtener_descripcion)
    codigo_habilitacion = ""

    def __init__(self):
        self.ct_model = ModeloControl.obtener_instancia()
        self.ct_model.asignar_valores(
            zip.ModeloZip.obtener_instancia().obtener_lista_registros_archivos()[self.nombre_archivo])
        if self.ct_model.obtener_instancia().obtener_lista():
            self.codigo_habilitacion = self.ct_model.obtener_instancia().obtener_lista()[0][
                CT_columnas.CT.obtener_codigo_prestador_posicion]
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.estado = False
        self.error_validar_columnas = False
        self.estado_codigo_validacion = False
        self.lista_errores_descripcion = Generico().lista_fichero(FicheroEnum.ERRORES.obtener_descripcion)

    def validar_estructura_ct(self):
        self.almacenar_archivos_presentes()
        self.ejecutar_validaciones_de_estructura()
        

    def ejecutar_validaciones_de_estructura(self):
        self.validar_columnas_genericos()
        self.validar_existencia_archivos_zip_en_ct()
        self.validar_codigo_habilitacion()
        if not self.error_validar_columnas:
            self.verificar_archivos_minimos(self.ct_model.obtener_instancia().obtener_archivos_presentes())
            self.verificar_prefijo_archivos()
            self.validar_total_de_datos()
            
            
    def validar_columnas_genericos(self):
        """
        Función para validar que la cantidad de columnas sea valido en el archivo
        :param ct_fila:
        :param linea_fila:
        :return:
        """
        try:
            for idx, ct_fila in enumerate(self.ct_model.obtener_instancia().obtener_lista()):
                if not Generico().validar_cantidad_columnas(ct_fila, self.ct_model.obtener_cantidad_columnas()):
                    self.error_validar_columnas = True
        except AssertionError:
            self.error_validar_columnas = True
        except ValueError:
            self.error_validar_columnas = True
        except IndexError:
            self.error_validar_columnas = True
        
    def almacenar_archivos_presentes(self):
        archivos_presentes = []
        for ct_fila in self.ct_model.obtener_instancia().obtener_lista():
            archivos_presentes.append(ct_fila[CT_columnas.CT.obtener_archivo_codigo_posicion])
        self.ct_model.obtener_instancia().asignar_archvos_presentes(archivos_presentes)

    def verificar_archivos_minimos(self, lista_archivos):
        """
        Método para validar que se contenga los archivos inicialmente requeridos
        :param lista_archivos:
        :return: Boolean
        """
        try:
            archivo_transacciones, archivo_usuarios, archivo_extra = False, False, False
            count=1
            linea=0
            for archivo in lista_archivos:
                prefijo_archivo = [archivo[:2].upper()]
                if prefijo_archivo == ['AF'] and prefijo_archivo in self.fichero_archivos:
                    archivo_transacciones = True
                if prefijo_archivo == ['US'] and prefijo_archivo in self.fichero_archivos:
                    archivo_usuarios = True
                if prefijo_archivo in self.fichero_archivos and prefijo_archivo != ['CT'] \
                        and prefijo_archivo != ['AF'] and prefijo_archivo != ['US']:
                    archivo_extra = True
            if archivo_transacciones and archivo_usuarios and archivo_extra:
                return True
            else:
                self.__detectar_error(TE.CT_ARCHIVOS_MINIMOS.obtener_descripcion)
        except AssertionError:
            self.__detectar_error(TE.CT_ARCHIVOS_MINIMOS.obtener_descripcion)
        except ValueError:
            self.__detectar_error(TE.CT_ARCHIVOS_MINIMOS.obtener_descripcion)
        except IndexError:
            self.__detectar_error(TE.CT_ARCHIVOS_MINIMOS.obtener_descripcion)

    def validar_longitud(self, ct_fila, linea_fila):
        """
        funcion que valida las longitudes de cada campo de cada registro
        :arg ct_fila: recibe una fila de registros del CT
        :arg self.ct_model.lista_posiciones_con_longitudes: lista con las posiciones y longitudes de cada columna pertenenciente al CT
        :return lista_errores o True
        """
        try:
            for campo in self.ct_model.obtener_lista_longitudes():
                valor_campo = ct_fila[campo[zip.posicion_campo]]
                posicion_campo = campo[zip.posicion_campo]
                if valor_campo != '':
                    if posicion_campo != CT_columnas.CT.obtener_codigo_prestador_posicion:
                        if not Generico().validar_longitud_campo(valor_campo, campo[zip.longitud_campo]):
                            self.__detectar_error(TE.CT_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                                  str(linea_fila), str(campo[zip.longitud_campo]))
                    else:
                        if not Generico().validar_longitud_campo(valor_campo, campo[zip.longitud_campo],
                                                                 campo[zip.longitud_campo]):
                            self.__detectar_error(TE.CT_LONGITUD_INVALIDA_CODIGO.obtener_descripcion, str(posicion_campo),
                                                  str(linea_fila), str(campo[zip.longitud_campo]))
        except AssertionError:
            self.__detectar_error(TE.CT_LONGITUD_INVALIDA_CODIGO.obtener_descripcion, str(posicion_campo),
                                  str(linea_fila), str(campo[zip.longitud_campo]))
        except ValueError:
            self.__detectar_error(TE.CT_LONGITUD_INVALIDA_CODIGO.obtener_descripcion, str(posicion_campo),
                                  str(linea_fila), str(campo[zip.longitud_campo]))
        except IndexError:
            self.__detectar_error(TE.CT_LONGITUD_INVALIDA_CODIGO.obtener_descripcion, str(posicion_campo),
                                  str(linea_fila), str(campo[zip.longitud_campo]))

    def validar_codigo_habilitacion(self):
        """
        funcion para validar que el codigo de habilitacion sea unico y este presente en todos los registros
        :arg ct_fila: recibe una fila de registros perteneciente ala rchivo CT
        :returns lista_errores o True
        """
        asignado=False
        codigo_lista=""
        try:
            linea_fila=1
            for campo in self.ct_model.obtener_lista():
                if campo[CT_columnas.CT.obtener_codigo_prestador_posicion]!="" :
                    if asignado ==False:
                        codigo_lista=campo[CT_columnas.CT.obtener_codigo_prestador_posicion]
                        asignado=True
                        
                    if not campo[
                        CT_columnas.CT.obtener_codigo_prestador_posicion] == codigo_lista:
                        self.__detectar_error(TE.CT_CODIGO_HABILITACION_INVALIDO.obtener_descripcion, linea=str(linea_fila))
                else:
                    if not self.estado_codigo_validacion:
                        self.__detectar_error(TE.CT_CODIGO_HABILITACION_INVALIDO.obtener_descripcion, linea=str(linea_fila))
                    self.estado_codigo_validacion = True
                linea_fila+=1
        except AssertionError:
            self.__detectar_error(TE.CT_CODIGO_HABILITACION_INVALIDO.obtener_descripcion, linea=str(linea_fila))
        except ValueError:
            self.__detectar_error(TE.CT_CODIGO_HABILITACION_INVALIDO.obtener_descripcion, linea=str(linea_fila))
        except IndexError:
            self.__detectar_error(TE.CT_CODIGO_HABILITACION_INVALIDO.obtener_descripcion, linea=str(linea_fila))

    def validar_numericos(self, ct_fila, linea_fila):
        """
        funcion para validar que un campo sea numerico y positivo en el registro
        :arg ct_fila: recibe una fila de registros perteneciente ala rchivo CT
        :returns lista_errores o True
        """
        try:
            if Generico().validar_es_numerico(
                    ct_fila[CT_columnas.CT.obtener_archivo_total_registros_posicion]) and ct_fila[
                CT_columnas.CT.obtener_archivo_total_registros_posicion] != '':
                return True
            else:
                self.__detectar_error(TE.CT_NUMERICO.obtener_descripcion, linea=str(linea_fila),
                                      posicion_columna=str(
                                          CT_columnas.CT.obtener_archivo_total_registros_posicion))
        except AssertionError:
            self.__detectar_error(TE.CT_NUMERICO.obtener_descripcion, linea=str(linea_fila),
                                  posicion_columna=str(
                                      CT_columnas.CT.obtener_archivo_total_registros_posicion))
        except ValueError:
            self.__detectar_error(TE.CT_NUMERICO.obtener_descripcion, linea=str(linea_fila),
                                  posicion_columna=str(
                                      CT_columnas.CT.obtener_archivo_total_registros_posicion))
        except IndexError:
            self.__detectar_error(TE.CT_NUMERICO.obtener_descripcion, linea=str(linea_fila),
                                  posicion_columna=str(
                                      CT_columnas.CT.obtener_archivo_total_registros_posicion))

    def validar_columnas(self, ct_fila,linea_fila):
        """
        Función para validar que la cantidad de columnas sea valido en el archivo
        :param ct_fila:
        :param linea_fila:
        :return:
        """
        
        try:
            if not Generico().validar_cantidad_columnas(ct_fila, self.ct_model.obtener_cantidad_columnas()):
                self.__detectar_error(TE.CT_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
                return True
            else:
                return False
        except AssertionError:
            self.__detectar_error(TE.CT_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            return True
        except ValueError:
            self.__detectar_error(TE.CT_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            
            return True
        except IndexError:
            self.__detectar_error(TE.CT_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            return True

    def validar_cantidad_columnas(self, ct_fila, linea_fila):
        """
        Función para validar que la cantidad de columnas sea valido en el registro
        :param ct_fila:
        :param linea_fila:
        :return:
        """
        error_validar_columnas=self.validar_columnas(ct_fila,linea_fila)
        if error_validar_columnas==False:
            if self.estado == False:
                self.verificar_campos_no_nulos(ct_fila, linea_fila)
                self.estado == True
            self.validar_longitud(ct_fila, linea_fila)
            self.validar_numericos(ct_fila, linea_fila)
            self.validar_existencia_de_los_registros_del_ct_en_zip(ct_fila, linea_fila)
            self.validar_formato_fecha(ct_fila, linea_fila)

    def validar_existencia_de_los_registros_del_ct_en_zip(self, ct_fila, linea_fila):
        """
        funcion para validar que los archivos que existan en el CT esten en el zip
        :arg codigo_archivo:nombre del archivo con indicador y codgo de remision
        :arg self.ct_model.nombres_archivos: almacena el nombre de los archivos presentes en los registros del CT
        :returns lista_errores o True
        """
        codigo = ct_fila[CT_columnas.CT.obtener_archivo_codigo_posicion]

        respuesta = False
        if ct_fila:
            respuesta = True
            if codigo.upper() + ".txt".upper() not in zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_archivos():
                respuesta = False
                self.__detectar_error(TE.CT_ARCHIVOS_EN_ZIP.obtener_descripcion, linea=str(linea_fila))
        return respuesta

    def validar_existencia_archivos_zip_en_ct(self):
        """
        funcion para validar que todos los archivos del zip esten en el ct
        :arg self.ct_model.nombres_archivos:nombre de los archivos presentes en el zip
        :arg self.ct_model.CT_archivos_presentes : almacena el nombre de los archivos presentes en los registros del CT
        :returns lista_errores o True
        """
        try:
            respuesta = True
            linea_fila = 1
            if zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_archivos() != [] and self.ct_model.obtener_instancia().obtener_archivos_presentes() != []:
                for ct in zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_archivos():
                    if ct[0:8] not in self.ct_model.obtener_instancia().obtener_archivos_presentes() and ct[
                                                                                                         0:2] != 'CT' and ct[
                                                                                                                          0:2] != 'US':
                        respuesta = False
                        self.__detectar_error(TE.CT_ARCHIVOS_ZIP_EN_CT.obtener_descripcion, linea=str(ct[0:8]))
                        linea_fila += 1
            return respuesta
        except AssertionError:
            self.__detectar_error(TE.CT_ARCHIVOS_ZIP_EN_CT.obtener_descripcion, linea=str(linea_fila))
        except ValueError:
            self.__detectar_error(TE.CT_ARCHIVOS_ZIP_EN_CT.obtener_descripcion, linea=str(linea_fila))
        except IndexError:
            self.__detectar_error(TE.CT_ARCHIVOS_ZIP_EN_CT.obtener_descripcion, linea=str(linea_fila))

    def validar_total_de_datos(self):
        """
        funcion que valida que la cantidad total de registros por archivos plasmada en el CT sea igual a la cantidad total
        de registros de cada archivo
        :returns lista_errores o True
        """
        try:
            respuesta = True
            if not self.error_validar_columnas:
                lista_archivos = zip.ModeloZip.obtener_instancia().obtener_lista_registros_archivos().keys()
                for archivo in self.ct_model.obtener_instancia().obtener_lista():
                    linea = 1
                    extension = ""
                    if archivo[CT_columnas.CT.obtener_archivo_codigo_posicion][0:2] in lista_archivos:
                        extension = archivo[CT_columnas.CT.obtener_archivo_codigo_posicion][0:2]
                        if archivo[CT_columnas.CT.obtener_archivo_total_registros_posicion] != "":
                            if Generico().validar_es_numerico(
                                    archivo[CT_columnas.CT.obtener_archivo_total_registros_posicion]):
                                if float(archivo[CT_columnas.CT.obtener_archivo_total_registros_posicion]) != len(
                                        zip.ModeloZip.obtener_instancia().obtener_lista_registros_archivos()[extension]):
                                    respuesta = False
                                    self.__detectar_error(TE.CT_TOTAL_DATOS.obtener_descripcion, linea=extension)
                    linea += 1
            return respuesta
        except AssertionError:
            self.__detectar_error(TE.CT_TOTAL_DATOS.obtener_descripcion, linea=extension)
        except ValueError:
            self.__detectar_error(TE.CT_TOTAL_DATOS.obtener_descripcion, linea=extension)
        except IndexError:
            self.__detectar_error(TE.CT_TOTAL_DATOS.obtener_descripcion, linea=extension)

    def verificar_prefijo_archivos(self):
        prefijo_archivo=""
        try:
            valores_archivos_enum = self.fichero_archivos

            respuesta = True
            for archivo in self.ct_model.obtener_instancia().obtener_archivos_presentes():
                linea = 0
                prefijo_archivo = [archivo[:2]]
                if prefijo_archivo not in valores_archivos_enum:
                    respuesta = False
                    self.__detectar_error(TE.CT_PREFIJO_ARCHIVO.obtener_descripcion, linea=prefijo_archivo)
                linea += 1
            return respuesta
        except AssertionError:
            self.__detectar_error(TE.CT_PREFIJO_ARCHIVO.obtener_descripcion, linea=prefijo_archivo)
        except ValueError:
            self.__detectar_error(TE.CT_PREFIJO_ARCHIVO.obtener_descripcion, linea=prefijo_archivo)
        except IndexError:
            self.__detectar_error(TE.CT_PREFIJO_ARCHIVO.obtener_descripcion, linea=prefijo_archivo)

    def generar_archivo_errores(self, lista_errores):
        """
        Genera el archivo de errores en base a la lista asignada
        :param lista_errores:
        :return:
        """
        Generico().crear_archivo_errores(lista_errores, self.nombre_archivo)

    def __detectar_error(self, tipo_error, posicion_columna=None, linea=None, longitud=None):
        """
        Método para obtener el error generado
        :param tipo_error:
        :param posicion_columna:
        :param linea:
        :param longitud:
        :return:
        """
        lista_fichero_errores = self.lista_errores_descripcion
        if posicion_columna is None and linea is None:
            self.lista_errores.append(
                Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error))
        else:
            if str(linea) is not None and posicion_columna is None and longitud is None:
                error = Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error)
                self.lista_errores.append(error.replace('$linea', str(linea)))
            else:
                if posicion_columna is not None and str(linea) is not None and longitud is None:
                    error = Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error,
                                                     int(posicion_columna))
                    error = error.replace('$posicion', str(int(posicion_columna) + 1))
                    error = error.replace('$linea', str(linea))
                    self.lista_errores.append(error)
                else:
                    if posicion_columna is not None and str(linea) is not None and longitud is not None:
                        error = Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error,
                                                         int(posicion_columna))
                        error = error.replace('$posicion', str(int(posicion_columna) + 1))
                        error = error.replace('$linea', str(linea))
                        error = error.replace('$longitud', longitud)
                        self.lista_errores.append(error)

    def verificar_campos_no_nulos(self, ct_fila, linea_fila):
        """
        Función para validar los campos nulos que existan en el registro sean validos
        :param ct_fila:
        :param linea_fila:
        :return:
        """
        try:
            for index, ct_campo in enumerate(ct_fila):
                if ct_campo == '':
                    self.__detectar_error(TE.CT_CAMPO_NULO.obtener_descripcion, index, linea_fila)
        except AssertionError:
            self.__detectar_error(TE.CT_CAMPO_NULO.obtener_descripcion, index, linea_fila)
        except ValueError:
            self.__detectar_error(TE.CT_CAMPO_NULO.obtener_descripcion, index, linea_fila)
        except IndexError:
            self.__detectar_error(TE.CT_CAMPO_NULO.obtener_descripcion, index, linea_fila)

    def validar_formato_fecha(self, ct_fila, linea_fila):
        """
        Función para validar que el formato de la fecha sea valido en el registro
        :param ct_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico().validar_formato_fecha(ct_fila[CT_columnas.CT.obtener_fecha_remision_posicion]):
                self.__detectar_error(TE.CT_FORMATO_FECHA.obtener_descripcion, linea=str(linea_fila),
                                      posicion_columna=str(
                                          CT_columnas.CT.obtener_fecha_remision_posicion))
        except AssertionError:
            self.__detectar_error(TE.CT_FORMATO_FECHA.obtener_descripcion, linea=str(linea_fila),
                                  posicion_columna=str(
                                      CT_columnas.CT.obtener_fecha_remision_posicion))
        except ValueError:
            self.__detectar_error(TE.CT_FORMATO_FECHA.obtener_descripcion, linea=str(linea_fila),
                                  posicion_columna=str(
                                      CT_columnas.CT.obtener_fecha_remision_posicion))
        except IndexError:
            self.__detectar_error(TE.CT_FORMATO_FECHA.obtener_descripcion, linea=str(linea_fila),
                                  posicion_columna=str(
                                      CT_columnas.CT.obtener_fecha_remision_posicion))
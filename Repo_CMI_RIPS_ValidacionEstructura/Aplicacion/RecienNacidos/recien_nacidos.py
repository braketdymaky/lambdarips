# -*- coding: utf-8 -*-
from Dominio.RecienNacidos.recien_nacidos import ModeloRecienNacidos
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Utilidades.Enumerados.Ficheros.fichero_enum import FicheroEnum
from Utilidades.Enumerados.Archivo.recien_nacidos_enum import RecienNacidosColumnaEnum as Columnas
from Aplicacion.Zip import zip


class ValidacionRecienNacidos:
    nombre_archivo = 'AN'
    an_model = ModeloRecienNacidos.obtener_instancia()
    an_model.asignar_valores([])
    metodos_de_validacion_a_ignorar = []
    lista_errores = []

    def __init__(self):
        self.an_model = ModeloRecienNacidos.obtener_instancia()
        self.an_model.asignar_valores(
            zip.ModeloZip.obtener_instancia().obtener_lista_registros_archivos()[self.nombre_archivo])
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.error_validar_columnas = False
        self.lista_errores_descripcion = Generico().lista_fichero(FicheroEnum.ERRORES.obtener_descripcion)

    def validar_columnas(self, an_fila, linea_fila):
        """
        Función para validar que la cantidad de columnas sea valido en el archivo
        :param an_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico().validar_cantidad_columnas(an_fila, self.an_model.obtener_cantidad_columnas()):
                self.__detectar_error(TE.AN_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
                return False
            else:
                return True
        except AssertionError:
            self.__detectar_error(TE.AN_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            return False
        except ValueError:
            self.__detectar_error(TE.AN_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            return False
        except IndexError:
            self.__detectar_error(TE.AN_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            return False

    def validar_cantidad_columnas(self, an_fila, linea_fila):
        """
       Función para validar que la cantidad de columnas sea valido en el registro
       :param an_fila:
       :param linea_fila:
       :return:
       """
        error_validar_columnas = self.validar_columnas(an_fila, linea_fila)
        if error_validar_columnas:
            self.validar_longitud(an_fila, linea_fila)
            self.validar_numerico(an_fila, linea_fila)
            self.verificar_campos_no_nulos(an_fila, linea_fila)
            self.validar_formato_fecha(an_fila, linea_fila)
            self.validar_formato_hora(an_fila, linea_fila)

    def validar_formato_fecha(self, an_fila, linea_fila):
        """
        Función para validar que el formato de la fecha sea valido en el registro
        :param an_fila:
        :param linea_fila:
        :return:
        """
        for campo in self.an_model.obtener_campos_fecha():
            if an_fila[campo] != '':
                try:
                    if not Generico().validar_formato_fecha(an_fila[campo]):
                        self.__detectar_error(TE.AN_FORMATO_FECHA.obtener_descripcion, str(campo), str(linea_fila))
                except AssertionError:
                    self.__detectar_error(TE.AN_FORMATO_FECHA.obtener_descripcion, str(campo), str(linea_fila))
                except ValueError:
                    self.__detectar_error(TE.AN_FORMATO_FECHA.obtener_descripcion, str(campo), str(linea_fila))
                except IndexError:
                    self.__detectar_error(TE.AN_FORMATO_FECHA.obtener_descripcion, str(campo), str(linea_fila))

    def validar_formato_hora(self, an_fila, linea_fila):
        """
        Función para validar que el formato de la hora sea valido en el registro
        :param an_fila:
        :param linea_fila:
        :return:
        """
        try:
            if not Generico().validar_formato_hora(an_fila[Columnas.AN.obtener_hora_nacimiento[zip.posicion_campo]]):
                self.__detectar_error(TE.AH_FORMATO_HORA.obtener_descripcion,
                                      posicion_columna=Columnas.AN.obtener_hora_nacimiento[zip.posicion_campo],
                                      linea=str(linea_fila))
        except AssertionError:
            self.__detectar_error(TE.AH_FORMATO_HORA.obtener_descripcion,
                                  posicion_columna=Columnas.AN.obtener_hora_nacimiento[zip.posicion_campo],
                                  linea=str(linea_fila))
        except ValueError:
            self.__detectar_error(TE.AH_FORMATO_HORA.obtener_descripcion,
                                  posicion_columna=Columnas.AN.obtener_hora_nacimiento[zip.posicion_campo],
                                  linea=str(linea_fila))
        except IndexError:
            self.__detectar_error(TE.AH_FORMATO_HORA.obtener_descripcion,
                                  posicion_columna=Columnas.AN.obtener_hora_nacimiento[zip.posicion_campo],
                                  linea=str(linea_fila))

        try:
            if an_fila[Columnas.AN.obtener_hora_de_muerte[zip.posicion_campo]] != '':
                if not Generico().validar_formato_hora(an_fila[Columnas.AN.obtener_hora_de_muerte[zip.posicion_campo]]):
                    self.__detectar_error(TE.AH_FORMATO_HORA.obtener_descripcion,
                                          posicion_columna=Columnas.AN.obtener_hora_de_muerte[zip.posicion_campo],
                                          linea=str(linea_fila))
        except AssertionError:
            self.__detectar_error(TE.AH_FORMATO_HORA.obtener_descripcion,
                                  posicion_columna=Columnas.AN.obtener_hora_de_muerte[zip.posicion_campo],
                                  linea=str(linea_fila))
        except ValueError:
            self.__detectar_error(TE.AH_FORMATO_HORA.obtener_descripcion,
                                  posicion_columna=Columnas.AN.obtener_hora_de_muerte[zip.posicion_campo],
                                  linea=str(linea_fila))
        except IndexError:
            self.__detectar_error(TE.AH_FORMATO_HORA.obtener_descripcion,
                                  posicion_columna=Columnas.AN.obtener_hora_de_muerte[zip.posicion_campo],
                                  linea=str(linea_fila))

    def validar_longitud(self, an_fila, linea_fila):
        """
        Función que valida la longitud de cada campo en cada registro
        :param an_fila:
        :param linea_fila:
        :return:
        """
        for campo in self.an_model.obtener_lista_longitudes():
            valor_campo = an_fila[campo[zip.posicion_campo]]
            posicion_campo = campo[zip.posicion_campo]
            try:
                if valor_campo != '':
                    if not Generico().validar_longitud_campo(valor_campo, campo[zip.longitud_campo]):
                        self.__detectar_error(TE.AN_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                              str(linea_fila), str(campo[zip.longitud_campo]))
            except AssertionError:
                self.__detectar_error(TE.AN_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                      str(linea_fila), str(campo[zip.longitud_campo]))
            except ValueError:
                self.__detectar_error(TE.AN_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                      str(linea_fila), str(campo[zip.longitud_campo]))
            except IndexError:
                self.__detectar_error(TE.AN_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                      str(linea_fila), str(campo[zip.longitud_campo]))

    def validar_numerico(self, an_fila, linea_fila):
        """
        Función para validar que un campo sea numerico y positivo en el registro
        :param an_fila:
        :param linea_fila:
        :return:
        """
        for campo in self.an_model.obtener_campos_numericos():
            valor_campo = an_fila[campo]
            try:
                if valor_campo != '':
                    if not Generico().validar_es_numerico(an_fila[campo]):
                        self.__detectar_error(TE.AN_NUMERICO.obtener_descripcion,
                                              str(campo), str(linea_fila))
            except AssertionError:
                self.__detectar_error(TE.AN_NUMERICO.obtener_descripcion,
                                      str(campo), str(linea_fila))
            except ValueError:
                self.__detectar_error(TE.AN_NUMERICO.obtener_descripcion,
                                      str(campo), str(linea_fila))
            except IndexError:
                self.__detectar_error(TE.AN_NUMERICO.obtener_descripcion,
                                      str(campo), str(linea_fila))

    def verificar_campos_no_nulos(self, an_fila, linea_fila):
        """
        Función para validar los campos nulos que existan en el registro sean validos
        :param an_fila:
        :param linea_fila:
        :return:
        """
        for index, ac_campo in enumerate(an_fila):
            try:
                if index not in self.an_model.obtener_campos_opcionales():
                    if ac_campo == '':
                        self.__detectar_error(TE.AN_CAMPO_NULO.obtener_descripcion, index, linea_fila)
            except AssertionError:
                self.__detectar_error(TE.AN_CAMPO_NULO.obtener_descripcion, index, linea_fila)
            except ValueError:
                self.__detectar_error(TE.AN_CAMPO_NULO.obtener_descripcion, index, linea_fila)
            except IndexError:
                self.__detectar_error(TE.AN_CAMPO_NULO.obtener_descripcion, index, linea_fila)

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
            self.lista_errores.append(Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error))
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

# -*- coding: utf-8 -*-
from Dominio.Procedimientos.procedimientos import ModeloProcedimientos
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Utilidades.Enumerados.Ficheros.fichero_enum import FicheroEnum
from Utilidades.Enumerados.Archivo.procedimientos_enum import ProcedimientosColumnasEnum as Columnas
from Aplicacion.Zip import zip
from time import time

class ValidacionProcedimientos:
    nombre_archivo = 'AP'
    ap_model = ModeloProcedimientos.obtener_instancia()
    ap_model.asignar_valores([])
    metodos_de_validacion_a_ignorar = []
    lista_errores = []

    def __init__(self):
        self.ap_model = ModeloProcedimientos.obtener_instancia()
        self.ap_model.asignar_valores(zip.ModeloZip.obtener_instancia().obtener_lista_registros_archivos()[self.nombre_archivo])
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.error_validar_columnas = False
        self.lista_errores_descripcion = Generico().lista_fichero(FicheroEnum.ERRORES.obtener_descripcion)
    
    def validar_columnas(self,ap_fila,linea_fila):
        """
        Función para validar que la cantidad de columnas sea valido en el archivo
        :param ct_fila:
        :param linea_fila:
        :return:
        """
        # inicio = time()
        try:
            if not Generico().validar_cantidad_columnas(ap_fila, self.ap_model.obtener_cantidad_columnas()):
                self.__detectar_error(TE.AP_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
                return False
            else:
                return True
        except AssertionError:
            self.__detectar_error(TE.AP_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            return False
        except ValueError:
            self.__detectar_error(TE.AP_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            return False
        except IndexError:
            self.__detectar_error(TE.AP_CANTIDAD_CAMPOS.obtener_descripcion, linea=linea_fila)
            return False
        # fin = time()
        # print("AP validar columnas: " + str(fin-inicio))

    def validar_cantidad_columnas(self, ap_fila, linea_fila):
        """
        Función para validar que la cantidad de columnas sea valido en el registro
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        inicio = time()
        error_validar_columnas = self.validar_columnas(ap_fila,linea_fila)
        if  error_validar_columnas != False:
            self.validar_longitud(ap_fila, linea_fila)
            self.validar_numerico(ap_fila, linea_fila)
            self.verificar_campos_no_nulos(ap_fila, linea_fila)
            self.validar_formato_fecha(ap_fila, linea_fila)
        fin = time()      
        

    def validar_longitud(self, ap_fila, linea_fila):
        """
        Función que valida la longitud de cada campo en cada registro
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        #inicio = time()
        try:
            for campo in self.ap_model.obtener_lista_longitudes():
                valor_campo = ap_fila[campo[zip.posicion_campo]]
                posicion_campo = campo[zip.posicion_campo]
                if valor_campo != '':
                    if not Generico().validar_longitud_campo(valor_campo, campo[zip.longitud_campo]):
                        self.__detectar_error(TE.AP_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                              str(linea_fila), str(campo[zip.longitud_campo]))
        except AssertionError:
            self.__detectar_error(TE.AP_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                              str(linea_fila), str(campo[zip.longitud_campo]))
        except ValueError:
            self.__detectar_error(TE.AP_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                              str(linea_fila), str(campo[zip.longitud_campo]))
        except IndexError:
            self.__detectar_error(TE.AP_LONGITUD_INVALIDA.obtener_descripcion, str(posicion_campo),
                                              str(linea_fila), str(campo[zip.longitud_campo]))
        #fin = time()
        #print("AP validar longitud: " + str(fin-inicio))

    def validar_numerico(self, ap_fila, linea_fila):
        """
        Función para validar que un campo sea numerico y positivo en el registro
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        #inicio = time()
        try:
            for campo in self.ap_model.obtener_campos_numericos():
                valor_campo = ap_fila[campo]
                if valor_campo != '':
                    if not Generico().validar_es_numerico(ap_fila[campo]):
                        self.__detectar_error(TE.AP_NUMERICO.obtener_descripcion,
                                              str(campo), str(linea_fila))
        except AssertionError:
            self.__detectar_error(TE.AP_NUMERICO.obtener_descripcion,
                                              str(campo), str(linea_fila))
        except ValueError:
            self.__detectar_error(TE.AP_NUMERICO.obtener_descripcion,
                                              str(campo), str(linea_fila))
        except IndexError:
            self.__detectar_error(TE.AP_NUMERICO.obtener_descripcion,
                                              str(campo), str(linea_fila))
        #fin = time()
        #print("AP validar numericos: " + str(fin-inicio))                                              

    def verificar_campos_no_nulos(self, ap_fila, linea_fila):
        """
        Función para validar los campos nulos que existan en el registro sean validos
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        #inicio = time()
        try:
            for index, ac_campo in enumerate(ap_fila):
                if index not in self.ap_model.obtener_campos_opcionales():
                    if ac_campo == '':
                        self.__detectar_error(TE.AC_CAMPO_NULO.obtener_descripcion, index, linea_fila)
        except AssertionError:
            self.__detectar_error(TE.AC_CAMPO_NULO.obtener_descripcion, index, linea_fila)
        except ValueError:
            self.__detectar_error(TE.AC_CAMPO_NULO.obtener_descripcion, index, linea_fila)
        except IndexError:
            self.__detectar_error(TE.AC_CAMPO_NULO.obtener_descripcion, index, linea_fila)
        #fin = time()
        #print("AP validar campos no nulos: " + str(fin-inicio))
    
        
    def validar_formato_fecha(self, ap_fila, linea_fila):
        """
        Función para validar que el formato de la fecha sea valido en el registro
        :param ap_fila:
        :param linea_fila:
        :return:
        """
        #inicio = time()
        try:
            for campo in self.ap_model.obtener_campos_fecha():
                if campo != '':
                    if not Generico().validar_formato_fecha(ap_fila[campo]):
                        self.__detectar_error(TE.AP_FORMATO_FECHA.obtener_descripcion, str(campo), str(linea_fila))
        except AssertionError:
            self.__detectar_error(TE.AP_FORMATO_FECHA.obtener_descripcion, str(campo), str(linea_fila))
        except ValueError:
            self.__detectar_error(TE.AP_FORMATO_FECHA.obtener_descripcion, str(campo), str(linea_fila))
        except IndexError:
            self.__detectar_error(TE.AP_FORMATO_FECHA.obtener_descripcion, str(campo))          
        #fin = time()
        #print("AP validar formato fecha: " + str(fin-inicio))
            

    def generar_archivo_errores(self, lista_errores):
        """
        Genera el archivo de errores en base a la lista asignada
        :param lista_errores:
        :return:
        """
        #inicio = time()
        Generico().crear_archivo_errores(lista_errores, self.nombre_archivo)
        #fin = time()
        #print("AP generar archivo errores: " + str(fin-inicio))
        
        
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

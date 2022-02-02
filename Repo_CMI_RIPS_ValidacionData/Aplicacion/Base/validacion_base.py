# -*- coding: utf-8 -*-
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico
from Utilidades.Enumerados.Ficheros.fichero_enum import FicheroEnum
from Dominio.Fichero.fichero import ModeloFichero
from time import time

class ValidacionBase:
    codigo_habilitacion = ''
    nombre_archivo = ''
    model = None
    model_fichero = ModeloFichero.obtener_instancia()
    metodos_de_validacion_a_ignorar = []
    lista_errores = []
    errores_validaciones=[]

    def __init__(self):
        self.errores_validaciones = self.model_fichero.obtener_errores()

    def generar_archivo_errores(self, lista_errores):
        """
        Genera el archivo de errores en base a la lista asignada
        :param lista_errores:
        :return:
        """
        Generico().crear_archivo_errores(lista_errores, self.nombre_archivo)

    def detectar_error(self, tipo_error, posicion_columna=None, linea=None,archivo=None):
        """
        Método para obtener el error generado
        :param tipo_error:
        :param posicion_columna:
        :param linea:
        :return:
        """
        lista_fichero_errores = self.errores_validaciones
        if posicion_columna is None and linea is None:
            error = Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error)
            if error is not None and error != "":
                self.lista_errores.append(error)
            else:
                error = "No se encontró descripción del error asociado para la validación fallida, Error en el archivo"
                self.lista_errores.append(error)
        else:
            if str(linea) is not None and posicion_columna is None:
                error = Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error)
                if error is not None and error != "":
                    self.lista_errores.append(error.replace('$linea', str(linea)))
                else:
                    error = "No se encontró descripción del error asociado para la validación fallida, el Error se presento en la linea "+str(linea)
                    self.lista_errores.append(error)

            else:
                if posicion_columna is not None and str(linea) is not None and str(archivo) is None:
                    error = Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error,
                                                     int(posicion_columna))
                    if error is not None and error != "":

                        error = error.replace('$posicion', str(int(posicion_columna) + 1))
                        error = error.replace('$linea', str(linea))
                        self.lista_errores.append(error)
                    else:
                        error = "Error en la linea " + str(linea) + " columna: " + str(
                            posicion_columna) + " de tipo: " + tipo_error + " No se encontró descripción del error asociado para la validación fallida."
                        self.lista_errores.append(error)
                else:
                    if posicion_columna is not None and str(linea) is not None and str(archivo) is not None:
                        error = Generico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error,
                                                        int(posicion_columna))
                    if error is not None and error != "":
                        error = error.replace('$posicion', str(int(posicion_columna) + 1))
                        error = error.replace('$linea', str(linea))
                        error = error.replace('$archivo', str(archivo))
                        self.lista_errores.append(error)
                    else:
                        error = "Error en la linea " + str(linea) + " columna: " + str(posicion_columna) + " de tipo: " + tipo_error + " No se encontró descripción del error asociado para la validación fallida."
                        self.lista_errores.append(error)



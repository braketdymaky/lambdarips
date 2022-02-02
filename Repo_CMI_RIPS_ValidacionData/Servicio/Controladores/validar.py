from Aplicacion.Dinamismo.codigos_validaciones import ValidacionDinamismo
from threading import *
import os
import zipfile
from os.path import basename
from multiprocessing import Process, Pipe

class Validador:
    nombre_zip = ""

    def __init__(self, zip, nombre_zip, id_cliente, listas, dinamismo,codigo_habilitacion,codigo_prestador):
        self.archivo_zip = zip
        self.nombre_zip = nombre_zip
        self.id_cliente = id_cliente
        self.listas = listas
        self.dinamismo = dinamismo
        self.codigo_habilitacion=codigo_habilitacion
        self.codigo_prestador = codigo_prestador
        self.validaciones_archivos = ValidacionDinamismo(self.archivo_zip, self.id_cliente, self.listas, self.dinamismo,self.codigo_habilitacion,self.codigo_prestador)


    def validar_archivos(self):
        funciones = [
            self.funciones_obligatorias,
            self.validaciones_archivos.dinamismos_am,
            self.validaciones_archivos.dinamismos_an,
            self.validaciones_archivos.dinamismos_at,
            self.validaciones_archivos.dinamismos_ap,
            self.validaciones_archivos.dinamismos_ac,
            self.validaciones_archivos.dinamismos_ah,
            self.validaciones_archivos.dinamismos_us,
            self.validaciones_archivos.dinamismos_au
            ]
        self.ejecutar_hilos(funciones)

    def crear_zip(self):
        array_archivos = os.listdir('/tmp/')
        if array_archivos:
            nombre_zip = "/tmp/Errores" + self.nombre_zip
            zip_errores = zipfile.ZipFile(nombre_zip, "w")
            try:
                for item in array_archivos:
                    zip_errores.write("/tmp/" + item, basename(item), compress_type=zipfile.ZIP_DEFLATED)
            finally:
                zip_errores.close()
            return zip_errores
        else:
            return 'ok'

    def ejecutar_hilos(self,funciones):
        processes = []
        for funcion in funciones:
            process = Process(target=funcion)
            processes.append(process)

        for process in processes:
            process.start()

        for process in processes:
            process.join()

    def funciones_obligatorias(self):
            self.validaciones_archivos.dinamismos_ct()
            self.validaciones_archivos.dinamismos_ad()
            self.validaciones_archivos.dinamismos_af()


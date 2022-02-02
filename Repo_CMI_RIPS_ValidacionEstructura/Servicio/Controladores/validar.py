from Aplicacion.Zip import zip
from Aplicacion.Dinamismo.codigos_validaciones import CodigosValidaciones
from threading import *
import os
import zipfile
from os.path import basename
from multiprocessing import Process, Pipe


class Validador:
    archivo_zip = []
    nombre_zip = ""

    def __init__(self, zip, nombre_zip):
        self.archivo_zip = zip
        self.nombre_zip = nombre_zip
        
    def validar_archivos(self, codigo_prestador, dinamismo):
        validaciones_zip = zip.ValidacionZip()
        zip_valido = validaciones_zip.validar_archivo_zip(self.archivo_zip, self.nombre_zip)
        if self.archivo_zip.namelist() and zip_valido:
            self.validaciones_archivos = CodigosValidaciones(codigo_prestador, dinamismo)
            funciones = [
            self.funciones_obligatorias,
            self.validaciones_archivos.dinamismos_am,
            self.validaciones_archivos.dinamismos_at,
            self.validaciones_archivos.dinamismos_an,
            self.validaciones_archivos.dinamismos_ap,
            self.validaciones_archivos.dinamismos_ac,
            self.validaciones_archivos.dinamismos_ah,
            self.validaciones_archivos.dinamismos_us,
            self.validaciones_archivos.dinamismos_au
            ]
            self.ejecutar_hilos(funciones)
            
            return True
        else:
            return False
        

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
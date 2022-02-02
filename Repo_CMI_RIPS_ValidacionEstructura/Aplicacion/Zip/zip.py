from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico
from Utilidades.Enumerados.Ficheros.fichero_enum import FicheroEnum
from Dominio.Zip.zip import ModeloZip

posicion_campo = 0
longitud_campo = 1


class ValidacionZip:
    lista_errores = []
    lista_archivos_existentes = []
    lista_archivos_presentes = []
    listas_archivos_registros = {}
    nombre_archivo = 'ZIP'
    modelo = ModeloZip()
    fichero_archivos = ValidacionGenerico().lista_fichero(FicheroEnum.TIPO_ARCHIVO.obtener_descripcion)

    def __init__(self):
        self.lista_errores = []
        self.lista_archivos_existentes = []
        self.lista_archivos_presentes = []
        self.lista_errores_descripcion = ValidacionGenerico().lista_fichero(FicheroEnum.ERRORES.obtener_descripcion)
        self.listas_archivos_registros = {'AC': [], 'AF': [], 'AH': [], 'AM': [], 'AP': [], 'AT': [],
                                          'AU': [], 'CT': [], 'US': [], 'AD': [], 'AN': []}
                                    

    def validar_archivo_zip(self, direccion_archivo, nombre_archivo):
        """
        Método para realizar paso a paso las validaciones generales del archivo .zip
        :param nombre_archivo:
        :param direccion_archivo:
        :return:
        """
        
        carpeta=False
        if nombre_archivo != '':
            if self.__validar_extension(nombre_archivo):
                self.modelo.obtener_instancia().asignar_valores(direccion_archivo, nombre_archivo)
                archivo_zip = self.modelo.obtener_instancia()
                self.__crear_lista_por_archivo(direccion_archivo)

                if direccion_archivo.namelist():
                    for name in direccion_archivo.namelist():
                        if "/" in name:
                            carpeta=True
                            
                    if not carpeta:
                        archivo_zip.obtener_instancia().asignar_lista_registros_archivos(self.listas_archivos_registros)
                    else:
                        self.__detectar_error(TipoErrorEnum.ZIP_CARPETA.obtener_descripcion)
                else:
                    self.__detectar_error(TipoErrorEnum.ZIP_VACIO.obtener_descripcion)
                
                if not carpeta:
                    if not self.__validar_longitud_nombre(nombre_archivo):
                        self.__detectar_error(TipoErrorEnum.ZIP_LONGITUD_INVALIDA.obtener_descripcion,
                                              nombre_archivo)
    
                    if not self.__validar_numerico(nombre_archivo):
                        self.__detectar_error(TipoErrorEnum.ZIP_NOMBRE_NUMERICO.obtener_descripcion,
                                              nombre_archivo)
    
                    if not self.__validar_indicadores_archivos(archivo_zip.obtener_lista_archivos()):
                        lista_duplicados = self.__obtener_lista_archivos_duplicados(
                            archivo_zip.obtener_lista_archivos())
                        lista_duplicados.sort()
                        self.__detectar_error(TipoErrorEnum.ZIP_ARCHIVO_DUPLICADO.obtener_descripcion,
                                              ', '.join(str(p) for p in lista_duplicados))
    
                    if not self.__comparar_numero_remision(archivo_zip.obtener_lista_archivos(),
                                                           archivo_zip.obtener_nombre()):
                        lista_error_remision = self.__obtener_lista_remision_incorrecta(
                            archivo_zip.obtener_lista_archivos(), archivo_zip.obtener_nombre())
                        for error in lista_error_remision:
                            self.__detectar_error(TipoErrorEnum.ZIP_NUMERO_REMISION.obtener_descripcion, error)
                    if not self.__validar_cantidad_archivos(archivo_zip.obtener_lista_archivos()):
                        lista_error_cantidad = self.__obtener_archivos_faltantes(
                            archivo_zip.obtener_lista_archivos())
                        for error in lista_error_cantidad:
                            self.__detectar_error(
                                TipoErrorEnum.ZIP_ARCHIVO_NO_ENCONTRADO.obtener_descripcion, error)
            else:
                self.__detectar_error(TipoErrorEnum.ZIP_EXTENSION_INVALIDA.obtener_descripcion)
        else:
            self.__detectar_error(TipoErrorEnum.ZIP_NO_EXISTE.obtener_descripcion)

        if self.lista_errores:
            ValidacionGenerico().crear_archivo_errores(self.lista_errores, self.nombre_archivo)
            return False
        else:
            return True

    def __detectar_error(self, tipo_error, variable=None):
        """
        Método para obtener el error generado
        :param tipo_error:
        :param variable:
        :return:
        """
        lista_fichero_errores = self.lista_errores_descripcion
        if variable is None:
            self.lista_errores.append(
                ValidacionGenerico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error))
        else:
            self.lista_errores.append(
                ValidacionGenerico().obtener_error(lista_fichero_errores, self.nombre_archivo, tipo_error).replace(
                    '$variable', variable))

    def __validar_extension(self, direccion_archivo):
        """
        Método validar la extensión del archivo comprimido
        :param direccion_archivo:
        :return: Boolean
        """
        numero = len(direccion_archivo)
        if direccion_archivo[numero - 4:numero].upper() == '.zip'.upper():
            return True
        else:
            return False

    def __validar_longitud_nombre(self, nombre_zip, longitud_maxima=6, longitud_minima=6):
        """
        Método para validar el nombre del archivo .zip
        :param nombre_zip:
        :param longitud_maxima:
        :param longitud_minima:
        :return: ValidacionGenerico.validar_longitud_campo(nombre_zip, longitud_maxima,
                                                        longitud_minima)
        """
        nombre_zip = nombre_zip.replace('.zip', '')
        return ValidacionGenerico().validar_longitud_campo(nombre_zip, longitud_maxima,
                                                           longitud_minima)

    def __validar_numerico(self, nombre_zip):
        """
        Método para validar el nombre del .zip como número de remisión
        :param nombre_zip:
        :return: ValidacionGenerico.validar_es_numerico(nombre_zip)
        """
        nombre_zip = nombre_zip.replace('.zip', '')
        return ValidacionGenerico().validar_es_numerico(nombre_zip)

    def __comparar_numero_remision(self, lista_archivos, nombre_archivo):
        """
        Método para comparar el número de remisión del comprimido con los archivos internos y su nombre
        :param lista_archivos:
        :param nombre_archivo:
        :return: validado
        """
        validado = True
        remision_zip = nombre_archivo.replace('.zip', '')
        for item in lista_archivos:
            remision_archivo = item[2:].lower().replace('.txt', '')
            if remision_zip != remision_archivo:
                validado = False
        return validado

    def __obtener_lista_remision_incorrecta(self, lista_archivos, nombre_archivo):
        """
        Método para comparar el número de remisión del comprimido con los archivos internos y su nombre
        :param lista_archivos:
        :param nombre_archivo:
        :return: lista_error_remision
        """
        lista_error_remision = []
        remision_zip = nombre_archivo.replace('.zip', '')
        for archivo in lista_archivos:
            remision_archivo = archivo[2:].lower().replace('.txt', '')
            if remision_zip != remision_archivo:
                lista_error_remision.append(archivo)
        return lista_error_remision

    def __validar_indicadores_archivos(self, lista_archivos):
        """
        Método para validar el nombre y la unicidad de los tipos de archivos
        :param lista_archivos:
        :return:
        """
        for enum in self.fichero_archivos:
            unico_archivo = 0
            for archivo in lista_archivos:
                prefijo_archivo = archivo[:2]
                if enum == prefijo_archivo:
                    unico_archivo += 1
                if unico_archivo > 1:
                    return False
        return True

    def __obtener_lista_archivos_duplicados(self, lista_archivos):
        """
        Método para obtener la lista de archivos duplicados dado que se presente el caso
        :param lista_archivos:
        :return: lista_duplicados
        """
        lista_duplicados = []
        for archivo in lista_archivos:
            unico_archivo = 0
            prefijo_archivo = archivo[:2]
            for item in lista_archivos:
                prefijo_item = item[:2]
                if prefijo_item == prefijo_archivo:
                    unico_archivo += 1
                if unico_archivo > 1:
                    lista_duplicados.append(archivo)
                    break
        return lista_duplicados

    def __validar_cantidad_archivos(self, lista_archivos):
        """
        Método para validar que se contenga los archivos inicialmente requeridos
        :param lista_archivos:
        :return: Boolean
        """
        archivo_control, archivo_transacciones, archivo_usuarios, archivo_extra = False, False, False, False
        for archivo in lista_archivos:
            prefijo_archivo = [archivo[:2].upper()]
            if prefijo_archivo == ['CT'] and prefijo_archivo in self.fichero_archivos:
                archivo_control = True
            if prefijo_archivo == ['AF'] and prefijo_archivo in self.fichero_archivos:
                archivo_transacciones = True
            if prefijo_archivo == ['US'] and prefijo_archivo in self.fichero_archivos:
                archivo_usuarios = True
            if prefijo_archivo in self.fichero_archivos and prefijo_archivo != ['CT'] \
                    and prefijo_archivo != ['AF'] and prefijo_archivo != ['US']:
                archivo_extra = True
        if archivo_control and archivo_transacciones and archivo_usuarios and archivo_extra:
            return True
        else:
            return False

    def __obtener_archivos_faltantes(self, lista_archivos):
        """
         Método para obtener archivos faltantes en el archivo comprimido
        :param lista_archivos:
        :return: lista_archivos_faltantes
        """
        lista_archivos_faltantes = []
        archivo_control, archivo_transacciones, archivo_usuarios, archivo_extra = False, False, False, False
        for archivo in lista_archivos:
            prefijo_archivo = [archivo[:2].upper()]
            if prefijo_archivo == ['CT'] and prefijo_archivo in self.fichero_archivos:
                archivo_control = True
            if prefijo_archivo == ['AF'] and prefijo_archivo in self.fichero_archivos:
                archivo_transacciones = True
            if prefijo_archivo == ['US'] and prefijo_archivo in self.fichero_archivos:
                archivo_usuarios = True
            if prefijo_archivo in self.fichero_archivos and prefijo_archivo != ['CT'] \
                    and prefijo_archivo != ['AF'] and prefijo_archivo != ['US']:
                archivo_extra = True
        if not archivo_control:
            lista_archivos_faltantes.append('control CT')
        if not archivo_transacciones:
            lista_archivos_faltantes.append('transacción AF')
        if not archivo_usuarios:
            lista_archivos_faltantes.append('usuarios US')
        if not archivo_extra:
            lista_archivos_faltantes.append('servicio')
        return lista_archivos_faltantes

    def __asignar_registros_a_lista(self, direccion_archivo):
        """
        Método para asignar registro a una lista
        :param direccion_archivo:
        :return: nueva_lista
        """
        nueva_lista = []
        archivo = open(direccion_archivo, "r")
        for registro in archivo:
            nueva_lista.append(registro)
        archivo.close()
        return nueva_lista

    def __crear_lista_por_archivo(self, direccion_archivo):
        """
        Método para generar listas por cada tipo de archivo
        :param direccion_archivo:
        :return:
        """
        self.lista_archivos_existentes = direccion_archivo.namelist()
        for archivo in direccion_archivo.namelist():
            self.lista_archivos_presentes.append(archivo)
            archivo_texto = direccion_archivo.open(archivo, 'r').name
            archivo_base = direccion_archivo.open(archivo_texto, 'r')
            archivo_leido = archivo_base.read()
            registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
            for item in registros:
                if item != "" and archivo != "" and archivo != None:
                    if [archivo[:2]] in self.fichero_archivos:
                        self.listas_archivos_registros[archivo[:2]].append(item.split(","))
            archivo_base.close()

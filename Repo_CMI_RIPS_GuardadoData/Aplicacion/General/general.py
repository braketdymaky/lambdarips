from Aplicacion.Pdf.pdf import GenerarPdf
class General:

    def generar_lista_us(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'US':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_af(self, direccion_archivo):
        lista = []
        lista_facturas = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AF':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                for item in lista:
                    lista_facturas.append([item[4], item[16]])
                GenerarPdf.obtener_instancia().asignar_lista_facturas(lista_facturas)
                GenerarPdf.obtener_instancia().asignar_numero_nit(lista[0][3])
                GenerarPdf.obtener_instancia().asignar_nombre_prestador(lista[0][1])
                archivo_base.close()
                return lista

    def generar_lista_ac(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AC':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_ah(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AH':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_am(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AM':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_ap(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AP':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_at(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AT':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_au(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AU':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_ct(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'CT':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_an(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AN':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

    def generar_lista_ad(self, direccion_archivo):
        lista = []
        for archivo in direccion_archivo.namelist():
            if archivo[:2].upper() == 'AD':
                archivo_texto = direccion_archivo.open(archivo, 'r').name
                archivo_base = direccion_archivo.open(archivo_texto, 'r')
                archivo_leido = archivo_base.read()
                registros = archivo_leido.decode('UTF-8-sig', errors='ignore').split("\r\n")
                for item in registros:
                    if item:
                        lista.append(item.split(","))
                archivo_base.close()
                return lista

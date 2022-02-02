from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from textwrap import wrap
import base64
import locale
import os.path
import io
import zipfile
import pickle
import boto3
import os

class GenerarPdf:
    __w, __h = A4
    __numero_paginas = 1
    __factura_posicion = 260
    __valor_posicion = 260
    __instance = None
    __nombre_rips = ''
    __nombre_prestador = ''
    __numero_nit = ''
    __fecha_registro = ''
    __lista_factura = []
    numero_de_lineas= 0
    _tipos_archivos=[]
    _posicion_tabla=0
    _tabla_pos=0
    __ct=[]
    
    @classmethod
    def obtener_instancia(cls):
        """
        obtener la instancia de la clase
        :return:
        """
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def obtener_nombre_rips(self):
        return self.__nombre_rips

    def asignar_nombre_rips(self, nombre_rips):
        self.__nombre_rips = nombre_rips

    def obtener_numero_nit(self):
        return self.__numero_nit

    def asignar_numero_nit(self, numero_nit):
        self.__numero_nit = numero_nit

    def obtener_fecha_registro(self):
        return self.__fecha_registro

    def asignar_fecha_registro(self, fecha_registro):
        self.__fecha_registro = fecha_registro

    def obtener_lista_facturas(self):
        return self.__lista_factura

    def asignar_lista_facturas(self, lista_factura):
        self.__lista_factura = lista_factura

    def obtener_nombre_prestador(self):
        return self.__nombre_prestador

    def asignar_nombre_prestador(self, nombre_prestador):
        self.__nombre_prestador = nombre_prestador

    def obtener_ct(self):
        return self.__ct

    def asignar_asignar_ct(self, ct):
        self.__ct = ct


    def coord(self, x, y, unit=1):
        x, y = x * unit, self.__h - y * unit
        return x, y

    def agregar_titulos_pdf(self, pdf,eapb,ct,estado):
        self._tipos_archivos=[]
        bucket = os.environ['bucket']
        key = 'images/logos.zip'

        zipp = self.obtener_zip(bucket, key)
        if zipp is not None:
            with io.BytesIO(zipp.read()) as tf:
                tf.seek(0)
                fantasy_zip = zipfile.ZipFile(tf)
                fantasy_zip.extractall('/tmp/')

        if eapb == "EPS005":
            pdf.drawImage('/tmp/Logos_Arus_Sanitas_v2.jpg',35, 780, 480, 40)
        elif eapb == "EPS010":
            pdf.drawImage('/tmp/Logos_Arus_Sura_v2.jpg',35, 780, 480, 40)
        else:
            pdf.drawImage('/tmp/Logo_Arus_v2.jpg',35, 780, 480, 40)

        # Agregar titulo PDF
        texto_titulo = pdf.beginText(65, self.__h - 100)
        texto_titulo.setFont("Helvetica-Bold", 18)
        texto_titulo.textLine(
            "RIPS #" + self.obtener_instancia().obtener_nombre_rips() + " fue validado y cargado exitosamente")
        pdf.drawText(texto_titulo)

        # Agregar subtitulo - Prestador
        prestador_subtitulo = pdf.beginText(70, self.__h - 120)
        prestador_subtitulo.setFont("Helvetica-Bold", 14)
        prestador_subtitulo.textLine("Prestador:")
        pdf.drawText(prestador_subtitulo)

        # Agregar subtitulo - Nit
        nit_ips = pdf.beginText(70, self.__h - 145)
        nit_ips.setFont("Helvetica-Bold", 14)
        nit_ips.textLine("NIT:")
        pdf.drawText(nit_ips)

        # Agregar subtitulo - Fecha
        fecha_registro = pdf.beginText(70, self.__h - 170)
        fecha_registro.setFont("Helvetica-Bold", 14)
        fecha_registro.textLine("Fecha de carga:")
        pdf.drawText(fecha_registro)



        if estado==0:
            # Agregar titulo registro de archivos
            documentos_titulo = pdf.beginText(210, self.__h - 210)
            documentos_titulo.setFont("Helvetica-Bold", 16)
            documentos_titulo.textLine("Registro de Archivos")
            pdf.drawText(documentos_titulo)

            self.generar_tabla(pdf,510,185,self.obtener_instancia().obtener_ct(),estado)
            self.__factura_posicion = self.__factura_posicion + 60
            self.__valor_posicion = self.__valor_posicion + 60


        if estado==0:
            self._posicion_tabla=self.__factura_posicion-250
            self._tabla_pos = self._posicion_tabla
            # Agregar titulo facturas registradas
            facturas_titulo = pdf.beginText(210, self.__h - self.__factura_posicion)
            facturas_titulo.setFont("Helvetica-Bold", 16)
            facturas_titulo.textLine("Facturas registradas")
            pdf.drawText(facturas_titulo)





        self.__factura_posicion = self.__factura_posicion + 40
        self.__valor_posicion = self.__valor_posicion + 40

        # Agregar enumerado página
        pie_de_pagina = pdf.beginText(30, self.__h - 750)
        pie_de_pagina.setFont("Helvetica", 12)
        pie_de_pagina.textLine("Este certificado se expide en concordancia a las resoluciones 3374 de 2000 artículo 7, decreto 4747")
        pdf.drawText(pie_de_pagina)

        # Agregar enumerado página
        pie_de_pagina2 = pdf.beginText(30, self.__h - 760)
        pie_de_pagina2.setFont("Helvetica", 12)
        pie_de_pagina2.textLine("de 2007 y la resolución 3047 de 2008 (Reglamentaria del decreto 4747) que establecen los RIPS")
        pdf.drawText(pie_de_pagina2)

        # Agregar enumerado página
        pie_de_pagina3 = pdf.beginText(30, self.__h - 770)
        pie_de_pagina3.setFont("Helvetica", 12)
        pie_de_pagina3.textLine("como parte de la factura y un soporte más de esta; por lo que la expedición de esta certificación")
        pdf.drawText(pie_de_pagina3)

        # Agregar enumerado página
        pie_de_pagina3 = pdf.beginText(30, self.__h - 780)
        pie_de_pagina3.setFont("Helvetica", 12)
        pie_de_pagina3.textLine("en sí misma no soporta la aprobación y pago de la factura.")
        pdf.drawText(pie_de_pagina3)
        # Agregar enumerado página
        numero_pagina = pdf.beginText(550, self.__h - 810)
        numero_pagina.setFont("Helvetica", 14)
        numero_pagina.textLine(str(self.__numero_paginas))
        pdf.drawText(numero_pagina)

    def agregar_variables_pdf(self, pdf):
        # Agregar variable para el nombre del prestador
        nombre_prestador = pdf.beginText(145, self.__h - 120)
        nombre_prestador.setFont("Helvetica", 12)
        text = self.obtener_instancia().obtener_nombre_prestador()
        wraped_text = "\n".join(wrap(text, 55))
        nombre_prestador.textLines(wraped_text)
        pdf.drawText(nombre_prestador)

        # Agregar variable para el nit
        nit = pdf.beginText(100, self.__h - 145)
        nit.setFont("Helvetica", 12)
        nit.textLine(self.obtener_instancia().obtener_numero_nit())
        pdf.drawText(nit)

        # Agregar valor fecha registro
        fecha_registro = pdf.beginText(180, self.__h - 170)
        fecha_registro.setFont("Helvetica", 12)
        fecha_registro.textLine(self.obtener_instancia().obtener_fecha_registro())
        pdf.drawText(fecha_registro)

    def generar_lista_facturas(self, pdf,eapb,ct,estado):
        locale.setlocale(locale.LC_ALL, '')
        list = self.obtener_instancia().obtener_lista_facturas()
        list_imr=[]
        posicion_en_lista = -1
        list_length= len(list)
        cambiar_pos=0
        pos_y=40
        for item in list:
            posicion_en_lista=posicion_en_lista+1
            if self.__factura_posicion >= 750:

                self.generar_tabla_Facturas(pdf,pos_y,list_imr)
                if cambiar_pos==0:
                    pos_y=pos_y+20
                pdf.showPage()
                list_imr=[]
                self.__factura_posicion = 260
                self.__valor_posicion = 260
                self._posicion_tabla=190
                cambiar_pos=1
                self.__numero_paginas = self.__numero_paginas + 1
                self.agregar_titulos_pdf(pdf,eapb,ct,1)
                self.agregar_variables_pdf(pdf)

                list_aux=(item[0],str(locale.currency(float(item[1]), grouping=True)))
                list_imr.append(list_aux)
                self.__factura_posicion = self.__factura_posicion + 20
                self.__valor_posicion = self.__valor_posicion + 20

            # Agregar número de facturas
            list_aux=(item[0],str(locale.currency(float(item[1]), grouping=True)))
            list_imr.append(list_aux)
            self.__factura_posicion = self.__factura_posicion + 20
            self.__valor_posicion = self.__valor_posicion + 20
            if posicion_en_lista == list_length-1:
                if estado==0 and cambiar_pos==0:
                    self.generar_tabla_Facturas(pdf,100,list_imr)
                if cambiar_pos==1:
                    ajuste_y=190-(len(list_imr)*5)
                    self.generar_tabla_Facturas(pdf,ajuste_y,list_imr)

    def generar_tabla_Facturas(self,pdf,y,facturas):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Número de factura', 'Valor')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = facturas

        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[5 * 20, 5 * 30])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
              ('GRID',(0,0),(-1,-1),0.5,colors.grey),
              ('BOX',(0,0),(-1,-1),2,colors.black),
              ('ALIGN', (1,1), (-1, -1), 'RIGHT'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, self.__w,self.__h)

        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60*mm, y*mm)

    def generar_tabla(self,pdf,y,x,ct,estado):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Tipo Archivo', 'Número de Líneas')
        #Creamos una lista de tuplas que van a contener a las personas
        if estado==0:
            self.generar_lista_tipo_archivos(pdf,ct)

        detalles = self._tipos_archivos

        total =[("Total Líneas",self.numero_de_lineas)]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles+total, colWidths=[5 * 20, 5 * 20])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
              ('GRID',(0,0),(-1,-1),0.5,colors.grey),
              ('BOX',(0,0),(-1,-1),2,colors.black),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        ajuste_y=190-(len(detalles)*5)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 65*mm,ajuste_y*mm)

    def generar_lista_tipo_archivos(self,pdf, lista_ct):
        locale.setlocale(locale.LC_ALL, '')
        for item in lista_ct:
            # Agregar número de facturas
            lista = (item[2][:2],str(int(item[3])))
            self._tipos_archivos.append(lista)
            self.__factura_posicion = self.__factura_posicion + 20

            self.__valor_posicion = self.__valor_posicion + 20

            self.numero_de_lineas = self.numero_de_lineas+int(int(item[3]))

    def generar_pdf(self,ct,eapb):
        pdf = canvas.Canvas("/tmp/a.pdf", pagesize=A4)
        pdf.setTitle('CERTIFICADO REMISIÓN - ' + self.obtener_instancia().obtener_nombre_rips())
        self.agregar_titulos_pdf(pdf,eapb,ct,0)
        self.agregar_variables_pdf(pdf)
        self.generar_lista_facturas(pdf,eapb,ct,0)

        pdf.save()
        with open("/tmp/a.pdf", "rb") as pdf_file:
            bytes = pdf_file.read()
            encoded_string = base64.b64encode(bytes).decode("utf-8")
            pdf_file.close()

        return encoded_string

    def obtener_zip(self, bucket, key):
        """
        Obtener zip, mediante conexi?n a bucket de s3
        :param bucket:
        :param key:
        :return:
        """
        s3 = boto3.client('s3')
        try:
            archivo = s3.get_object(Bucket=bucket, Key=key)
        except Exception as e:
            return None
        return archivo['Body']


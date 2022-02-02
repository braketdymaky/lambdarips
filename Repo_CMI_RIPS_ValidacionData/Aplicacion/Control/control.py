# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.control_enum import ControlColumnasEnum as Columnas
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Utilidades.Enumerados.TipoArchivo.tipo_archivo_enum import TipoArchivosEnum as TA
from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.Control.control import ModeloControl
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico as Generico


class ValidacionControl(ValidacionBase):

    def __init__(self):
        super().__init__()
        self.nombre_archivo = TA.CT.obtener_nombre
        self.model = ModeloControl.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.codigo_habilitacion = ''
        self.codigo_habilitacion_token = ''

    def validar_codigo_habilitacion(self, ct_fila, linea_fila):
        """
        Función para validar que el código de habilitación, este contenido en todos los registros de CT
        :param ct_fila:
        :param linea_fila:
        :return:
        """
        lista_ct = self.model.obtener_lista()
        self.codigo_habilitacion = lista_ct[0][Columnas.CT.obtener_codigo_prestador_posicion]
        if not ct_fila[Columnas.CT.obtener_codigo_prestador_posicion] == self.codigo_habilitacion:
            self.detectar_error(TE.CT_CODIGO_HABILITACION.obtener_descripcion,
                                Columnas.CT.obtener_codigo_prestador_posicion, linea_fila)

    def validar_fecha_remision(self, ct_fila, linea_fila):
        try:
            fecha_remision = Generico().validar_fecha_menor_actual(ct_fila[Columnas.CT.obtener_fecha_remision_posicion])
            if fecha_remision is False:
                self.detectar_error(TE.CT_FECHA_REMISION.obtener_descripcion,
                                    Columnas.CT.obtener_fecha_remision_posicion,
                                    linea_fila)

        except AssertionError:
            self.detectar_error(TE.CT_FECHA_REMISION.obtener_descripcion, Columnas.CT.obtener_fecha_remision_posicion,
                                linea_fila)
        except ValueError:
            self.detectar_error(TE.CT_FECHA_REMISION.obtener_descripcion, Columnas.CT.obtener_fecha_remision_posicion,
                                linea_fila)
        except IndexError:
            self.detectar_error(TE.CT_FECHA_REMISION.obtener_descripcion, Columnas.CT.obtener_fecha_remision_posicion,
                                linea_fila)

    def validar_codigo_habilitacion_token(self,ct_fila,linea_fila):
        """
        Función para validar que el código de habilitación, sea igual al del token
        :param ct_fila:
        :param linea_fila:
        :return:
        """
        if not ct_fila[Columnas.CT.obtener_codigo_prestador_posicion] == self.codigo_habilitacion_token:
            self.detectar_error(TE.CT_CODIGO_HABILITACION_TOKEN.obtener_descripcion,
                                Columnas.CT.obtener_codigo_prestador_posicion, linea_fila)

    def validar_codigos_habilitacion(self):
        lista_ac = self.model.listas_archivos_registros[TA.AC.obtener_nombre]
        lista_ap = self.model.listas_archivos_registros[TA.AP.obtener_nombre]
        lista_au = self.model.listas_archivos_registros[TA.AU.obtener_nombre]
        lista_ah = self.model.listas_archivos_registros[TA.AH.obtener_nombre]
        lista_an = self.model.listas_archivos_registros[TA.AN.obtener_nombre]
        lista_am = self.model.listas_archivos_registros[TA.AM.obtener_nombre]
        lista_at = self.model.listas_archivos_registros[TA.AT.obtener_nombre]
        lista_af = self.model.listas_archivos_registros[TA.AF.obtener_nombre]
        lista_ad = self.model.listas_archivos_registros[TA.AD.obtener_nombre]
        listas = [lista_ac, lista_ap, lista_au, lista_ah, lista_an, lista_am, lista_at,lista_af,lista_ad]
        lista_indice=[TA.AC.obtener_nombre,TA.AP.obtener_nombre,TA.AU.obtener_nombre,TA.AH.obtener_nombre,TA.AN.obtener_nombre,TA.AM.obtener_nombre,TA.AT.obtener_nombre,TA.AF.obtener_nombre,TA.AD.obtener_nombre]
        for idx,lista in enumerate(listas):
            if lista:
                if lista!=[]:
                    linea_fila=1
                    fallos=0
                    for fila in lista:
                        if fallos==100:
                            break
                        if self.codigo_habilitacion_token not in fila:
                            self.detectar_error(TE.CT_CODIGO_HABILITACION_NO_LISTA.obtener_descripcion,
                                posicion_columna=Columnas.CT.obtener_codigo_prestador_posicion, linea=linea_fila,archivo=lista_indice[idx])
                            fallos+=1
                        linea_fila+=1

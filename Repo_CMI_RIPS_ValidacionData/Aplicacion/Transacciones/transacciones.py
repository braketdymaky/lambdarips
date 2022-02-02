# -*- coding: utf-8 -*-
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as Columnas
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Utilidades.Enumerados.Archivo.consulta_enum import ConsultaColumnasEnum as ACE
from Utilidades.Enumerados.Archivo.otros_servicios_enum import OtrosServiciosColumnasEnum as ATE
from Utilidades.Enumerados.Archivo.medicamentos_enum import MedicamentosColumnasEnum as AME
from Utilidades.Enumerados.Archivo.procedimientos_enum import ProcedimientosColumnasEnum as APE
from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.Transacciones.transacciones import ModeloTransacciones
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico
from Utilidades.Enumerados.Archivo.consulta_enum import ConsultaColumnasEnum as ACE
from Utilidades.Enumerados.Archivo.procedimientos_enum import ProcedimientosColumnasEnum as APE
from Utilidades.Enumerados.Archivo.urgencias_enum import UrgenciasColumnasEnum as UE
from Utilidades.Enumerados.Archivo.hospitalizaciones_enum import HospitalizacionesColumnasEnum as HE
from Utilidades.Enumerados.Archivo.recien_nacidos_enum import RecienNacidosColumnaEnum as RNE
from Utilidades.Enumerados.Archivo.medicamentos_enum import MedicamentosColumnasEnum as ME
from Utilidades.Enumerados.Archivo.otros_servicios_enum import OtrosServiciosColumnasEnum as ATE

class ValidacionTransacciones(ValidacionBase):

    def __init__(self,listas):
        super().__init__()
        self.nombre_archivo = 'AF'
        self.model = ModeloTransacciones.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.lista_ac = listas['AC']
        self.lista_ap = listas['AP']
        self.lista_au = listas['AU']
        self.lista_ah = listas['AH']
        self.lista_an = listas['AN']
        self.lista_am = listas['AM']
        self.lista_at = listas['AT']
        self.tipo_id_prestador = self.model_fichero.obtener_tipo_id_prestador()
        self.fichero_eapb = self.model_fichero.obtener_eapb()
        self.dic_eapb=self.diccionario_eapb(self.fichero_eapb)
        self.dic_ac=self.diccionario_ac(self.lista_ac)
        self.dic_ap=self.diccionario_ap(self.lista_ap)
        self.dic_au=self.diccionario_au(self.lista_au)
        self.dic_an=self.diccionario_an(self.lista_an)
        self.dic_am=self.diccionario_am(self.lista_am)
        self.dic_at=self.diccionario_at(self.lista_at)
        self.dic_ah=self.diccionario_ah(self.lista_ah)
        self.lista_af=listas['AF']
        self.encontrados={}
        
    def diccionario_eapb(self,lista_eapb):
        dic_eapb={}
        for eapb in lista_eapb:
            codigo_eapb=eapb[1]
            dic_eapb[codigo_eapb]=eapb
        return dic_eapb
        
    def diccionario_ac(self,lista_ac):
        dic_ac={}
        for ac_fila in lista_ac:
            factura= ac_fila[ACE.AC.obtener_numero_factura]
            dic_ac[factura]=ac_fila
        
        return dic_ac
    
    def diccionario_ap(self,lista_ap):
        dic_ap={}
        for ap_fila in lista_ap:
            factura= ap_fila[APE.AP.obtener_numero_factura]
            dic_ap[factura]=ap_fila
        
        return dic_ap
        
    def diccionario_au(self,lista_ap):
        dic_ap={}
        for ap_fila in lista_ap:
            factura= ap_fila[UE.AU.obtener_numero_factura]
            dic_ap[factura]=ap_fila
        
        return dic_ap
    
    def diccionario_ah(self,lista_ap):
        dic_ap={}
        for ap_fila in lista_ap:
            factura= ap_fila[HE.AH.obtener_numero_factura]
            dic_ap[factura]=ap_fila
        
        return dic_ap
    
    def diccionario_an(self,lista_ap):
        dic_ap={}
        for ap_fila in lista_ap:
            factura= ap_fila[RNE.AN.obtener_numero_factura]
            dic_ap[factura]=ap_fila
        
        return dic_ap
        
    def diccionario_am(self,lista_ap):
        dic_ap={}
        for ap_fila in lista_ap:
            factura= ap_fila[ME.AM.obtener_numero_factura]
            dic_ap[factura]=ap_fila
        
        return dic_ap
    
    def diccionario_at(self,lista_ap):
        dic_ap={}
        for ap_fila in lista_ap:
            factura= ap_fila[ATE.AT.obtener_numero_factura]
            dic_ap[factura]=ap_fila
        
        return dic_ap
    
    
    def validar_facturas_archivos(self, af_fila, linea_fila):
        
        numero_factura = af_fila[Columnas.AF.obtener_numero_factura]
        ac= self.dic_ac.get(numero_factura)
        ap= self.dic_ap.get(numero_factura)
        au= self.dic_au.get(numero_factura)
        ah= self.dic_ah.get(numero_factura)
        am= self.dic_am.get(numero_factura)
        an= self.dic_an.get(numero_factura)
        at= self.dic_at.get(numero_factura)
       
        if ac is None and ap is None and au is None and ah is None and am is None and an is None and at is None:
            self.detectar_error(TE.AF_NUMERO_IDENTIFICACION.obtener_descripcion,
                                Columnas.AF.obtener_numero_factura, linea_fila)

    def validar_tipo_identificacion_prestador(self, af_fila, linea_fila):
        """
        función que valida que el tipo de identificación del prestador sea valido

        :param af_fila:
        :param linea_fila:
        :return:
        """
        tipos_identificacion = self.tipo_id_prestador
        tipo_id_en_af_fila = [af_fila[Columnas.AF.obtener_tipo_id]]
        encontrado = list(filter(lambda tipo_id: tipo_id == tipo_id_en_af_fila, tipos_identificacion))
        if not encontrado:
            self.detectar_error(TE.AF_TIPO_ID.obtener_descripcion,
                                Columnas.AF.obtener_tipo_id, linea_fila)

    def validar_numero_factura(self, af_fila, linea_fila):
        """
        Función para validar que el numero de factura se encuentre una sola vez
        :param af_fila:
        :param linea_fila:
        :return:
        """
        factura_repetida= self.encontrados.get(af_fila[Columnas.AF.obtener_numero_factura])
        if factura_repetida is None:
            lista_af = self.lista_af
            encontrado = list(filter(lambda campo_af: campo_af[Columnas.AF.obtener_numero_factura] ==
                                                      af_fila[Columnas.AF.obtener_numero_factura], lista_af))
            if len(encontrado) > 1:
                self.encontrados[af_fila[Columnas.AF.obtener_numero_factura]]=encontrado
                self.detectar_error(TE.AF_NUMERO_FACTURA.obtener_descripcion,
                                    Columnas.AF.obtener_numero_factura, linea_fila)
        else:
            self.detectar_error(TE.AF_NUMERO_FACTURA.obtener_descripcion,
                                    Columnas.AF.obtener_numero_factura, linea_fila)
                                    
    def validar_fecha_expedicion(self, af_fila, linea_fila):
        """
        función que valida que la fecha sea mayor a la actual
        :param af_fila:
        :param linea_fila:
        :return:
        """
        estado = ValidacionGenerico.validar_fecha_menor_actual(af_fila[Columnas.AF.obtener_fecha_expedicion])
        if not estado:
            self.detectar_error(TE.AF_FECHA_EXPEDICION.obtener_descripcion, Columnas.AF.obtener_fecha_expedicion,
                                linea_fila)

    def validar_fecha_inicio(self, af_fila, linea_fila):
        """
        función que valida que la fecha sea mayor a la actual y que no sea mayor a la fecha final
        :param af_fila:
        :param linea_fila:
        :return:
        """
        estado = ValidacionGenerico.validar_fecha_menor_actual(af_fila[Columnas.AF.obtener_fecha_inicio])
        estado_menor_final = ValidacionGenerico.validar_fecha_menor_fecha(af_fila[Columnas.AF.obtener_fecha_inicio],
                                                                          af_fila[Columnas.AF.obtener_fecha_final])

        if estado == False or estado_menor_final == False:
            self.detectar_error(TE.AF_FECHA_INICIO.obtener_descripcion, Columnas.AF.obtener_fecha_inicio, linea_fila)

    def validar_fecha_final(self, af_fila, linea_fila):
        """
        función que valida que la fecha sea mayor a la actual y que no sea mayor a la fecha de inicio
        :param af_fila:
        :param linea_fila:
        :return:
        """
        estado = ValidacionGenerico.validar_fecha_menor_actual(af_fila[Columnas.AF.obtener_fecha_final])
        estado_mayor_inicial = ValidacionGenerico.validar_fecha_menor_fecha(af_fila[Columnas.AF.obtener_fecha_inicio],
                                                                            af_fila[Columnas.AF.obtener_fecha_final])
        if estado == False or estado_mayor_inicial == False:
            self.detectar_error(TE.AF_FECHA_FINAL.obtener_descripcion,
                                Columnas.AF.obtener_fecha_final, linea_fila)

    def validar_valor_neto(self, af_fila, linea_fila):
        lista_ac = self.lista_ac
        lista_ap = self.lista_ap
        lista_am = self.lista_am
        lista_at = self.lista_at
        listas = [lista_ac, lista_ap, lista_am, lista_at]
        posicion_campo = [ACE.AC.obtener_valor_neto, APE.AP.obtener_valor, AME.AM.obtener_valor_total,
                          ATE.AT.obtener_valor_total]
        numero_factura = af_fila[Columnas.AF.obtener_numero_factura]
        valor_neto = 0
        ac=self.dic_ac.get(af_fila[Columnas.AF.obtener_numero_factura])
        ap=self.dic_ap.get(af_fila[Columnas.AF.obtener_numero_factura])
        am=self.dic_am.get(af_fila[Columnas.AF.obtener_numero_factura])
        at=self.dic_at.get(af_fila[Columnas.AF.obtener_numero_factura])
        valores_encontrados=[ac,ap,am,at]
        for idx, lista in enumerate(listas):
            if lista and valores_encontrados[idx] is not None:
                for fila in lista:
                    if numero_factura in fila:
                        valor_neto += float(fila[posicion_campo[idx]])
        if not float(valor_neto) == float(af_fila[Columnas.AF.obtener_valor_neto]):
            self.detectar_error(TE.AF_VALOR_NETO.obtener_descripcion, Columnas.AF.obtener_valor_neto, linea_fila)

    def validar_codigo_entidad(self, af_fila, linea_fila):
        codigo_entidad = af_fila[Columnas.AF.obtener_codigo_entidad]
        encontrado =  self.dic_eapb.get(codigo_entidad)
        if encontrado is None:
            self.detectar_error(TE.AF_EAPB_INVALIDO.obtener_descripcion, Columnas.AF.obtener_codigo_entidad,
                                linea_fila)

    def validar_codigo_eps(self, af_fila, linea_fila):
        codigo_entidad = af_fila[Columnas.AF.obtener_codigo_entidad]
        codigo_eps = self.model.obtener_id_cliente()
        if codigo_entidad != codigo_eps:
            self.detectar_error(TE.AF_EPS_INVALIDO.obtener_descripcion, Columnas.AF.obtener_codigo_entidad, linea_fila)

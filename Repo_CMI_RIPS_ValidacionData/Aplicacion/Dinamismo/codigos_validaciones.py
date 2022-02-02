# -*- coding: utf-8 -*-
from threading import *
from Aplicacion.Control.control import ValidacionControl
from Aplicacion.DescripcionAgrupada.descripcion_agrupada import ValidacionDescripcionAgrupada
from Aplicacion.OtrosServicios.otros_servicios import ValidacionOtrosServicios
from Aplicacion.Transacciones.transacciones import ValidacionTransacciones
from Aplicacion.Consulta.consulta import ValidacionConsulta
from Aplicacion.Usuarios.usuarios import ValidacionUsuarios
from Aplicacion.Procedimientos.procedimientos import ValidacionProcedimiento
from Aplicacion.Hospitalizacion.hospitalizacion import ValidacionHospitalizacion
from Aplicacion.Medicamentos.medicamentos import ValidacionMedicamentos
from Aplicacion.Urgencias.urgencias import ValidacionUrgencias
from Aplicacion.RecienNacidos.recien_nacidos import ValidacionRecienNacidos
from Dominio.Hospitalizaciones.hospitalizaciones import ModeloHospitalizacion
from Dominio.Medicamentos.medicamentos import ModeloMedicamentos
from Dominio.Urgencias.urgencias import ModeloUrgencias
from Dominio.Fichero.fichero import ModeloFichero
from Utilidades.Enumerados.Archivo.transacciones_enum import TransaccionesColumnasEnum as Transacciones
from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as USE


class ValidacionDinamismo:
    listas_archivos_registros = []
    CT_codigos_validaciones = []
    AC_codigos_validaciones = []
    AD_codigos_validaciones = []
    AH_codigos_validaciones = []
    AM_codigos_validaciones = []
    AT_codigos_validaciones = []
    AN_codigos_validaciones = []
    AF_codigos_validaciones = []
    AU_codigos_validaciones = []
    AP_codigos_validaciones = []
    US_codigos_validaciones = []

    def cargar_validaciones(self):
        self.CT_codigos_validaciones = {17:self.CT.validar_codigo_habilitacion_token,19: self.CT.validar_codigo_habilitacion, 12: self.CT.validar_fecha_remision}
        self.US_codigos_validaciones = {48: self.US.validar_identificaciones_archivos, 49: self.US.validar_tipo_id,
                                        50: self.US.validar_long_id_cc_ms, 51: self.US.validar_long_id_ce,
                                        52: self.US.validar_long_id_pa_cd_sc, 53: self.US.validar_long_id_rc_ti,
                                        54: self.US.validar_long_id_as, 55: self.US.validar_long_id_cn,
                                        56: self.US.validar_long_id_pe, 58: self.US.validar_codigo_eapb,
                                        59: self.US.validar_codigo_eps, 60: self.US.validar_tipo_usuario,
                                        68: self.US.validar_unidad_medida,
                                        69: self.US.validar_edad_segun_unidad_medida_1,
                                        70: self.US.validar_edad_segun_unidad_medida_2,
                                        71: self.US.validar_edad_segun_unidad_medida_3,
                                        72: self.US.validar_tipo_id_edad_um_1, 74: self.US.validar_tipo_id_edad_um_2,
                                        75: self.US.validar_tipo_id_edad_um_3, 76: self.US.validar_tipo_id_edad_um_4,
                                        77: self.US.validar_tipo_id_edad_um_5, 78: self.US.validar_tipo_id_edad_um_6,
                                        79: self.US.validar_tipo_id_edad_um_7, 80: self.US.validar_tipo_id_edad_um_8,
                                        81: self.US.validar_sexo, 82: self.US.validar_departamento,
                                        83: self.US.validar_municipio, 84: self.US.validar_zona_residencial}
        self.AD_codigos_validaciones = {288: self.AD.validar_numero_factura, 289: self.AD.validar_codigo_del_concepto,
                                        293: self.AD.validar_valor_unitario_cantidad,
                                        296: self.AD.validar_valor_total_segun_unitario}
        self.AT_codigos_validaciones = {271: self.AT.validar_numero_factura, 272: self.AT.validar_tipo_identificacion,
                                        274: self.AT.validar_tipo_numero_identificacion,
                                        276: self.AT.validar_tipo_servicio,
                                        278: self.AT.validar_tipo_servicio_codigo_cups,
                                        280: self.AT.validar_nombre_servico, 282: self.AT.validar_cantidad_servicio,
                                        285: self.AT.validar_valor_unitario,
                                        287: self.AT.validar_valor_total_segun_unitario,
                                        300: self.AT.validar_guion_numero_autorizacion}

        self.AF_codigos_validaciones = {20: self.AF.validar_facturas_archivos,
                                        22: self.AF.validar_tipo_identificacion_prestador,
                                        25: self.AF.validar_numero_factura, 28: self.AF.validar_fecha_expedicion,
                                        30: self.AF.validar_fecha_inicio,
                                        32: self.AF.validar_fecha_final,33:self.AF.validar_codigo_entidad,
                                        34: self.AF.validar_codigo_eps,47: self.AF.validar_valor_neto}

        self.AU_codigos_validaciones = {148: self.AU.validar_numero_factura,
                                        149: self.AU.validar_tipo_identificacion,
                                        151: self.AU.validar_tipo_numero_identificacion,
                                        153: self.AU.validar_fecha_ingreso_usuario_a_observacion,
                                        156: self.AU.validar_causa_externa,
                                        157: self.AU.validar_diagnostico_principal_de_salida,
                                        158: self.AU.validar_diagnostico_principal_de_salida_sexo,
                                        159: self.AU.validar_diagnostico_principal_de_salida_edad,
                                        160: self.AU.validar_diagnostico_principal_de_salida_rel_1,
                                        161: self.AU.validar_diagnostico_principal_de_salida_rel_1_sexo,
                                        162: self.AU.validar_diagnostico_principal_de_salida_rel_1_edad,
                                        163: self.AU.validar_diagnostico_principal_de_salida_rel_2,
                                        164: self.AU.validar_diagnostico_principal_de_salida_rel_2_sexo,
                                        165: self.AU.validar_diagnostico_principal_de_salida_rel_2_edad,
                                        166: self.AU.validar_diagnostico_principal_de_salida_rel_3,
                                        167: self.AU.validar_diagnostico_principal_de_salida_rel_3_sexo,
                                        168: self.AU.validar_diagnostico_principal_de_salida_rel_3_edad,
                                        169: self.AU.validar_destino_usuario_salida_observacion,
                                        170: self.AU.validar_estado_salida,
                                        171: self.AU.validar_causa_basica_de_muerte,
                                        172: self.AU.validar_causa_basica_de_muerte_2,
                                        173: self.AU.validar_causa_muerte_sexo,
                                        174: self.AU.validar_causa_muerte_edad,
                                        176: self.AU.validar_fecha_salida_usuario_a_observacion,
                                        178: self.AU.validar_fecha_ingreso_menor_salida_usuario_a_observacion,
                                        179: self.AU.validar_hora_ingreso_menor_salida_usuario_a_observacion,
                                        180: self.AU.validar_destino_salida_usuario,
                                        297: self.AU.validar_guion_numero_autorizacion}

        self.AM_codigos_validaciones = {248: self.AM.validar_numero_factura,
                                        249: self.AM.validar_tipo_identificacion,
                                        251: self.AM.validar_tipo_numero_identificacion,
                                        254: self.AM.validar_tipo_medicamento,
                                        256: self.AM.validar_nombre_generico_del_medicamento_no_nulo,
                                        258: self.AM.validar_forma_farmaceutica_no_nulo,
                                        260: self.AM.validar_concentracion_del_medicamento_no_nulo,
                                        262: self.AM.validar_unidad_de_medida_del_medicamento_no_nulo,
                                        264: self.AM.validar_numero_de_unidades_no_nulo,
                                        267: self.AM.validar_valor_unitario_de_medicamento_no_nulo,
                                        270: self.AM.validar_valor_total_de_medicamento,
                                        299: self.AM.validar_guion_numero_autorizacion}

        self.AH_codigos_validaciones = {181: self.AH.validar_numero_factura,
                                        182: self.AH.validar_tipo_identificacion,
                                        184: self.AH.validar_tipo_numero_identificacion,
                                        185: self.AH.validar_via_ingreso_a_institucion,
                                        186: self.AH.validar_via_ingreso_a_institucion_1,
                                        187: self.AH.validar_via_ingreso_a_institucion_2,
                                        188: self.AH.validar_via_ingreso_a_institucion_4,
                                        190: self.AH.validar_fecha_ingreso_usuario_a_institucion,
                                        193: self.AH.validar_causa_externa,
                                        194: self.AH.validar_diagnostico_principal_de_ingreso,
                                        195: self.AH.validar_diagnostico_principal_de_ingreso_2,
                                        196: self.AH.validar_diagnostico_principal_de_ingreso_sexo,
                                        197: self.AH.validar_diagnostico_principal_de_ingreso_edad,
                                        198:self.AH.validar_diagnostico_principal_de_egreso,
                                        199:self.AH.validar_diagnostico_egreso_sexo,
                                        200:self.AH.validar_diagnostico_egreso_edad,
                                        201: self.AH.validar_diagnostico_relacionado_1,
                                        202: self.AH.validar_diagnostico_relacionado_1_sexo,
                                        203: self.AH.validar_diagnostico_relacionado_1_edad,
                                        204: self.AH.validar_diagnostico_relacionado_2,
                                        205: self.AH.validar_diagnostico_relacionado_2_sexo,
                                        206: self.AH.validar_diagnostico_relacionado_2_edad,
                                        207: self.AH.validar_diagnostico_relacionado_3,
                                        208: self.AH.validar_diagnostico_relacionado_3_sexo,
                                        209: self.AH.validar_diagnostico_relacionado_3_edad,
                                        210: self.AH.validar_diagnostico_complicacion,
                                        211: self.AH.validar_diagnostico_complicacion_sexo,
                                        212: self.AH.validar_diagnostico_complicacion_edad,
                                        213: self.AH.validar_estado_salida,
                                        214: self.AH.validar_causa_basica_de_muerte_estado_salida,
                                        215: self.AH.validar_causa_basica_de_muerte,
                                        216: self.AH.validar_causa_basica_de_muerte_sexo,
                                        217: self.AH.validar_causa_basica_de_muerte_edad,
                                        219: self.AH.validar_fecha_egreso_usuario_a_observacion,
                                        221: self.AH.validar_fecha_ingreso_menor_egreso_a_institucion,
                                        222: self.AH.validar_hora_ingreso_menor_salida_usuario_a_institucion,
                                        298: self.AH.validar_guion_numero_autorizacion}

        self.AP_codigos_validaciones = {122: self.AP.validar_numero_factura,
                                        123: self.AP.validar_tipo_id,
                                        125: self.AP.validar_tipo_numero_identificacion,
                                        127: self.AP.validar_fecha_procedimiento,
                                        129: self.AP.validar_guion_numero_autorizacion,
                                        130: self.AP.validar_codigo_procedimiento,
                                        131: self.AP.validar_ambito_realizacion_procedimiento,
                                        133: self.AP.validar_personal_atiende,
                                        132: self.AP.validar_finalidad_procedimiento,
                                        134: self.AP.validar_codigo_quirurgico,
                                        135: self.AP.validar_diagnostico_rel1,
                                        136: self.AP.validar_complicacion,
                                        137: self.AP.validar_forma_realizacion,
                                        138: self.AP.validar_no_quirurgico,
                                        139: self.AP.validar_diagnostico_principal_sexo,
                                        140: self.AP.validar_diagnostico_principal_edad,
                                        141: self.AP.validar_diagnostico_rel_1_sexo,
                                        142: self.AP.validar_diagnostico_rel_1_edad,
                                        143: self.AP.validar_complicacion_sexo,
                                        144: self.AP.validar_complicacion_edad}

        self.AN_codigos_validaciones = {223: self.AN.validar_numero_factura,
                                        224: self.AN.validar_tipo_id_madre,
                                        226: self.AN.validar_tipo_numero_identificacion,
                                        228: self.AN.validar_fecha_nacimiento,
                                        231: self.AN.validar_control_prenatal,
                                        232: self.AN.validar_sexo,
                                        235: self.AN.validar_diagnostico_nacido,
                                        236: self.AN.validar_diagnostico_nacido_sexo,
                                        237: self.AN.validar_diagnostico_nacido_edad,
                                        238: self.AN.validar_causa_muerte,
                                        239: self.AN.validar_causa_muerte2,
                                        240: self.AN.validar_causa_muerte_sexo,
                                        241: self.AN.validar_causa_muerte_edad,
                                        243: self.AN.validar_fecha_muerte_actual,
                                        244: self.AN.validar_fecha_muerte_nacimiento,
                                        246: self.AN.validar_causa_fecha_muerte_hora_muerte,
                                        247: self.AN.validar_horas_fechas_iguales}

        self.AC_codigos_validaciones = {86: self.AC.validar_numero_factura, 87: self.AC.validar_tipo_id,
                                        89: self.AC.validar_tipo_numero_identificacion,
                                        91: self.AC.validar_fecha_procedimiento, 94: self.AC.validar_codigo_consulta,
                                        92: self.AC.validar_guion_numero_autorizacion,
                                        95: self.AC.validar_finalidad_consulta, 96: self.AC.validar_causa_externa,
                                        97: self.AC.validar_codigo_diagnostico_principal,
                                        98: self.AC.validar_diagnostico_principal_sexo,
                                        99: self.AC.validar_diagnostico_principal_edad,
                                        100: self.AC.validar_finalidad_diagnostico_1,
                                        101: self.AC.validar_finalidad_diagnostico_2,
                                        102: self.AC.validar_diagnostico_relacionado_1,
                                        103: self.AC.validar_diagnostico_relacionado_1_sexo,
                                        104: self.AC.validar_diagnostico_relacionado_1_edad,
                                        105: self.AC.validar_diagnostico_relacionado_2,
                                        106: self.AC.validar_diagnostico_relacionado_2_sexo,
                                        107: self.AC.validar_diagnostico_relacionado_2_edad,
                                        108: self.AC.validar_diagnostico_relacionado_3,
                                        109: self.AC.validar_diagnostico_relacionado_3_sexo,
                                        110: self.AC.validar_diagnostico_relacionado_3_edad,
                                        111: self.AC.validar_tipo_diagnostico_principal}

    def __init__(self, direccion_archivo, id_cliente, listas, dinamismo,codigo_habilitacion,codigo_prestador):
        self.model_fichero = ModeloFichero.obtener_instancia()
        self.evento = Event()
        self.ignorar = dinamismo
        self.codigo_prestador=codigo_prestador
        self.cups=self.model_fichero.obtener_cups()
        self.cups_dic = self.crear_diccionario_cups(self.cups)
        self.dic_us=self.crear_diccionario_us(listas['US'])
        self.dic_af=self.crear_diccionario_af(listas['AF'])
        self.cie10=self.model_fichero.obtener_cie10()
        self.cie10_dic= self.crear_diccionario_cie10(self.cie10)
        self.listas_archivos_registros = listas
        self.CT = ValidacionControl()
        self.CT.model.asignar_valores(listas['CT'])
        self.CT.model.asignar_listas(self.listas_archivos_registros)
        self.CT.codigo_habilitacion_token =codigo_habilitacion
        self.AD = ValidacionDescripcionAgrupada(listas['AF'])
        self.AD.model.asignar_valores(listas['AD'])
        self.AT = ValidacionOtrosServicios(listas['AC'],listas['AP'],listas['US'],listas['AF'],self.cups_dic,self.dic_af,self.dic_us)
        self.AT.model.asignar_valores(listas['AT'])
        self.AF = ValidacionTransacciones(listas)
        self.AF.model.asignar_valores(listas['AF'])
        self.AF.model.asignar_listas(self.listas_archivos_registros)
        self.AF.model.asignar_id_cliente(id_cliente)
        self.US = ValidacionUsuarios(self.listas_archivos_registros)
        self.US.model.asignar_valores(listas['US'])
        self.US.model.asignar_id_cliente(id_cliente)
        self.AP = ValidacionProcedimiento(listas['AF'],listas['US'],self.cups_dic,self.dic_af,self.dic_us,self.cie10_dic)
        self.AP.model.asignar_valores(listas['AP'])
        self.AC = ValidacionConsulta(listas['AF'],listas['US'],self.cups_dic,self.cie10_dic,self.dic_af,self.dic_us)
        self.AC.model.asignar_valores(listas['AC'])
        self.AU = ValidacionUrgencias(listas['AF'],listas['AH'],listas['US'],self.cie10_dic,self.dic_af,self.dic_us)
        self.AU.model.asignar_valores(listas['AU'])
        self.AH = ValidacionHospitalizacion(listas,self.cie10_dic,self.dic_af,self.dic_us,self.codigo_prestador)
        self.AH.model.asignar_valores(listas['AH'])
        self.AM = ValidacionMedicamentos(listas['AF'],listas['US'],self.dic_af,self.dic_us)
        self.AM.model.asignar_valores(listas['AM'])
        self.AN = ValidacionRecienNacidos(listas['AF'],listas['US'],listas['AH'],self.cie10_dic,self.dic_af,self.dic_us)
        self.AN.model.asignar_valores(listas['AN'])
        self.cargar_validaciones()

    @classmethod
    def obtener_lista(cls, tipo_archivo):
        return cls.listas_archivos_registros[tipo_archivo]

    def crear_diccionario_us(self,lista_us):
        dic_us={}
        for us in lista_us:
            usc=us[USE.US.obtener_numero_id]
            dic_us[usc]=us
        return dic_us
    
    def crear_diccionario_af(self,lista_af):
        dic_af={}
        for af in lista_af:
            afc=af[Transacciones.AF.obtener_numero_factura]
            dic_af[afc]=af
        return dic_af
    def crear_diccionario_cie10(self, lista_cie10):
        cie10_dic={}

        for c in lista_cie10:
            cod_procedimiento = c[0]
            cie10_dic[cod_procedimiento] = c

        return cie10_dic

    def crear_diccionario_cups(self, lista_cups):
        cups_dic={}

        for c in lista_cups:
            cod_procedimiento = c[0]
            cups_dic[cod_procedimiento] = c

        return cups_dic

    def decorator(self, fun, ct_fila, posicion_fila):
        def inner():
            resultfun = fun(ct_fila, posicion_fila)
            return resultfun

        return inner

    def dinamismos_ah(self):
        fila = 1
        if self.AH.model.obtener_instancia().obtener_lista() != []:
            for ah_fila in self.AH.model.obtener_instancia().obtener_lista():
                for AH_key in self.AH_codigos_validaciones.keys():
                    if AH_key not in self.ignorar:
                        funcion = self.decorator(self.AH_codigos_validaciones[AH_key], ah_fila, fila)
                        funcion()
                fila += 1
        if self.AH.lista_errores:
            self.AH.generar_archivo_errores(self.AH.lista_errores)

    def dinamismos_am(self):
        fila = 1
        for am_fila in self.AM.model.obtener_instancia().obtener_lista():
            for AM_key in self.AM_codigos_validaciones.keys():
                if AM_key not in self.ignorar:
                    funcion = self.decorator(self.AM_codigos_validaciones[AM_key], am_fila, fila)
                    funcion()
            fila += 1
        if self.AM.lista_errores:
            self.AM.generar_archivo_errores(self.AM.lista_errores)

    def dinamismos_ct(self):
        self.CT.validar_codigos_habilitacion()
        fila = 1
        for ct_fila in self.CT.model.obtener_instancia().obtener_lista():
            for CT_key in self.CT_codigos_validaciones.keys():
                if CT_key not in self.CT.metodos_de_validacion_a_ignorar:
                    funcion = self.decorator(self.CT_codigos_validaciones[CT_key], ct_fila, fila)
                    funcion()
            fila += 1
        if self.CT.lista_errores:
            self.CT.generar_archivo_errores(self.CT.lista_errores)

    def dinamismos_ac(self):
        fila = 1
        for ac_fila in self.AC.model.obtener_instancia().obtener_lista():
            for AC_key in self.AC_codigos_validaciones.keys():
                if AC_key not in self.ignorar:
                    funcion = self.decorator(self.AC_codigos_validaciones[AC_key], ac_fila, fila)
                    funcion()
            fila += 1
        if self.AC.lista_errores:
            self.AC.generar_archivo_errores(self.AC.lista_errores)

    def dinamismos_ad(self):
        fila = 1
        for ad_fila in self.AD.model.obtener_instancia().obtener_lista():
            for AD_key in self.AD_codigos_validaciones.keys():
                if AD_key not in self.ignorar:
                    funcion = self.decorator(self.AD_codigos_validaciones[AD_key], ad_fila, fila)
                    funcion()
            fila += 1
        if self.AD.lista_errores:
            self.AD.generar_archivo_errores(self.AD.lista_errores)

    def dinamismos_at(self):
        fila = 1
        for at_fila in self.AT.model.obtener_instancia().obtener_lista():
            for AT_key in self.AT_codigos_validaciones.keys():
                if AT_key not in self.ignorar:
                    funcion = self.decorator(self.AT_codigos_validaciones[AT_key], at_fila, fila)
                    funcion()
            fila += 1
        if self.AT.lista_errores:
            self.AT.generar_archivo_errores(self.AT.lista_errores)

    def dinamismos_af(self):
        fila = 1
        for af_fila in self.AF.model.obtener_instancia().obtener_lista():
            for AF_key in self.AF_codigos_validaciones.keys():
                if AF_key not in self.ignorar:
                    funcion = self.decorator(self.AF_codigos_validaciones[AF_key], af_fila, fila)
                    funcion()
            fila += 1
        if self.AF.lista_errores:
            self.AF.generar_archivo_errores(self.AF.lista_errores)

    def dinamismos_ap(self):
        listas_ap=self.AP.model.obtener_instancia().obtener_lista()
        fila = 1
        for ap_fila in listas_ap:
            for AP_key in self.AP_codigos_validaciones.keys():
                if AP_key not in self.ignorar:
                    funcion = self.decorator(self.AP_codigos_validaciones[AP_key], ap_fila, fila)
                    funcion()
            fila += 1

        if self.AP.lista_errores:
            self.AP.generar_archivo_errores(self.AP.lista_errores)

    def dinamismos_an(self):
        fila = 1
        for an_fila in self.AN.model.obtener_instancia().obtener_lista():
            for AN_key in self.AN_codigos_validaciones.keys():
                if AN_key not in self.ignorar:
                    funcion = self.decorator(self.AN_codigos_validaciones[AN_key], an_fila, fila)
                    funcion()
            fila += 1
        if self.AN.lista_errores:
            self.AN.generar_archivo_errores(self.AN.lista_errores)

    def dinamismos_au(self):
        fila = 1
        for au_fila in self.AU.model.obtener_instancia().obtener_lista():
            for AU_key in self.AU_codigos_validaciones.keys():
                if AU_key not in self.ignorar:
                    funcion = self.decorator(self.AU_codigos_validaciones[AU_key], au_fila, fila)
                    funcion()
            fila += 1
        if self.AU.lista_errores:
            self.AU.generar_archivo_errores(self.AU.lista_errores)

    def dinamismos_us(self):
        fila = 1
        for us_fila in self.US.model.obtener_instancia().obtener_lista():
            for US_key in self.US_codigos_validaciones.keys():
                if US_key not in self.ignorar:
                    funcion = self.decorator(self.US_codigos_validaciones[US_key], us_fila, fila)
                    funcion()
            fila += 1
        if self.US.lista_errores:
            self.US.generar_archivo_errores(self.US.lista_errores)



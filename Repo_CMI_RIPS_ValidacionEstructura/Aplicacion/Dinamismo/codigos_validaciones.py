from Utilidades.Enumerados.Archivo.control_enum import ControlColumnasEnum as CT_columnas
from Aplicacion.DescripcionAgrupada.descripcion_agrupada import ValidacionDescripcionAgrupada
from Aplicacion.Hospitalizacion.hospitalizacion import ValidacionHospitalizacion
from Aplicacion.OtrosServicios.otros_servicios import ValidacionOtrosServicios
from Aplicacion.Procedimientos.procedimientos import ValidacionProcedimientos
from Aplicacion.RecienNacidos.recien_nacidos import ValidacionRecienNacidos
from Aplicacion.Transacciones.transacciones import ValidacionTransacciones
from Aplicacion.Medicamentos.medicamentos import ValidacionMedicamentos
from Aplicacion.Genericos.genericos_servicio import ValidacionGenerico
from Aplicacion.Urgencias.urgencias import ValidacionUrgencias
from Aplicacion.Consulta.consulta import ValidacionConsulta
from Aplicacion.Usuarios.usuarios import ValidacionUsuarios
from Aplicacion.Control.control import ValidacionControl
from Aplicacion.Zip import zip


class CodigosValidaciones:
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
        self.CT_codigos_validaciones = {0: self.CT.validar_cantidad_columnas}
        self.AC_codigos_validaciones = {0: self.AC.validar_cantidad_columnas}
        self.AD_codigos_validaciones = {0: self.AD.validar_cantidad_columnas}
        self.AH_codigos_validaciones = {0: self.AH.validar_cantidad_columnas}
        self.AM_codigos_validaciones = {0: self.AM.validar_cantidad_columnas}
        self.AT_codigos_validaciones = {0: self.AT.validar_cantidad_columnas}
        self.AN_codigos_validaciones = {0: self.AN.validar_cantidad_columnas}
        self.AP_codigos_validaciones = {0: self.AP.validar_cantidad_columnas}
        self.AF_codigos_validaciones = {0: self.AF.validar_cantidad_columnas}
        self.AU_codigos_validaciones = {0: self.AU.validar_cantidad_columnas}
        self.US_codigos_validaciones = {0: self.US.validar_cantidad_columnas}

    def __init__(self, codigo_prestador,dinamismo):
        self.ignorar = dinamismo
        self.CT = ValidacionControl()
        self.CT.ct_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['CT'])


        self.AC = ValidacionConsulta()
        self.AC.ac_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AC'])
        self.AH = ValidacionHospitalizacion()
        self.AH.ah_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AH'])
        self.AD = ValidacionDescripcionAgrupada()
        self.AD.ad_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AD'])
        self.AM = ValidacionMedicamentos()
        self.AM.am_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AM'])
        self.AT = ValidacionOtrosServicios()
        self.AT.at_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AT'])
        self.AN = ValidacionRecienNacidos()
        self.AN.an_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AN'])
        self.AP = ValidacionProcedimientos()
        self.AP.ap_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AP'])
        self.AF = ValidacionTransacciones()
        self.AF.af_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AF'])
        self.AU = ValidacionUrgencias()
        self.AU.au_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['AU'])
        self.US = ValidacionUsuarios()
        self.US.us_model.obtener_instancia().asignar_valores(
            zip.ValidacionZip().modelo.obtener_instancia().obtener_lista_registros_archivos()['US'])
        self.cargar_validaciones()

    def decorator(self, fun, ct_fila, posicion_fila):
        def inner():
            resultfun = fun(ct_fila, posicion_fila)
            return resultfun

        return inner

    def dinamismos_ct(self):
        self.CT.validar_estructura_ct()
        for CT_key in self.CT_codigos_validaciones.keys():
            fila = 1
            if CT_key not in self.CT.metodos_de_validacion_a_ignorar:
                for ct_fila in self.CT.ct_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.CT_codigos_validaciones[CT_key], ct_fila, fila)
                    funcion()
                    fila += 1
        if self.CT.lista_errores:
            self.CT.generar_archivo_errores(self.CT.lista_errores)

    def dinamismos_ac(self):
        for AC_key in self.AC_codigos_validaciones.keys():
            fila = 1
            if AC_key not in self.ignorar:
                for ac_fila in self.AC.ac_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AC_codigos_validaciones[AC_key], ac_fila, fila)
                    funcion()
                    fila += 1
        if self.AC.lista_errores:
            self.AC.generar_archivo_errores(self.AC.lista_errores)

    def dinamismos_ad(self):
        for AD_key in self.AD_codigos_validaciones.keys():
            fila = 1
            if AD_key not in self.ignorar:
                for ad_fila in self.AD.ad_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AD_codigos_validaciones[AD_key], ad_fila, fila)
                    funcion()
                    fila += 1
        if self.AD.lista_errores:
            self.AD.generar_archivo_errores(self.AD.lista_errores)

    def dinamismos_ah(self):
        for AH_key in self.AH_codigos_validaciones.keys():
            fila = 1
            if AH_key not in self.ignorar:
                for ah_fila in self.AH.ah_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AH_codigos_validaciones[AH_key], ah_fila, fila)
                    funcion()
                    fila += 1
        if self.AH.lista_errores:
            self.AH.generar_archivo_errores(self.AH.lista_errores)

    def dinamismos_am(self):
        for AM_key in self.AM_codigos_validaciones.keys():
            fila = 1
            if AM_key not in self.ignorar:
                for am_fila in self.AM.am_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AM_codigos_validaciones[AM_key], am_fila, fila)
                    funcion()
                    fila += 1
        if self.AM.lista_errores:
            self.AM.generar_archivo_errores(self.AM.lista_errores)

    def dinamismos_at(self):
        for AT_key in self.AT_codigos_validaciones.keys():
            fila = 1
            if AT_key not in self.ignorar:
                for at_fila in self.AT.at_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AT_codigos_validaciones[AT_key], at_fila, fila)
                    funcion()
                    fila += 1
        if self.AT.lista_errores:
            self.AT.generar_archivo_errores(self.AT.lista_errores)

    def dinamismos_ap(self):
        for AP_key in self.AP_codigos_validaciones.keys():
            fila = 1
            if AP_key not in self.ignorar:
                for ap_fila in self.AP.ap_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AP_codigos_validaciones[AP_key], ap_fila, fila)
                    funcion()
                    fila += 1
        if self.AP.lista_errores:
            self.AP.generar_archivo_errores(self.AP.lista_errores)

    def dinamismos_an(self):
        for AN_key in self.AN_codigos_validaciones.keys():
            fila = 1
            if AN_key not in self.ignorar:
                for an_fila in self.AN.an_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AN_codigos_validaciones[AN_key], an_fila, fila)
                    funcion()
                    fila += 1
        if self.AN.lista_errores:
            self.AN.generar_archivo_errores(self.AN.lista_errores)

    def dinamismos_af(self):
        for AF_key in self.AF_codigos_validaciones.keys():
            fila = 1
            if AF_key not in self.ignorar:
                for af_fila in self.AF.af_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AF_codigos_validaciones[AF_key], af_fila, fila)
                    funcion()
                    fila += 1
        if self.AF.lista_errores:
            self.AF.generar_archivo_errores(self.AF.lista_errores)

    def dinamismos_au(self):
        for AU_key in self.AU_codigos_validaciones.keys():
            fila = 1
            if AU_key not in self.ignorar:
                for au_fila in self.AU.au_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.AU_codigos_validaciones[AU_key], au_fila, fila)
                    funcion()
                    fila += 1
        if self.AU.lista_errores:
            self.AU.generar_archivo_errores(self.AU.lista_errores)
            
    def dinamismos_us(self):
        for US_key in self.US_codigos_validaciones.keys():
            fila = 1
            if US_key not in self.ignorar:
                for us_fila in self.US.us_model.obtener_instancia().obtener_lista():
                    funcion = self.decorator(self.US_codigos_validaciones[US_key], us_fila, fila)
                    funcion()
                    fila += 1
        if self.US.lista_errores:
            self.US.generar_archivo_errores(self.US.lista_errores)



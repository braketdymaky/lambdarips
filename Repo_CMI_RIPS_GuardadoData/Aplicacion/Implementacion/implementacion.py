from Utilidades.Archivo.transacciones_enum import TransaccionesColumnasEnum
from Utilidades.Archivo.usuarios_enum import UsuariosColumnasEnum
from Utilidades.Archivo.control_enum import ControlColumnasEnum
from Utilidades.Archivo.consulta_enum import ConsultaColumnasEnum
from Utilidades.Archivo.procedimientos_enum import ProcedimientosColumnasEnum
from Utilidades.Archivo.urgencias_enum import UrgenciasColumnasEnum
from Utilidades.Archivo.descripcion_agrupada_enum import DescripcionAgrupadaColumnasEnum
from Utilidades.Archivo.hospitalizaciones_enum import HospitalizacionesColumnasEnum
from Utilidades.Archivo.medicamentos_enum import MedicamentosColumnasEnum
from Utilidades.Archivo.otros_servicios_enum import OtrosServiciosColumnasEnum
from Utilidades.Archivo.recien_nacidos_enum import RecienNacidosColumnaEnum
from Aplicacion.Implementacion.reemplazar import Reemplazar
from Aplicacion.Consulta.consultas import Consulta


class Implementacion:
    cambios = Reemplazar()
    consulta = Consulta()

    def us_reemplazar(self, lista_us):
        tipo_id = UsuariosColumnasEnum.US.obtener_tipo_id
        tipo_usuario = UsuariosColumnasEnum.US.obtener_tipo_usuario
        u_medida = UsuariosColumnasEnum.US.obtener_medida_de_edad
        sexo = UsuariosColumnasEnum.US.obtener_sexo
        municipio = UsuariosColumnasEnum.US.obtener_municipio_residencia
        zona_residencia = UsuariosColumnasEnum.US.obtener_zona_residencial
        for registro in lista_us:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id(registro[tipo_id])
            registro[tipo_usuario] = self.cambios.reemplazar_tipo_usuario(registro[tipo_usuario])
            registro[u_medida] = self.cambios.reemplazar_unidad_medida(registro[u_medida])
            registro[sexo] = self.cambios.reemplazar_sexo(registro[sexo])
            registro[municipio] = self.cambios.reemplazar_municipio(registro[municipio])
            registro[zona_residencia] = self.cambios.reemplazar_zona_residencial(registro[zona_residencia])
        return lista_us

    def af_reemplazar(self, lista_af, rips_id):
        tipo_id = TransaccionesColumnasEnum.AF.obtener_tipo_id
        codigo_prestador = TransaccionesColumnasEnum.AF.obtener_codigo_prestador
        for registro in lista_af:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id_prestador(registro[tipo_id])
            registro[codigo_prestador] = rips_id
        return lista_af

    def ct_reemplazar(self, lista_ct, rips_id):
        codigo_prestador = ControlColumnasEnum.CT.obtener_codigo_prestador_posicion
        for registro in lista_ct:
            registro[codigo_prestador] = rips_id
        return lista_ct

    def ac_reemplazar(self, lista_ac):
        tipo_id = ConsultaColumnasEnum.AC.obtener_tipo_id
        codigo_consulta = ConsultaColumnasEnum.AC.obtener_codigo_consulta
        finalidad_consulta = ConsultaColumnasEnum.AC.obtener_finalidad_consulta
        causa_externa = ConsultaColumnasEnum.AC.obtener_causa_externa
        codigo_diagnostico_principal = ConsultaColumnasEnum.AC.obtener_diagnostico_principal
        cod_diagnostico_rel_1 = ConsultaColumnasEnum.AC.obtener_diagnostico_relacionado_1
        cod_diagnostico_rel_2 = ConsultaColumnasEnum.AC.obtener_diagnostico_relacionado_2
        cod_diagnostico_rel_3 = ConsultaColumnasEnum.AC.obtener_diagnostico_relacionado_3
        tipo_diagnostico = ConsultaColumnasEnum.AC.obtener_tipo_diagnostico

        for registro in lista_ac:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id(registro[tipo_id])
            registro[codigo_consulta] = self.cambios.reemplazar_cups(registro[codigo_consulta])
            registro[finalidad_consulta] = self.cambios.reemplazar_finalidad_consulta(registro[finalidad_consulta])
            registro[causa_externa] = self.cambios.reemplazar_causa_externa(registro[causa_externa])
            registro[codigo_diagnostico_principal] = self.cambios.reemplazar_cie10(
                registro[codigo_diagnostico_principal])
            if registro[cod_diagnostico_rel_1]:
                registro[cod_diagnostico_rel_1] = self.cambios.reemplazar_cie10(registro[cod_diagnostico_rel_1])
            else:
                registro[cod_diagnostico_rel_1] = None
            if registro[cod_diagnostico_rel_2]:
                registro[cod_diagnostico_rel_2] = self.cambios.reemplazar_cie10(registro[cod_diagnostico_rel_2])
            else:
                registro[cod_diagnostico_rel_2] = None
            if registro[cod_diagnostico_rel_3]:
                registro[cod_diagnostico_rel_3] = self.cambios.reemplazar_cie10(registro[cod_diagnostico_rel_3])
            else:
                registro[cod_diagnostico_rel_3] = None
            registro[tipo_diagnostico] = self.cambios.reemplazar_tipo_diagnostico(registro[tipo_diagnostico])
        return lista_ac

    def ap_reemplazar(self, lista_ap):
        tipo_id = ProcedimientosColumnasEnum.AP.obtener_tipo_id
        codigo_procedimiento = ProcedimientosColumnasEnum.AP.obtener_codigo_procedimiento
        ambito = ProcedimientosColumnasEnum.AP.obtener_ambito
        finalidad_procedimiento = ProcedimientosColumnasEnum.AP.obtener_finalidad_procedimiento
        personal_atiende = ProcedimientosColumnasEnum.AP.obtener_personal_que_atendio
        codigo_diagnostico = ProcedimientosColumnasEnum.AP.obtener_diagnostico_principal
        diagnostico_relacionado = ProcedimientosColumnasEnum.AP.obtener_diagnostico_relacionado_1
        complicacion = ProcedimientosColumnasEnum.AP.obtener_complicacion
        acto_quirurgico = ProcedimientosColumnasEnum.AP.obtener_realizacion_act_quirurgico
        for registro in lista_ap:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id(registro[tipo_id])
            registro[codigo_procedimiento] = self.cambios.reemplazar_cups(registro[codigo_procedimiento])
            registro[ambito] = self.cambios.reemplazar_ambito(registro[ambito])
            registro[finalidad_procedimiento] = self.cambios.reemplazar_finalidad_procedimiento(
                registro[finalidad_procedimiento])
            if registro[personal_atiende]:
                registro[personal_atiende] = self.cambios.reemplazar_personal_atiende(registro[personal_atiende])
            else:
                registro[personal_atiende] = None
            if registro[codigo_diagnostico]:
                registro[codigo_diagnostico] = self.cambios.reemplazar_cie10(registro[codigo_diagnostico])
            else:
                registro[codigo_diagnostico] = None
            if registro[diagnostico_relacionado]:
                registro[diagnostico_relacionado] = self.cambios.reemplazar_cie10(registro[diagnostico_relacionado])
            else:
                registro[diagnostico_relacionado] = None
            if registro[complicacion]:
                registro[complicacion] = self.cambios.reemplazar_cie10(registro[complicacion])
            else:
                registro[complicacion] = None
            if registro[acto_quirurgico]:
                registro[acto_quirurgico] = self.cambios.reemplazar_forma_quirurjico(registro[acto_quirurgico])
            else:
                registro[acto_quirurgico] = None
        return lista_ap

    def au_reemplazar(self, lista_au):
        tipo_id = UrgenciasColumnasEnum.AU.obtener_tipo_id
        causa_externa = UrgenciasColumnasEnum.AU.obtener_causa_externa
        diagnostico_salida = UrgenciasColumnasEnum.AU.obtener_diagnostico_principal
        diagnostico_salida_rel1 = UrgenciasColumnasEnum.AU.obtener_diagnostico_relacionado_1
        diagnostico_salida_rel2 = UrgenciasColumnasEnum.AU.obtener_diagnostico_relacionado_2
        diagnostico_salida_rel3 = UrgenciasColumnasEnum.AU.obtener_diagnostico_relacionado_3
        destino_usuario = UrgenciasColumnasEnum.AU.obtener_destino_usuario
        estado_salida = UrgenciasColumnasEnum.AU.obtener_hdestino_usuario
        causa_muerte = UrgenciasColumnasEnum.AU.obtener_causa_muerte
        for registro in lista_au:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id(registro[tipo_id])
            registro[causa_externa] = self.cambios.reemplazar_causa_externa(registro[causa_externa])
            registro[diagnostico_salida] = self.cambios.reemplazar_cie10(registro[diagnostico_salida])
            if registro[diagnostico_salida_rel1]:
                registro[diagnostico_salida_rel1] = self.cambios.reemplazar_cie10(registro[diagnostico_salida_rel1])
            else:
                registro[diagnostico_salida_rel1] = None
            if registro[diagnostico_salida_rel2]:
                registro[diagnostico_salida_rel2] = self.cambios.reemplazar_cie10(registro[diagnostico_salida_rel2])
            else:
                registro[diagnostico_salida_rel2] = None
            if registro[diagnostico_salida_rel3]:
                registro[diagnostico_salida_rel3] = self.cambios.reemplazar_cie10(registro[diagnostico_salida_rel3])
            else:
                registro[diagnostico_salida_rel3] = None
            registro[destino_usuario] = self.cambios.reemplazar_destino_usuario(registro[destino_usuario])
            registro[estado_salida] = self.cambios.reemplazar_estado_salida(registro[estado_salida])
            if registro[causa_muerte]:
                registro[causa_muerte] = self.cambios.reemplazar_cie10(registro[causa_muerte])
            else:
                registro[causa_muerte] = None
        return lista_au

    def ah_reemplazar(self, lista_ah):
        tipo_id = HospitalizacionesColumnasEnum.AH.obtener_tipo_id
        via_ingreso = HospitalizacionesColumnasEnum.AH.obtener_via_ingreso
        causa_externa = HospitalizacionesColumnasEnum.AH.obtener_causa_externa
        diagnostico_principal_ingreso = HospitalizacionesColumnasEnum.AH.obtener_diagnostico_principal_ingreso
        diagnostico_principal_egreso = HospitalizacionesColumnasEnum.AH.obtener_diagnostico_principal_egreso
        diagnostico_relacionado1 = HospitalizacionesColumnasEnum.AH.obtener_diagnostico_relacionado_1
        diagnostico_relacionado2 = HospitalizacionesColumnasEnum.AH.obtener_diagnostico_relacionado_2
        diagnostico_relacionado3 = HospitalizacionesColumnasEnum.AH.obtener_diagnostico_relacionado_3
        diagnostico_complicacion = HospitalizacionesColumnasEnum.AH.obtener_complicacion
        estado_salida = HospitalizacionesColumnasEnum.AH.obtener_estado_salida
        causa_muerte = HospitalizacionesColumnasEnum.AH.obtener_causa_muerte

        for registro in lista_ah:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id(registro[tipo_id])
            registro[via_ingreso] = self.cambios.reemplazar_via_ingreso(registro[via_ingreso])
            registro[causa_externa] = self.cambios.reemplazar_causa_externa(registro[causa_externa])
            registro[diagnostico_principal_ingreso] = self.cambios.reemplazar_cie10(
                registro[diagnostico_principal_ingreso])
            registro[diagnostico_principal_egreso] = self.cambios.reemplazar_cie10(
                registro[diagnostico_principal_egreso])
            if registro[diagnostico_relacionado1]:
                registro[diagnostico_relacionado1] = self.cambios.reemplazar_cie10(registro[diagnostico_relacionado1])
            else:
                registro[diagnostico_relacionado1] = None
            if registro[diagnostico_relacionado2]:
                registro[diagnostico_relacionado2] = self.cambios.reemplazar_cie10(registro[diagnostico_relacionado2])
            else:
                registro[diagnostico_relacionado2] = None
            if registro[diagnostico_relacionado3]:
                registro[diagnostico_relacionado3] = self.cambios.reemplazar_cie10(registro[diagnostico_relacionado3])
            else:
                registro[diagnostico_relacionado3] = None
            if registro[diagnostico_complicacion]:
                registro[diagnostico_complicacion] = self.cambios.reemplazar_cie10(registro[diagnostico_complicacion])
            else:
                registro[diagnostico_complicacion] = None
            registro[estado_salida] = self.cambios.reemplazar_estado_salida(registro[estado_salida])
            if registro[causa_muerte]:
                registro[causa_muerte] = self.cambios.reemplazar_cie10(registro[causa_muerte])
            else:
                registro[causa_muerte] = None
        return lista_ah

    def an_reemplazar(self, lista_an):
        tipo_id = RecienNacidosColumnaEnum.AN.obtener_tipo_id_madre
        control_prenatal = RecienNacidosColumnaEnum.AN.obtener_control_prenatal
        sexo = RecienNacidosColumnaEnum.AN.obtener_sexo_nacido
        diagnostico_recien_nacido = RecienNacidosColumnaEnum.AN.obtener_diagnostico_de_nacido  #
        causa_basica_muerte = RecienNacidosColumnaEnum.AN.obtener_causa_de_muerte  #
        for registro in lista_an:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id(registro[tipo_id])
            registro[control_prenatal] = self.cambios.reemplazar_control_prenatal(registro[control_prenatal])
            registro[sexo] = self.cambios.reemplazar_sexo(registro[sexo])
            if registro[diagnostico_recien_nacido]:
                registro[diagnostico_recien_nacido] = self.cambios.reemplazar_cie10(registro[diagnostico_recien_nacido])
            else:
                registro[diagnostico_recien_nacido] = None
            if registro[causa_basica_muerte]:
                registro[causa_basica_muerte] = self.cambios.reemplazar_cie10(registro[diagnostico_recien_nacido])
            else:
                registro[causa_basica_muerte] = None
        return lista_an

    def am_reemplazar(self, lista_am):
        tipo_id = MedicamentosColumnasEnum.AM.obtener_tipo_id
        tipo_medicamento = MedicamentosColumnasEnum.AM.obtener_tipo_medicamento
        for registro in lista_am:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id(registro[tipo_id])
            registro[tipo_medicamento] = self.cambios.reemplazar_tipo_medicamento(registro[tipo_medicamento])
        return lista_am

    def at_reemplazar(self, lista_at):
        tipo_id = OtrosServiciosColumnasEnum.AT.obtener_tipo_id
        tipo_servicio = OtrosServiciosColumnasEnum.AT.obtener_tipo_servicio
        codigo_servicio = OtrosServiciosColumnasEnum.AT.obtener_codigo_servicio
        for registro in lista_at:
            registro[tipo_id] = self.cambios.reemplazar_tipo_id(registro[tipo_id])
            registro[tipo_servicio] = self.cambios.reemplazar_tipo_servicio(registro[tipo_servicio])
            registro[codigo_servicio] = self.cambios.reemplazar_cups(registro[codigo_servicio])
        return lista_at

    def ad_reemplazar(self, lista_ad):
        codigo_concepto = DescripcionAgrupadaColumnasEnum.AD.obtener_codigo_concepto
        for registro in lista_ad:
            registro[codigo_concepto] = self.cambios.reemplazar_codigo_concepto(registro[codigo_concepto])
        return lista_ad

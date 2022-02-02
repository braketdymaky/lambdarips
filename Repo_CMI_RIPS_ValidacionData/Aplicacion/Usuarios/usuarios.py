from Utilidades.Enumerados.Archivo.usuarios_enum import UsuariosColumnasEnum as Columnas
from Utilidades.Enumerados.TipoArchivo.tipo_archivo_enum import TipoArchivosEnum as TA
from Utilidades.Enumerados.TipoError.tipo_error_enum import TipoErrorEnum as TE
from Utilidades.Enumerados.Comun.tipo_id_enum import TipoIdEnum as TipoId
from Aplicacion.Base.validacion_base import ValidacionBase
from Dominio.Usuarios.usuarios import ModeloUsuarios


class ValidacionUsuarios(ValidacionBase):

    def __init__(self,listas):
        super().__init__()
        self.nombre_archivo = TA.US.obtener_nombre
        self.model = ModeloUsuarios.obtener_instancia()
        self.metodos_de_validacion_a_ignorar = []
        self.lista_errores = []
        self.codigo_habilitacion = ''
        self.listas_archivos_registros=listas

    def validar_identificaciones_archivos(self, us_fila, linea_fila):
        lista_ac = self.listas_archivos_registros[TA.AC.obtener_nombre]
        lista_ap = self.listas_archivos_registros[TA.AP.obtener_nombre]
        lista_au = self.listas_archivos_registros[TA.AU.obtener_nombre]
        lista_ah = self.listas_archivos_registros[TA.AH.obtener_nombre]
        lista_an = self.listas_archivos_registros[TA.AN.obtener_nombre]
        lista_am = self.listas_archivos_registros[TA.AM.obtener_nombre]
        lista_at = self.listas_archivos_registros[TA.AT.obtener_nombre]
        listas = [lista_ac, lista_ap, lista_au, lista_ah, lista_an, lista_am, lista_at]
        numero_identificacion = us_fila[Columnas.US.obtener_numero_id]
        existencia = False
        for lista in listas:
            if lista:
                for fila in lista:
                    if numero_identificacion in fila:
                        existencia = True
                        break
                if existencia:
                    break

        if not existencia:
            self.detectar_error(TE.US_IDENTIFICACION_NO_REPORTADO.obtener_descripcion,
                                Columnas.US.obtener_numero_id, linea_fila)

    def validar_tipo_id(self, us_fila, linea_fila):
        tipo_id = [us_fila[Columnas.US.obtener_tipo_id]]
        fichero_tipo_id = self.model_fichero.obtener_tipo_id_usuario()
        if tipo_id not in fichero_tipo_id:
            self.detectar_error(TE.US_TIPO_IDENTIFICACION_NO_ENCONTRADA.obtener_descripcion,
                                Columnas.US.obtener_tipo_id, linea_fila)

    def validar_long_id_cc_ms(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        numero_identificacion = us_fila[Columnas.US.obtener_numero_id]
        if tipo_id == TipoId.CC.obtener_nombre or tipo_id == TipoId.AS.obtener_nombre:
            longitud_requerida = TipoId.CC.obtener_longitud
            if len(numero_identificacion) > longitud_requerida:
                self.detectar_error(TE.US_ID_LONGITUD_CC_MS.obtener_descripcion, Columnas.US.obtener_numero_id,
                                    linea_fila)

    def validar_long_id_ce(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        numero_identificacion = us_fila[Columnas.US.obtener_numero_id]
        if tipo_id == TipoId.CE.obtener_nombre:
            longitud_requerida = TipoId.CC.obtener_longitud
            if len(numero_identificacion) > longitud_requerida:
                self.detectar_error(TE.US_ID_LONGITUD_CE.obtener_descripcion, Columnas.US.obtener_numero_id, linea_fila)

    def validar_long_id_pa_cd_sc(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        numero_identificacion = us_fila[Columnas.US.obtener_numero_id]
        if tipo_id == TipoId.PA.obtener_nombre or tipo_id == TipoId.CD.obtener_nombre \
                or tipo_id == TipoId.SC.obtener_nombre:
            longitud_requerida = TipoId.PA.obtener_longitud
            if len(numero_identificacion) > longitud_requerida:
                self.detectar_error(TE.US_ID_LONGITUD_PA_CD_SC.obtener_descripcion, Columnas.US.obtener_numero_id,
                                    linea_fila)

    def validar_long_id_rc_ti(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        numero_identificacion = us_fila[Columnas.US.obtener_numero_id]
        if tipo_id == TipoId.RC.obtener_nombre or tipo_id == TipoId.TI.obtener_nombre:
            longitud_requerida = TipoId.RC.obtener_longitud
            if len(numero_identificacion) > longitud_requerida:
                self.detectar_error(TE.US_ID_LONGITUD_RC_TI.obtener_descripcion, Columnas.US.obtener_numero_id,
                                    linea_fila)

    def validar_long_id_as(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        numero_identificacion = us_fila[Columnas.US.obtener_numero_id]
        if tipo_id == TipoId.AS.obtener_nombre:
            longitud_requerida = TipoId.AS.obtener_longitud
            if len(numero_identificacion) > longitud_requerida:
                self.detectar_error(TE.US_ID_LONGITUD_AS.obtener_descripcion, Columnas.US.obtener_numero_id, linea_fila)

    def validar_long_id_cn(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        numero_identificacion = us_fila[Columnas.US.obtener_numero_id]
        if tipo_id == TipoId.CN.obtener_nombre:
            longitud_requerida = TipoId.CN.obtener_longitud
            if len(numero_identificacion) > longitud_requerida:
                self.detectar_error(TE.US_ID_LONGITUD_CN.obtener_descripcion, Columnas.US.obtener_numero_id, linea_fila)

    def validar_long_id_pe(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        numero_identificacion = us_fila[Columnas.US.obtener_numero_id]
        if tipo_id == TipoId.PE.obtener_nombre:
            longitud_requerida = TipoId.PE.obtener_longitud
            if len(numero_identificacion) > longitud_requerida:
                self.detectar_error(TE.US_ID_LONGITUD_PE.obtener_descripcion, Columnas.US.obtener_numero_id, linea_fila)

    def validar_codigo_eapb(self, us_fila, linea_fila):
        codigo_entidad = us_fila[Columnas.US.obtener_codigo_prestador]
        fichero_eapb = self.model_fichero.obtener_eapb()
        encontrado = list(filter(lambda campo_eapb: campo_eapb[1] == codigo_entidad, fichero_eapb))
        if not encontrado:
            self.detectar_error(TE.US_EAPB_INVALIDO.obtener_descripcion, Columnas.US.obtener_codigo_prestador,
                                linea_fila)

    def validar_codigo_eps(self, us_fila, linea_fila):
        codigo_entidad = us_fila[Columnas.US.obtener_codigo_prestador]
        codigo_eps = self.model.obtener_id_cliente()
        if not codigo_entidad == codigo_eps:
            self.detectar_error(TE.US_EAPB_INCORRECTO.obtener_descripcion, Columnas.US.obtener_codigo_prestador,
                                linea_fila)

    def validar_tipo_usuario(self, us_fila, linea_fila):
        tipo_usuario = [us_fila[Columnas.US.obtener_tipo_usuario]]
        fichero_tipo_usuario = self.model_fichero.obtener_tipo_usuario()
        if tipo_usuario not in fichero_tipo_usuario:
            self.detectar_error(TE.US_TIPO_USUARIO_INVALIDO.obtener_descripcion, Columnas.US.obtener_tipo_usuario,
                                linea_fila)

    def validar_unidad_medida(self, us_fila, linea_fila):
        unidad_medida = [us_fila[Columnas.US.obtener_medida_de_edad]]
        fichero_unidad_medida = self.model_fichero.obtener_unidad_medida()
        if unidad_medida not in fichero_unidad_medida:
            self.detectar_error(TE.US_UNIDAD_MEDIDA_INVALIDA.obtener_descripcion, Columnas.US.obtener_medida_de_edad,
                                linea_fila)

    def validar_edad_segun_unidad_medida_1(self, us_fila, linea_fila):
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if unidad_medida == '1':
            if edad < 1 or edad > 120:
                self.detectar_error(TE.US_EDAD_UNIDAD_MEDIDA_1.obtener_descripcion, Columnas.US.obtener_edad,
                                    linea_fila)

    def validar_edad_segun_unidad_medida_2(self, us_fila, linea_fila):
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if unidad_medida == '2':
            if edad < 1 or edad > 11:
                self.detectar_error(TE.US_EDAD_UNIDAD_MEDIDA_2.obtener_descripcion, Columnas.US.obtener_edad,
                                    linea_fila)

    def validar_edad_segun_unidad_medida_3(self, us_fila, linea_fila):
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if unidad_medida == '3':
            if edad < 1 or edad > 29:
                self.detectar_error(TE.US_EDAD_UNIDAD_MEDIDA_3.obtener_descripcion, Columnas.US.obtener_edad,
                                    linea_fila)

    def validar_tipo_id_edad_um_1(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        if unidad_medida == '3' and tipo_id != TipoId.PE.obtener_nombre:
            if not (tipo_id == TipoId.RC.obtener_nombre or tipo_id == TipoId.MS.obtener_nombre or
                    tipo_id == TipoId.PA.obtener_nombre or tipo_id == TipoId.CN.obtener_nombre):
                self.detectar_error(TE.US_TIPO_ID_EDAD_UM_1.obtener_descripcion, Columnas.US.obtener_medida_de_edad,
                                    linea_fila)

    def validar_tipo_id_edad_um_2(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        if unidad_medida == '2' and tipo_id != TipoId.PE.obtener_nombre:
            if (tipo_id == TipoId.CC.obtener_nombre or tipo_id == TipoId.TI.obtener_nombre
                    or tipo_id == TipoId.AS.obtener_nombre):
                self.detectar_error(TE.US_TIPO_ID_EDAD_UM_2.obtener_descripcion, Columnas.US.obtener_medida_de_edad,
                                    linea_fila)

    def validar_tipo_id_edad_um_3(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if tipo_id == TipoId.RC.obtener_nombre and unidad_medida == '1':
            if not (0 < edad < 18):
                self.detectar_error(TE.US_TIPO_ID_EDAD_UM_3.obtener_descripcion, Columnas.US.obtener_medida_de_edad,
                                    linea_fila)

    def validar_tipo_id_edad_um_4(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if tipo_id == TipoId.MS.obtener_nombre or tipo_id == TipoId.CN.obtener_nombre:
            if unidad_medida == '3' and 0 < edad < 30:
                pass
            else:
                if unidad_medida == '2' and 0 < edad < 4:
                    pass
                else:
                    self.detectar_error(TE.US_TIPO_ID_EDAD_UM_4.obtener_descripcion, Columnas.US.obtener_edad,
                                        linea_fila)

    def validar_tipo_id_edad_um_5(self, us_fila, linea_fila):
        fichero_tipo_id = self.model_fichero.obtener_tipo_id_usuario()
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if edad > 17 and unidad_medida == '1' and tipo_id != TipoId.PE.obtener_nombre:
            if [tipo_id] in fichero_tipo_id:
                if tipo_id == TipoId.RC.obtener_nombre or tipo_id == TipoId.TI.obtener_nombre or tipo_id == TipoId.MS.obtener_nombre or tipo_id == TipoId.CN.obtener_nombre:
                    self.detectar_error(TE.US_TIPO_ID_EDAD_UM_5.obtener_descripcion, Columnas.US.obtener_edad,
                                        linea_fila)

    def validar_tipo_id_edad_um_6(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if tipo_id == TipoId.AS.obtener_nombre or tipo_id == TipoId.CC.obtener_nombre and unidad_medida == '1':
            if not edad > 17:
                self.detectar_error(TE.US_TIPO_ID_EDAD_UM_6.obtener_descripcion, Columnas.US.obtener_edad, linea_fila)

    def validar_tipo_id_edad_um_7(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if 6 < edad < 18 and tipo_id != TipoId.PE.obtener_nombre and unidad_medida == '1':
            if not tipo_id == TipoId.TI.obtener_nombre:
                self.detectar_error(TE.US_TIPO_ID_EDAD_UM_7.obtener_descripcion, Columnas.US.obtener_edad,
                                    linea_fila)

    def validar_tipo_id_edad_um_8(self, us_fila, linea_fila):
        tipo_id = us_fila[Columnas.US.obtener_tipo_id]
        unidad_medida = us_fila[Columnas.US.obtener_medida_de_edad]
        edad = int(us_fila[Columnas.US.obtener_edad])
        if edad < 7 and tipo_id != TipoId.PE.obtener_nombre and unidad_medida == '1':
            if not tipo_id == TipoId.RC.obtener_nombre:
                self.detectar_error(TE.US_TIPO_ID_EDAD_UM_8.obtener_descripcion, Columnas.US.obtener_edad,
                                    linea_fila)

    def validar_sexo(self, us_fila, linea_fila):
        sexo = [us_fila[Columnas.US.obtener_sexo]]
        fichero_sexo = self.model_fichero.obtener_sexo()
        if sexo not in fichero_sexo:
            self.detectar_error(TE.US_SEXO_INVALIDO.obtener_descripcion, Columnas.US.obtener_sexo, linea_fila)

    def validar_departamento(self, us_fila, linea_fila):
        departamento = [us_fila[Columnas.US.obtener_departamento_residencia]]
        fichero_departamento = self.model_fichero.obtener_departmamento()
        if departamento not in fichero_departamento:
            self.detectar_error(TE.US_DEPARTAMENTO_INVALIDO.obtener_descripcion,
                                Columnas.US.obtener_departamento_residencia, linea_fila)

    def validar_municipio(self, us_fila, linea_fila):
        municipio = [us_fila[Columnas.US.obtener_municipio_residencia]]
        fichero_municipio = self.model_fichero.obtener_municipio()
        if municipio not in fichero_municipio:
            self.detectar_error(TE.US_MUNICIPIO_INVALIDO.obtener_descripcion, Columnas.US.obtener_municipio_residencia,
                                linea_fila)

    def validar_zona_residencial(self, us_fila, linea_fila):
        zona_residencial = [us_fila[Columnas.US.obtener_zona_residencial]]
        fichero_zona_residencial = self.model_fichero.obtener_zona_residencial()
        if zona_residencial not in fichero_zona_residencial:
            self.detectar_error(TE.US_ZONA_RESIDENCIAL.obtener_descripcion, Columnas.US.obtener_zona_residencial,
                                linea_fila)

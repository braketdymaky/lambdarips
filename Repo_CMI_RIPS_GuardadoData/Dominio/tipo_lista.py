class TipoLista:
    __instance = None
    __tipo_usuario = {}
    __tipo_id_usuario = {}
    __unidad_medida = {}
    __zona_residencial = {}
    __sexo = {}
    __tipo_id_prestador = {}
    __codigo_concepto = {}
    __finalidad_consulta = {}
    __diagnostico_principal = {}
    __control_prenatal = {}
    __causa_externa = {}
    __tipo_medicamento = {}
    __tipo_servicio = {}
    __cie10 = {}
    __forma_acto_quirurjico = {}
    __personal_atiende = {}
    __ambito_procedimiento = {}
    __finalidad_procedimiento = {}
    __cups = {}
    __via_ingreso = {}
    __estado_salida = {}
    __destino_usuario = {}
    __municipio = {}
    __eapb = {}
    lista = []

    @classmethod
    def obtener_instancia(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def asignar_tipo_usuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario

    def obtener_tipo_usuario(self):
        return self.__tipo_usuario

    def asignar_tipo_id_usuario(self, tipo_id_usuario):
        self.__tipo_id_usuario = tipo_id_usuario

    def obtener_tipo_id_usuario(self):
        return self.__tipo_id_usuario

    def asignar_unidad_medida(self, unidad_medida):
        self.__unidad_medida = unidad_medida

    def obtener_unidad_medida(self):
        return self.__unidad_medida

    def asignar_zona_residencial(self, zona_residencial):
        self.__zona_residencial = zona_residencial

    def obtener_zona_residencial(self):
        return self.__zona_residencial

    def asignar_sexo(self, sexo):
        self.__sexo = sexo

    def obtener_sexo(self):
        return self.__sexo

    def asignar_tipo_id_prestador(self, tipo_id_prestador):
        self.__tipo_id_prestador = tipo_id_prestador

    def obtener_tipo_id_prestador(self):
        return self.__tipo_id_prestador

    def asignar_codigo_concepto(self, codigo_concepto):
        self.__codigo_concepto = codigo_concepto

    def obtener_codigo_concepto(self):
        return self.__codigo_concepto

    def asignar_finalidad_consulta(self, finalidad_consulta):
        self.__finalidad_consulta = finalidad_consulta

    def obtener_finalidad_consulta(self):
        return self.__finalidad_consulta

    def asignar_diagnostico_principal(self, tipo_archivo):
        self.__diagnostico_principal = tipo_archivo

    def obtener_diagnostico_principal(self):
        return self.__diagnostico_principal

    def asignar_control_prenatal(self, control_prenatal):
        self.__control_prenatal = control_prenatal

    def obtener_control_prenatal(self):
        return self.__control_prenatal

    def asignar_causa_externa(self, causa_externa):
        self.__causa_externa = causa_externa

    def obtener_causa_externa(self):
        return self.__causa_externa

    def asignar_tipo_medicamento(self, tipo_medicamento):
        self.__tipo_medicamento = tipo_medicamento

    def obtener_tipo_medicamento(self):
        return self.__tipo_medicamento

    def asignar_tipo_servicio(self, tipo_servicio):
        self.__tipo_servicio = tipo_servicio

    def obtener_tipo_servicio(self):
        return self.__tipo_servicio

    def asignar_cie10(self, cie10):
        self.__cie10 = cie10

    def obtener_cie10(self):
        return self.__cie10

    def asignar_forma_acto_quirurjico(self, forma_acto_quirurjico):
        self.__forma_acto_quirurjico = forma_acto_quirurjico

    def obtener_forma_acto_quirurjico(self):
        return self.__forma_acto_quirurjico

    def asignar_personal_atiende(self, personal_atiende):
        self.__personal_atiende = personal_atiende

    def obtener_personal_atiende(self):
        return self.__personal_atiende

    def asignar_ambito_procedimiento(self, ambito_procedimiento):
        self.__ambito_procedimiento = ambito_procedimiento

    def obtener_ambito_procedimiento(self):
        return self.__ambito_procedimiento

    def asignar_finalidad_procedimiento(self, finalidad_procedimiento):
        self.__finalidad_procedimiento = finalidad_procedimiento

    def obtener_finalidad_procedimiento(self):
        return self.__finalidad_procedimiento

    def asignar_cups(self, cups):
        self.__cups = cups

    def obtener_cups(self):
        return self.__cups

    def asignar_via_ingreso(self, via_ingreso):
        self.__via_ingreso = via_ingreso

    def obtener_via_ingreso(self):
        return self.__via_ingreso

    def asignar_estado_salida(self, estado_salida):
        self.__estado_salida = estado_salida

    def obtener_estado_salida(self):
        return self.__estado_salida

    def asignar_destino_usuario(self, destino_usuario):
        self.__destino_usuario = destino_usuario

    def obtener_destino_usuario(self):
        return self.__destino_usuario

    def asignar_municipio(self, municipio):
        self.__municipio = municipio

    def obtener_municipio(self):
        return self.__municipio

    def asignar_eapb(self, eapb):
        self.__eapb = eapb

    def obtener_eapb(self):
        return self.__eapb

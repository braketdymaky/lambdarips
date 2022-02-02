from Dominio.tipo_lista import TipoLista


class Reemplazar:
    __tipo_lista = TipoLista.obtener_instancia()

    def reemplazar_tipo_id(self, campo_tipo_id):
        return self.__tipo_lista.obtener_tipo_id_usuario().get(campo_tipo_id)

    def reemplazar_tipo_id_prestador(self, campo_tipo_id):
        return self.__tipo_lista.obtener_tipo_id_prestador().get(campo_tipo_id)

    def reemplazar_tipo_usuario(self, campo_tipo_usuario):
        return self.__tipo_lista.obtener_tipo_usuario().get(campo_tipo_usuario)

    def reemplazar_eapb(self, campo_eapb):
        return self.__tipo_lista.obtener_eapb().get(campo_eapb)

    def reemplazar_unidad_medida(self, campo_u_medida):
        return self.__tipo_lista.obtener_unidad_medida().get(campo_u_medida)

    def reemplazar_sexo(self, campo_sexo):
        return self.__tipo_lista.obtener_sexo().get(campo_sexo)

    def reemplazar_municipio(self, campo_municipio):
        return self.__tipo_lista.obtener_municipio().get(campo_municipio)

    def reemplazar_zona_residencial(self, campo_zona_residencal):
        return self.__tipo_lista.obtener_zona_residencial().get(campo_zona_residencal)

    def reemplazar_cups(self, campo_cups):
        return self.__tipo_lista.obtener_cups().get(campo_cups)

    def reemplazar_finalidad_consulta(self, campo_finalidad_consulta):
        return self.__tipo_lista.obtener_finalidad_consulta().get(campo_finalidad_consulta)

    def reemplazar_causa_externa(self, campo_causa_externa):
        return self.__tipo_lista.obtener_causa_externa().get(campo_causa_externa)

    def reemplazar_cie10(self, campo_cie10):
        return self.__tipo_lista.obtener_cie10().get(campo_cie10)

    def reemplazar_tipo_diagnostico(self, campo_tipo_diagnostico):
        return self.__tipo_lista.obtener_diagnostico_principal().get(campo_tipo_diagnostico)

    def reemplazar_ambito(self, campo_ambito):
        return self.__tipo_lista.obtener_ambito_procedimiento().get(campo_ambito)

    def reemplazar_finalidad_procedimiento(self, campo_finalidad_procedimiento):
        return self.__tipo_lista.obtener_finalidad_procedimiento().get(campo_finalidad_procedimiento)

    def reemplazar_personal_atiende(self, campo_personal_atiende):
        return self.__tipo_lista.obtener_personal_atiende().get(campo_personal_atiende)

    def reemplazar_forma_quirurjico(self, campo_forma_quirurjico):
        return self.__tipo_lista.obtener_forma_acto_quirurjico().get(campo_forma_quirurjico)

    def reemplazar_destino_usuario(self, campo_destino):
        return self.__tipo_lista.obtener_destino_usuario().get(campo_destino)

    def reemplazar_estado_salida(self, campo_salida):
        return self.__tipo_lista.obtener_estado_salida().get(campo_salida)

    def reemplazar_via_ingreso(self, campo_via_ingreso):
        return self.__tipo_lista.obtener_via_ingreso().get(campo_via_ingreso)

    def reemplazar_control_prenatal(self, campo_control_prenatal):
        return self.__tipo_lista.obtener_control_prenatal().get(campo_control_prenatal)

    def reemplazar_tipo_medicamento(self, campo_tipo_medicamento):
        return self.__tipo_lista.obtener_tipo_medicamento().get(campo_tipo_medicamento)

    def reemplazar_tipo_servicio(self, campo_tipo_servicio):
        return self.__tipo_lista.obtener_tipo_servicio().get(campo_tipo_servicio)

    def reemplazar_codigo_concepto(self, campo_codigo_concepto):
        return self.__tipo_lista.obtener_codigo_concepto().get(campo_codigo_concepto)

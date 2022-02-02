from Persistencia.Conexion.conexion import BaseDatos
from Aplicacion.Consulta.consultas import Consulta
from Aplicacion.Implementacion.reemplazar import Reemplazar
from Aplicacion.Pdf.pdf import GenerarPdf
from Utilidades.Archivo.usuarios_enum import UsuariosColumnasEnum as us
from Utilidades.Archivo.transacciones_enum import TransaccionesColumnasEnum as af
from Utilidades.Archivo.control_enum import ControlColumnasEnum as ct
from Utilidades.Archivo.consulta_enum import ConsultaColumnasEnum as ac
from Utilidades.Archivo.procedimientos_enum import ProcedimientosColumnasEnum as ap
from Utilidades.Archivo.urgencias_enum import UrgenciasColumnasEnum as au
from Utilidades.Archivo.hospitalizaciones_enum import HospitalizacionesColumnasEnum as ah
from Utilidades.Archivo.recien_nacidos_enum import RecienNacidosColumnaEnum as an
from Utilidades.Archivo.medicamentos_enum import MedicamentosColumnasEnum as am
from Utilidades.Archivo.otros_servicios_enum import OtrosServiciosColumnasEnum as at
from Utilidades.Archivo.descripcion_agrupada_enum import DescripcionAgrupadaColumnasEnum as ad
import dateutil.tz
from datetime import datetime


class Almacenamiento:
    __database = BaseDatos()
    __consulta = Consulta()
    __reemplazar = Reemplazar()
    continuar = True
    __fecha_local = ''
    cursor = __database.connection.cursor()

    def insertar_rips(self, codigo_prestador, codigo_cliente, nombre_zip):
        numero_remision = nombre_zip.replace('.zip', '')
        fmt = "%Y-%m-%d %H:%M:%S"
        fecha_utc = dateutil.tz.gettz('America/Bogota')
        fecha_local = datetime.now(tz=fecha_utc).strftime(fmt)
        self.__fecha_local = fecha_local
        GenerarPdf.obtener_instancia().asignar_nombre_rips(numero_remision)
        GenerarPdf.obtener_instancia().asignar_fecha_registro(fecha_local)
        codigo_cliente = self.__reemplazar.reemplazar_eapb(codigo_cliente)
        codigo_dinamismo = self.__consulta.dinamismo_id_por_codigo(codigo_cliente)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_REGISTROS_VALIDADOS (DSNUMERO_REMISION, \n
            FEFECHA_REGISTRO, CDCLIENTES_ID, NMCODIGO_PRESTADOR, CDID_DINAMISMO) \n
            VALUES (%s, %s, %s, %s, %s)"""
            self.cursor.execute(sql, (numero_remision, fecha_local, codigo_cliente, codigo_prestador, codigo_dinamismo))
        except Exception as e:
            self.continuar = False
            print(e)

        return self.continuar

    def insertar_us(self, lista_us, rips_id):
        tipo_id = us.US.obtener_tipo_id
        numero_id = us.US.obtener_numero_id
        tipo_usuario = us.US.obtener_tipo_usuario
        primer_apellido = us.US.obtener_primer_apellido
        segundo_apellido = us.US.obtener_segundo_apellido
        primer_nombre = us.US.obtener_primer_nombre
        segundo_nombre = us.US.obtener_segundo_nombre
        edad = us.US.obtener_edad
        u_medida = us.US.obtener_medida_de_edad
        sexo = us.US.obtener_sexo
        municipio = us.US.obtener_municipio_residencia
        zona_residencia = us.US.obtener_zona_residencial
        lista_insertar = []
        for registro in lista_us:
            item = [rips_id, registro[tipo_id], registro[numero_id], registro[tipo_usuario], registro[primer_apellido],
                    registro[segundo_apellido], registro[primer_nombre], registro[segundo_nombre], registro[edad],
                    registro[u_medida], registro[sexo], registro[municipio], registro[zona_residencia]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_USUARIO (CDID_REGISTROS_VALIDADOS, CDID_TIPO_IDENTIFICACION_USUARIO,\n
            DSNUMERO_IDENTIFICACION, CDID_TIPO_USUARIO, DSPRIMER_APELLIDO,\n
             DSSSEGUNDO_APELLIDO, DSPRIMER_NOMBRE, DSSEGUNDO_NOMBRE, NMEDAD, CDID_UNIDAD_MEDIDA_EDAD, CDID_SEXO, \n
             CDID_MUNICIPIO, CDID_ZONA_RESIDENCIAL ) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_af(self, lista_af):
        rips_id = af.AF.obtener_codigo_prestador
        razon_social = af.AF.obtener_razon_social
        tipo_id = af.AF.obtener_tipo_id
        n_id = af.AF.obtener_numero_id
        n_factura = af.AF.obtener_numero_factura
        f_expedicion = af.AF.obtener_fecha_expedicion
        f_inicio = af.AF.obtener_fecha_inicio
        f_final = af.AF.obtener_fecha_final
        n_contrato = af.AF.obtener_numero_contrato
        p_beneficios = af.AF.obtener_plan_beneficios
        n_poliza = af.AF.obtener_numero_poliza
        v_copago = af.AF.obtener_valor_total
        v_comision = af.AF.obtener_valor_comision
        v_descuento = af.AF.obtener_valor_descuentos
        v_neto = af.AF.obtener_valor_neto
        lista_insertar = []
        for registro in lista_af:
            item = [registro[rips_id], registro[razon_social], registro[tipo_id], registro[n_id], registro[n_factura],
                    self.convertir_fecha(registro[f_expedicion]),self.convertir_fecha(registro[f_inicio]),self.convertir_fecha(registro[f_final]), registro[n_contrato],
                    registro[p_beneficios], registro[n_poliza], registro[v_copago], registro[v_comision],
                    registro[v_descuento], registro[v_neto]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_TRANSACCIONES (CDID_REGISTROS_VALIDADOS,DSRAZON_SOCIAL,\n
            CDID_TIPO_IDENTIFICACION_PRESTADOR,DSNUMERO_ID,DSNUMERO_FACTURA,FEFECHA_EXPEDICION,FEFECHA_INICIO,\n
            FEFECHA_FINAL,DSNUMERO_CONTRATO,DSPLAN_BENEFICIOS,DSNUMERO_POLIZA,NMVALOR_COPAGO,NMVALOR_COMISION,\n 
            NMVALOR_DESCUENTOS,NMVALOR_NETO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_ct(self, lista_ct, rips_id):
        f_remision = ct.CT.obtener_fecha_remision_posicion
        archivo_nombre = ct.CT.obtener_archivo_codigo_posicion
        c_registros = ct.CT.obtener_archivo_total_registros_posicion
        lista_insertar = []
        for registro in lista_ct:
            item = [rips_id, self.convertir_fecha(registro[f_remision]), registro[archivo_nombre], registro[c_registros]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_CONTROL (CDID_REGISTROS_VALIDADOS, FEFECHA_REMISION, DSNOMBRE_ARCHIVO,\n
            NMNUMERO_REGISTROS) VALUES (%s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_ac(self, lista_ac, rips_id):
        num_factura = ac.AC.obtener_numero_factura
        tipo_id = ac.AC.obtener_tipo_id
        num_id = ac.AC.obtener_numero_id
        f_consulta = ac.AC.obtener_fecha_consulta
        n_autorizacion = ac.AC.obtener_numero_autorizacion
        cod_consulta = ac.AC.obtener_codigo_consulta
        finalidad_consulta = ac.AC.obtener_finalidad_consulta
        causa_externa = ac.AC.obtener_causa_externa
        diag_ppal = ac.AC.obtener_diagnostico_principal
        diag_rel1 = ac.AC.obtener_diagnostico_relacionado_1
        diag_rel2 = ac.AC.obtener_diagnostico_relacionado_2
        diag_rel3 = ac.AC.obtener_diagnostico_relacionado_3
        tipo_diag = ac.AC.obtener_tipo_diagnostico
        v_consulta = ac.AC.obtener_valor_consulta
        v_cuota = ac.AC.obtener_valor_cuota_moderadora
        v_neto = ac.AC.obtener_valor_neto
        lista_insertar = []
        for registro in lista_ac:
            item = [rips_id, registro[tipo_id], registro[num_id], registro[num_factura], self.convertir_fecha(registro[f_consulta]),
                    registro[n_autorizacion], registro[cod_consulta], registro[finalidad_consulta],
                    registro[causa_externa], registro[diag_ppal], registro[diag_rel1],
                    registro[diag_rel2], registro[diag_rel3], registro[tipo_diag],
                    registro[v_consulta], registro[v_cuota], registro[v_neto]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_CONSULTA (CDID_REGISTROS_VALIDADOS,CDID_TIPO_IDENTIFICACION, \n
            DSNUMERO_IDENTIFICACION, DSNUMERO_FACTURA, FEFECHA_CONSULTA, \n
            DSNUMERO_AUTORIZACION, DSCODIGO_CONSULTA, CDID_FINALIDAD_CONSULTA, CDID_CAUSA_EXTERNA,\n
            CDID_CIE10_DIAGNOSTICO_PRINCIPAL, CDID_CIE10_DIAGNOSTICO_1, CDID_CIE10_DIAGNOSTICO_2,\n
            CDID_CIE10_DIAGNOSTICO_3, CDID_DIAGNOSTICO_PRINCIPAL, NMVALOR_CONSULTA, NMVALOR_CUOTA_MODERADORA,\n
            NMVALOR_NETO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_ap(self, lista_ap, rips_id):
        tipo_id = ap.AP.obtener_tipo_id
        num_factura = ap.AP.obtener_numero_factura
        num_id = ap.AP.obtener_numero_id
        f_procedimiento = ap.AP.obtener_fecha_procedimiento
        n_autorizacion = ap.AP.obtener_numero_autorizacion
        cups_codigo = ap.AP.obtener_codigo_procedimiento
        ambito_procedimiento = ap.AP.obtener_ambito
        fin_procedimiento = ap.AP.obtener_finalidad_procedimiento
        personal = ap.AP.obtener_personal_que_atendio
        diag_ppal = ap.AP.obtener_diagnostico_principal
        diag_rel = ap.AP.obtener_diagnostico_relacionado_1
        complicacion = ap.AP.obtener_complicacion
        forma_quirurjico = ap.AP.obtener_realizacion_act_quirurgico
        v_procedimiento = ap.AP.obtener_valor
        lista_insertar = []
        for registro in lista_ap:
            item = [rips_id, registro[tipo_id], registro[num_id], registro[num_factura], self.convertir_fecha(registro[f_procedimiento]),
                    registro[n_autorizacion], registro[cups_codigo], registro[ambito_procedimiento],
                    registro[fin_procedimiento], registro[personal], registro[diag_ppal], registro[diag_rel],
                    registro[complicacion], registro[forma_quirurjico], registro[v_procedimiento]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_PROCEDIMIENTOS (CDID_REGISTROS_VALIDADOS, CDID_TIPO_IDENTIFICACION, \n
            DSNUMERO_IDENTIFICACION, DSNUMERO_FACTURA, FEFECHA_PROCEDIMIENTO, \n
            DSNUMERO_AUTORIZACION, CDID_CUPS_CODIGO_PROCEDIMIENTO, CDID_AMBITO_PROCEDIMIENTO, \n
            CDID_FINALIDAD_PROCEDIMIENTO, CDID_PERSONAL_ATIENDE, CDID_CIE10_DIAGNOSTICO_PRINCIPAL, \n
            CDID_CIE10_DIAGNOSTICO_RELACIONADO, CDID_CIE10_COMPLICACION, CDID_FORMA_REALIZACION_ACTO_QUIRURJICO, \n
            NMVALOR_PROCEDIMIENTO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_au(self, lista_au, rips_id):
        tipo_id = au.AU.obtener_tipo_id
        num_factura = au.AU.obtener_numero_factura
        num_id = au.AU.obtener_numero_id
        f_ingreso = au.AU.obtener_fecha_ingreso
        h_ingreso = au.AU.obtener_hora_ingreso
        n_autorizacion = au.AU.obtener_numero_autorizacion
        causa_externa = au.AU.obtener_causa_externa
        diag_salida = au.AU.obtener_diagnostico_principal
        dia_rel1 = au.AU.obtener_diagnostico_relacionado_1
        dia_rel2 = au.AU.obtener_diagnostico_relacionado_2
        dia_rel3 = au.AU.obtener_diagnostico_relacionado_3
        destino_us = au.AU.obtener_destino_usuario
        estado_salida = au.AU.obtener_hdestino_usuario
        causa_muerte = au.AU.obtener_causa_muerte
        f_salida = au.AU.obtener_fecha_salida
        h_salida = au.AU.obtener_hora_salida
        lista_insertar = []
        for registro in lista_au:
            item = [rips_id, registro[tipo_id], registro[num_id], registro[num_factura],self.convertir_fecha(registro[f_ingreso]),
                    registro[h_ingreso], registro[n_autorizacion], registro[causa_externa], registro[diag_salida],
                    registro[dia_rel1], registro[dia_rel2], registro[dia_rel3], registro[destino_us],
                    registro[estado_salida], registro[causa_muerte], self.convertir_fecha(registro[f_salida]), registro[h_salida]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_URGENCIAS (CDID_REGISTROS_VALIDADOS, CDID_TIPO_IDENTIFICACION, \n
            DSNUMERO_IDENTIFICACION, DSNUMERO_FACTURA, FEFECHA_INGRESO, \n
            FEHORA_INGRESO, DSNUMERO_AUTORIZACION, CDID_CAUSA_EXTERNA, CDID_CIE10_DIAGNOSTICO_SALIDA,\n
            CDID_CIE10_DIAGNOSTICO_RELACIONADO_1, CDID_CIE10_DIAGNOSTICO_RELACIONADO_2,\n
            CDID_CIE10_DIAGNOSTICO_RELACIONADO_3, CDID_DESTINO_USUARIO,CDID_ESTADO_SALIDA, \n
            CDID_CIE10_CAUSA_BASICA_MUERTE,FEFECHA_SALIDA,FEHORA_SALIDA) \n 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            print(e)
            self.continuar = False

    def insertar_ah(self, lista_ah, rips_id):
        tipo_id = ah.AH.obtener_tipo_id
        numero_factura = ah.AH.obtener_numero_factura
        num_id = ah.AH.obtener_numero_id
        via_ingreso = ah.AH.obtener_via_ingreso
        f_ingreso = ah.AH.obtener_fecha_ingreso
        h_ingreso = ah.AH.obtener_hora_ingreso
        n_autorizacion = ah.AH.obtener_numero_autorizacion
        causa_externa = ah.AH.obtener_causa_externa
        diag_ingreso = ah.AH.obtener_diagnostico_principal_ingreso
        diag_egreso = ah.AH.obtener_diagnostico_principal_egreso
        diag_rel1 = ah.AH.obtener_diagnostico_relacionado_1
        diag_rel2 = ah.AH.obtener_diagnostico_relacionado_2
        diag_rel3 = ah.AH.obtener_diagnostico_relacionado_3
        diag_complicacion = ah.AH.obtener_complicacion
        estado_salida = ah.AH.obtener_estado_salida
        causa_muerte = ah.AH.obtener_causa_muerte
        f_salida = ah.AH.obtener_fecha_egreso
        h_salida = ah.AH.obtener_hora_egreso
        lista_insertar = []
        for registro in lista_ah:
            item = [rips_id, registro[tipo_id], registro[num_id], registro[numero_factura],
                    registro[via_ingreso], self.convertir_fecha(registro[f_ingreso]), registro[h_ingreso], registro[n_autorizacion],
                    registro[causa_externa], registro[diag_ingreso], registro[diag_egreso], registro[diag_rel1],
                    registro[diag_rel2], registro[diag_rel3], registro[diag_complicacion], registro[estado_salida],
                    registro[causa_muerte], self.convertir_fecha(registro[f_salida]), registro[h_salida]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_HOSPITALIZACIONES (CDID_REGISTROS_VALIDADOS, CDID_TIPO_IDENTIFICACION, \n
            DSNUMERO_IDENTIFICACION, DSNUMERO_FACTURA, CDID_VIA_INGRESO,FEFECHA_INGRESO,\n
            FEHORA_INGRESO,DSNUMERO_AUTORIZACION,CDID_CAUSA_EXTERNA,CDID_CIE10_DIAGNOSTICO_INGRESO, \n
            CDID_CIE10_DIAGNOSTICO_EGRESO,CDID_CIE10_DIAGNOSTICO_RELACIONADO_1,CDID_CIE10_DIAGNOSTICO_RELACIONADO_2, \n
            CDID_CIE10_DIAGNOSTICO_RELACIONADO_3,CDID_CIE10_DIAGNOSTICO_COMPLICACION,CDID_ESTADO_SALIDA, \n
            CDID_CIE10_CAUSA_BASICA_MUERTE, FEFECHA_SALIDA,FEHORA_SALIDA) \n 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_an(self, lista_an, rips_id):
        tipo_id = an.AN.obtener_tipo_id_madre
        numero_factura = an.AN.obtener_numero_factura
        num_id = an.AN.obtener_numero_id_madre
        f_nacimiento = an.AN.obtener_fecha_nacimiento
        h_nacimiento = an.AN.obtener_hora_nacimiento
        edad = an.AN.obtener_edad_gestacional
        control_prenatal = an.AN.obtener_control_prenatal
        sexo = an.AN.obtener_sexo_nacido
        peso = an.AN.obtener_peso_nacido
        diag_recien_nacido = an.AN.obtener_diagnostico_de_nacido
        causa_muerte = an.AN.obtener_causa_de_muerte
        f_muerte = an.AN.obtener_fecha_de_muerte
        h_muerte = an.AN.obtener_hora_de_muerte
        lista_insertar = []
        for registro in lista_an:
            item = [rips_id, registro[tipo_id], registro[num_id], registro[numero_factura], self.convertir_fecha(registro[f_nacimiento]),
                    registro[h_nacimiento],
                    registro[edad], registro[control_prenatal], registro[sexo], registro[peso],
                    registro[diag_recien_nacido], registro[causa_muerte], self.convertir_fecha(registro[f_muerte]), registro[h_muerte]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_RECIEN_NACIDOS (CDID_REGISTROS_VALIDADOS, CDID_TIPO_IDENTIFICACION, \n
            DSNUMERO_IDENTIFICACION, DSNUMERO_FACTURA, FEFECHA_NACIMIENTO,\n
            FEHORA_NACIMIENTO,NMEDAD_GESTIONAL,CDID_CONTROL_PRENATAL,CDID_SEXO,NMPESO,\n
            CDID_CIE10_DIAGNOSTICO_RECIEN_NACIDO,CDID_CIE10_CAUSA_MUERTE,FEFECHA_MUERTE,FEHORA_MUERTE) \n 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_am(self, lista_am, rips_id):
        tipo_id = am.AM.obtener_tipo_id
        numero_factura = am.AM.obtener_numero_factura
        num_id = am.AM.obtener_numero_id
        n_autorizacion = am.AM.obtener_numero_autorizacion
        c_medicamento = am.AM.obtener_codigo_medicamento
        tipo_medicamento = am.AM.obtener_tipo_medicamento
        nombre_generico = am.AM.obtener_nombre_generico_medicamento
        formula = am.AM.obtener_formula_farmaceutica
        concentracion = am.AM.obtener_concentracion_medicamento
        u_medida = am.AM.obtener_unidad_medida_medicamento
        n_unidades = am.AM.obtener_numero_unidades
        v_unitario = am.AM.obtener_valor_unitario
        v_total = am.AM.obtener_valor_total
        lista_insertar = []
        for registro in lista_am:
            item = [rips_id, registro[tipo_id], registro[num_id], registro[numero_factura], registro[n_autorizacion],
                    registro[c_medicamento], registro[tipo_medicamento], registro[nombre_generico], registro[formula],
                    registro[concentracion], registro[u_medida], registro[n_unidades], registro[v_unitario],
                    registro[v_total]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_MEDICAMENTO (CDID_REGISTROS_VALIDADOS, CDID_TIPO_IDENTIFICACION, \n
            DSNUMERO_IDENTIFICACION, DSNUMERO_FACTURA, DSNUMERO_AUTORIZACION,\n
            DSCODIGO_MEDICAMENTO,CDID_TIPO_MEDICAMENTO,DSNOMBRE_GENERICO,DSFORMA_FARMACEUTICA,DSCONCENTRACION,\n
            DSUNIDAD_MEDIDA,NMNUMERO_UNIDADES,NMVALOR_UNITARIO,NMVALOR_TOTAL) \n 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_at(self, lista_at, rips_id):
        numero_factura = at.AT.obtener_numero_factura
        tipo_id = at.AT.obtener_tipo_id
        num_id = at.AT.obtener_numero_id
        n_autorizacion = at.AT.obtener_numero_autorizacion
        tipo_servicio = at.AT.obtener_tipo_servicio
        cod_servicio = at.AT.obtener_codigo_servicio
        nombre_servicio = at.AT.obtener_nombre_servicio
        cantidad = at.AT.obtener_numero_unidades
        v_unitario = at.AT.obtener_valor_unitario
        v_total = at.AT.obtener_valor_total
        lista_insertar = []
        for registro in lista_at:
            item = [rips_id, registro[tipo_id], registro[num_id], registro[numero_factura], registro[n_autorizacion],
                    registro[tipo_servicio],
                    registro[cod_servicio], registro[nombre_servicio], registro[cantidad], registro[v_unitario],
                    registro[v_total]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_OTROS_SERVICIOS (CDID_REGISTROS_VALIDADOS, CDID_TIPO_IDENTIFICACION, \n 
            DSNUMERO_IDENTIFICACION, DSNUMERO_FACTURA, DSNUMERO_AUTORIZACION,\n
            CDID_TIPO_SERVICIO, DSCODIGO_SERVICIO, DSNOMBRE_SERVICIO, NMCANTIDAD, NMVALOR_UNITARIO,NMVALOR_TOTAL) \n 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def insertar_ad(self, lista_ad, rips_id):
        num_factura = ad.AD.obtener_numero_factura
        cod_concepto = ad.AD.obtener_codigo_concepto
        cantidad = ad.AD.obtener_cantidad_de_servicios
        v_unitario = ad.AD.obtener_valor_unitario
        v_total = ad.AD.obtener_valor_total
        lista_insertar = []
        for registro in lista_ad:
            item = [rips_id, registro[num_factura], registro[cod_concepto], registro[cantidad], registro[v_unitario],
                    registro[v_total]]
            registro = tuple(item)
            lista_insertar.append(registro)
        try:
            self.__database.connection.ping(reconnect=True)
            sql = """INSERT INTO TRIPS_DESCRIPCION_AGRUPADA (CDID_REGISTROS_VALIDADOS, DSNUMERO_FACTURA, \n
            CDID_CODIGO_CONCEPTO, NMCANTIDAD, NMVALOR_UNITARIO,NMVALOR_TOTAL_CONCEPTO) VALUES (%s, %s, %s, %s, %s, %s)"""
            self.cursor.executemany(sql, lista_insertar)
        except Exception as e:
            self.continuar = False
            print(e)

    def guardar_cambios(self):
        if self.continuar:
            try:
                self.__database.connection.commit()
                self.__database.connection.close()
            except Exception as e:
                print(e)
            return self.__fecha_local
        else:
            try:
                self.__database.connection.rollback()
                self.__database.connection.close()
            except Exception as e:
                print(e)
            return False

    def convertir_fecha(self,fecha):
        if fecha != "":
            return datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y-%m-%d")
        else:
            return fecha

from servicio.almacenar_fichero import AlmacenarFichero
from servicio.conexion import BaseDatos
from utilidades.fichero_enum import FicheroEnum as FE
from os.path import basename
import pymysql
import zipfile
import pickle
import os


class Tablas:
    database = BaseDatos()
    bucket = AlmacenarFichero()

    def obtener_ficheros(self):
        self.obtener_ambito_procedimiento()
        self.obtener_causa_externa()
        self.obtener_codigo_concepto()
        self.obtener_control_prenatal()
        self.obtener_destino_usuario()
        self.obtener_diagnostico_principal()
        self.obtener_estado_salida()
        self.obtener_finalidad_consulta()
        self.obtener_finalidad_procedimiento()
        self.obtener_forma_realizacion_acto_quirurjico()
        self.obtener_personal_atiende()
        self.obtener_sexo()
        self.obtener_tipo_id_prestador()
        self.obtener_tipo_id_usuario()
        self.obtener_tipo_usuario()
        self.obtener_tipo_servicio()
        self.obtener_unidad_medida_edad()
        self.obtener_via_ingreso()
        self.obtener_zona_residencial()
        self.obtener_cie10()
        self.obtener_cups()
        self.obtener_errores()
        self.obtener_tipo_medicamento()
        self.obtener_eapb()
        self.obtener_departamento()
        self.obtener_municipio()
        self.obtener_tipo_archivo()
        self.obtener_vacunas_cups()
        self.crear_zip()

    def obtener_ambito_procedimiento(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_AMBITO_PROCEDIMIENTO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.AMBITO_PROCEDIMIENTO.obtener_nombre, resultado)

    def obtener_causa_externa(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSCODIGO FROM TRIPS_CAUSA_EXTERNA""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.CAUSA_EXTERNA.obtener_nombre, resultado)

    def obtener_codigo_concepto(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSCODIGO FROM TRIPS_CODIGO_CONCEPTO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.CODIGO_CONCEPTO.obtener_nombre, resultado)

    def obtener_control_prenatal(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_CONTROL_PRENATAL""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.CONTROL_PRENATAL.obtener_nombre, resultado)

    def obtener_destino_usuario(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_DESTINO_USUARIO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.DESTINO_USUARIO.obtener_nombre, resultado)

    def obtener_diagnostico_principal(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_DIAGNOSTICO_PRINCIPAL""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.DIAGNOSTICO_PRINCIPAL.obtener_nombre, resultado)

    def obtener_estado_salida(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_ESTADO_SALIDA""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.ESTADO_SALIDA.obtener_nombre, resultado)

    def obtener_finalidad_consulta(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSCODIGO FROM TRIPS_FINALIDAD_CONSULTA""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.FINALIDAD_CONSULTA.obtener_nombre, resultado)

    def obtener_finalidad_procedimiento(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_FINALIDAD_PROCEDIMIENTO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.FINALIDAD_PROCEDIMIENTO.obtener_nombre, resultado)

    def obtener_forma_realizacion_acto_quirurjico(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_FORMA_REALIZACION_ACTO_QUIRURJICO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.FORMA_REALIZACION_ACTO_QUIRURJICO.obtener_nombre, resultado)

    def obtener_personal_atiende(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_PERSONAL_ATIENDE""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.PERSONAL_ATIENDE.obtener_nombre, resultado)

    def obtener_sexo(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSCODIGO FROM TRIPS_SEXO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.SEXO.obtener_nombre, resultado)

    def obtener_tipo_id_prestador(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSCODIGO FROM TRIPS_TIPO_IDENTIFICACION_PRESTADOR""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.TIPO_IDENTIFICACION_PRESTADOR.obtener_nombre, resultado)

    def obtener_tipo_id_usuario(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSCODIGO FROM TRIPS_TIPO_IDENTIFICACION_USUARIO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.TIPO_IDENTIFICACION_USUARIO.obtener_nombre, resultado)

    def obtener_tipo_servicio(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_TIPO_SERVICIO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.TIPO_SERVICIO.obtener_nombre, resultado)

    def obtener_tipo_usuario(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_TIPO_USUARIO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.TIPO_USUARIO.obtener_nombre, resultado)

    def obtener_unidad_medida_edad(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_UNIDAD_MEDIDA_EDAD""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.UNIDAD_MEDIDA_EDAD.obtener_nombre, resultado)

    def obtener_via_ingreso(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_VIA_INGRESO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.VIA_INGRESO.obtener_nombre, resultado)

    def obtener_zona_residencial(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSCODIGO FROM TRIPS_ZONA_RESIDENCIAL""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.ZONA_RESIDENCIAL.obtener_nombre, resultado)

    def obtener_cie10(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute(
                """SELECT DSCODIGO, DSSEXO, NMLIMITE_INFERIOR, NMLIMITE_SUPERIOR FROM TRIPS_CIE10 WHERE SNACTIVO = 1""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.CIE10.obtener_nombre, resultado)

    def obtener_cups(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSCODIGO, DSDESCRIPCION, DSNOMBRE, DSCOBERTURA FROM TRIPS_CUPS WHERE SNACTIVO = 1""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.CUPS.obtener_nombre, resultado)

    def obtener_eapb(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT DSNIT, DSCODIGO_ENTIDAD FROM TRIPS_CLIENTES_EAPB WHERE SNACTIVO = 1""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.EAPB.obtener_nombre, resultado)

    def obtener_tipo_medicamento(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute("""SELECT NMCODIGO FROM TRIPS_TIPO_MEDICAMENTO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.TIPO_MEDICAMENTO.obtener_nombre, resultado)

    def obtener_errores(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute(
                """SELECT NMNUMERO_COLUMNA, DSNOMBRE_COLUMNA, DSDESCRIPCION, DSARCHIVO, DSTIPO_ERROR FROM TRIPS_ERRORES""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.ERRORES.obtener_nombre, resultado)

    def obtener_departamento(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute(
                """SELECT DSCODIGO FROM TRIPS_DEPARTAMENTO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.DEPARTAMENTO.obtener_nombre, resultado)

    def obtener_municipio(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute(
                """SELECT DSCODIGO FROM TRIPS_MUNICIPIO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.MUNICIPIO.obtener_nombre, resultado)

    def obtener_tipo_archivo(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute(
                """SELECT DSCODIGO FROM TRIPS_TIPO_ARCHIVO""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.TIPO_ARCHIVO.obtener_nombre, resultado)

    def obtener_vacunas_cups(self):
        resultado = []
        with self.database.conn.cursor() as cur:
            cur.execute(
                """SELECT DSCODIGO FROM TRIPS_CUPS_VACUNAS""")
            self.database.conn.commit()
            cur.close()
            for fila in cur:
                resultado.append(list(fila))
            self.crear_fichero(FE.VACUNAS_CUPS.obtener_nombre, resultado)

    def crear_fichero(self, nombre_fichero, resultados):
        fichero = open("/tmp/" + nombre_fichero, "wb")
        pickle.dump(resultados, fichero)
        fichero.close()

    def crear_zip(self):
        array_archivos = os.listdir('/tmp/')
        if array_archivos:
            nombre_zip = "/tmp/Ficheros"
            zip_ficheros = zipfile.ZipFile(nombre_zip, "w")
            try:
                for item in array_archivos:
                    zip_ficheros.write("/tmp/" + item, basename(item), compress_type=zipfile.ZIP_DEFLATED)
                    os.remove("/tmp/" + item)
            finally:
                zip_ficheros.close()
                self.bucket.almacenar_fichero_s3(zip_ficheros)

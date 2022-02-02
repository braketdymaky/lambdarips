from Persistencia.Conexion.conexion import BaseDatos
from Dominio.tipo_lista import TipoLista
import pymysql


class Tablas:
    __database = BaseDatos()
    __lista = TipoLista().obtener_instancia()
    __continuar = True

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
        self.obtener_tipo_medicamento()
        self.obtener_eapb()
        self.obtener_municipio()
        return self.__continuar

    def obtener_ambito_procedimiento(self):
        resultado = []
        diccionario = {}
        try:
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_AMBITO_PROCEDIMIENTO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_ambito_procedimiento(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_causa_externa(self):
        resultado = []
        diccionario = {}
        try:
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_CAUSA_EXTERNA""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_causa_externa(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_codigo_concepto(self):
        resultado = []
        diccionario = {}
        try:
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_CODIGO_CONCEPTO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_codigo_concepto(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_control_prenatal(self):
        resultado = []
        diccionario = {}
        try:
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_CONTROL_PRENATAL""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_control_prenatal(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_destino_usuario(self):
        resultado = []
        diccionario = {}
        try:
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_DESTINO_USUARIO""")
                for fila in cur:
                    resultado.append(list(fila))
                    for obj_bd in resultado:
                        diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_destino_usuario(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_diagnostico_principal(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_DIAGNOSTICO_PRINCIPAL""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_diagnostico_principal(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_estado_salida(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_ESTADO_SALIDA""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_estado_salida(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_finalidad_consulta(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_FINALIDAD_CONSULTA""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_finalidad_consulta(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_finalidad_procedimiento(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_FINALIDAD_PROCEDIMIENTO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_finalidad_procedimiento(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_forma_realizacion_acto_quirurjico(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_FORMA_REALIZACION_ACTO_QUIRURJICO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_forma_acto_quirurjico(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_personal_atiende(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_PERSONAL_ATIENDE""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_personal_atiende(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_sexo(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_SEXO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_sexo(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_tipo_id_prestador(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_TIPO_IDENTIFICACION_PRESTADOR""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_tipo_id_prestador(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_tipo_id_usuario(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_TIPO_IDENTIFICACION_USUARIO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_tipo_id_usuario(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_tipo_servicio(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_TIPO_SERVICIO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_tipo_servicio(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_tipo_usuario(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_TIPO_USUARIO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_tipo_usuario(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_unidad_medida_edad(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_UNIDAD_MEDIDA_EDAD""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_unidad_medida(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_via_ingreso(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_VIA_INGRESO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_via_ingreso(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_zona_residencial(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_ZONA_RESIDENCIAL""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_zona_residencial(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_cie10(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_CIE10""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_cie10(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_cups(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_CUPS""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_cups(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_eapb(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO_ENTIDAD FROM TRIPS_CLIENTES_EAPB""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_eapb(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_tipo_medicamento(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, NMCODIGO FROM TRIPS_TIPO_MEDICAMENTO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_tipo_medicamento(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

    def obtener_municipio(self):
        try:
            resultado = []
            diccionario = {}
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                cur.execute("""SELECT CDID, DSCODIGO FROM TRIPS_MUNICIPIO""")
                for fila in cur:
                    resultado.append(list(fila))
                for obj_bd in resultado:
                    diccionario[obj_bd[1]] = obj_bd[0]
                self.__lista.asignar_municipio(diccionario)
        except Exception as e:
            print(e)
            self.__continuar = False
        finally:
            cur.close()

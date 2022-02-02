from Persistencia.Conexion.conexion import BaseDatos


class Consulta:
    __database = BaseDatos()
    continuar = True

    def dinamismo_id_por_codigo(self, codigo_cliente):
        try:
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                sql = """SELECT CDID FROM TRIPS_DINAMISMO WHERE CDIDCLIENTE = %s AND SNACTIVE = 1"""
                cur.execute(sql, codigo_cliente)
                for fila in cur:
                    return fila[0]
        except Exception as e:
            self.continuar = False
            print(e)
        finally:
            cur.close()

    def rips_id(self, codigo_prestador):
        try:
            with self.__database.connection.cursor() as cur:
                self.__database.connection.ping(reconnect=True)
                sql = """SELECT CDID FROM TRIPS_REGISTROS_VALIDADOS WHERE NMCODIGO_PRESTADOR = %s \n
                ORDER BY FEFECHA_REGISTRO DESC LIMIT 1"""
                cur.execute(sql, codigo_prestador)
                for fila in cur:
                    return fila[0]
        except Exception as e:
            self.continuar = False
            print(e)
        finally:
            cur.close()
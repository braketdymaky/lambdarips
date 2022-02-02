import os
from datetime import datetime

from Persistencia.Listas.lista_base_datos import ListaBaseDatos


class ValidacionGenerico:
    def validar_longitud_campo(self, campo, longitud_maxima, longitud_minima=1):
        """
        Método para validar la longitud de un campo especifico
        :param campo:
        :param longitud_maxima:
        :param longitud_minima:
        :return:
        """
        return True if longitud_minima <= len(str(campo)) <= longitud_maxima else False

    def validar_es_numerico(self,campo):
        """
        Método para validar que un campo espcifico sea númerico y entero
        :param campo:
        :return:
        """
        try:
            assert float(campo) >= 0 or int(campo) >= 0
            return True
        except AssertionError:
            return False
        except ValueError:
            return False

    def validar_formato_fecha(self, campo_fecha):
        """
        Método para validar el formato de un campo fecha
        :param campo_fecha:
        :return:
        """
        try:
            if len(campo_fecha) != 10:
                return False
            assert datetime.strptime(campo_fecha, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validar_cantidad_columnas(self, fila_archivo, cantidad_columnas):
        """
        Método para validar que la fila tenga la cantidad de columnas requerida
        :param fila_archivo:
        :param cantidad_columnas:
        :return:
        """
        return True if len(fila_archivo) == cantidad_columnas else False

    def validar_formato_hora(self, campo_hora):
        """
        Método para validar el formato de un campo hora
        :param campo_hora:
        :return:
        """
        try:
            assert datetime.strptime(campo_hora, '%H:%M')
            return True
        except ValueError:
            return False

    def validar_fecha_menor_actual(self, campo_fecha):
        """
        Método para validar que la fecha no sea superior a la actual
        :param campo_fecha:
        :return:
        """
        fecha_actual = datetime.today().date().strftime('%d/%m/%Y')
        fecha_actual = datetime.strptime(fecha_actual, '%d/%m/%Y')
        campo_fecha = datetime.strptime(campo_fecha, '%d/%m/%Y')
        return True if campo_fecha <= fecha_actual else False

    def validar_fecha_menor_fecha(self, fecha_menor, fecha_mayor):
        """
        Método para validar que la fecha_menor sea inferior a la fecha_mayor
        :param fecha_menor:
        :param fecha_mayor:
        :return:
        """
        try:
            fecha_menor = datetime.strptime(fecha_menor, '%d/%m/%Y')
            fecha_mayor = datetime.strptime(fecha_mayor, '%d/%m/%Y')
            assert fecha_menor <= fecha_mayor, 'La fecha inicial es mayor a la fecha final'
            return True
        except AssertionError as fecha_invalida:
            return False

    def crear_archivo_errores(self, lista_error, nombre_archivo):
        file = open('/tmp/' + nombre_archivo + '.txt', 'w')
        file.write('Los errores en el archivo ' + nombre_archivo + ' son:' + '\r\n\r\n')
        for item in lista_error:
            if item is not None:
                file.write((lista_error.index(item) + 1).__str__() + ' - ' + item + '\r\n\r\n')
            else:
                file.write(
                    'Se presentaron errores en el archivo ' + nombre_archivo + ', por favor, corregir los errores evidenciados para continuar.' + '\r\n\r\n')
        file.write('Por favor, corregir los errores evidenciados para continuar.')
        file.close()

    def obtener_error(self, lista_errores, nombre_archivo, tipo_error=None, posicion_columna=None):
        for error in lista_errores:
            if nombre_archivo in error:
                if posicion_columna is not None:
                    if posicion_columna in error and tipo_error in error:
                        return error[2].replace('$columna', error[1])
                else:
                    if tipo_error in error:
                        return error[2]

    def lista_fichero(self, nombre_archivo):
        lista_valores = ListaBaseDatos().obtener_lista_fichero(str(nombre_archivo))
        return lista_valores

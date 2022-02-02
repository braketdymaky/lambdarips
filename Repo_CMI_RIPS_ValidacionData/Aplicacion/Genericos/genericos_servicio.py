# -*- coding: utf-8 -*-
from datetime import datetime
import math
from Dominio.Fichero.fichero import ModeloFichero

class ValidacionGenerico:
    
    model_fichero = ModeloFichero.obtener_instancia()

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


    @staticmethod
    def validar_fecha_menor_actual(campo_fecha):
        """
        Método para validar que la fecha no sea superior a la actual
        :param campo_fecha:
        :return:
        """
        fecha_actual = datetime.today().date().strftime('%d/%m/%Y')
        fecha_actual = datetime.strptime(fecha_actual, '%d/%m/%Y')
        campo_fecha = datetime.strptime(campo_fecha, '%d/%m/%Y')
        return True if campo_fecha <= fecha_actual  else False

    @staticmethod
    def validar_fecha_menor_fecha(fecha_menor, fecha_mayor):
        """
        Método para validar que la fecha_menor sea inferior a la fecha_mayor
        :param fecha_menor:
        :param fecha_mayor:
        :return:
        """
        try:
            fecha_menor = datetime.strptime(fecha_menor, '%d/%m/%Y')
            fecha_mayor = datetime.strptime(fecha_mayor, '%d/%m/%Y')
            return True if fecha_menor <= fecha_mayor else False
            assert fecha_menor <= fecha_mayor
            
        except AssertionError:
            return False

    @staticmethod
    def validar_fecha_igual_fecha(fecha_menor, fecha_mayor):
        """
        Método para validar que la fecha_menor sea igual a la fecha_mayor
        :param fecha_menor:
        :param fecha_mayor:
        :return:
        """
        try:
            fecha_menor = datetime.strptime(fecha_menor, '%d/%m/%Y')
            fecha_mayor = datetime.strptime(fecha_mayor, '%d/%m/%Y')
            assert fecha_menor == fecha_mayor
            return True
        except AssertionError:
            return False

    @staticmethod
    def validar_hora_menor_fecha(hora_menor, hora_mayor):
        """
        Método para validar que la hora_menor sea inferion a la hora_mayor
        :param hora_menor:
        :param hora_mayor:
        :return:
        """
        try:
            hora_menor = datetime.strptime(hora_menor, '%H:%M')
            hora_mayor = datetime.strptime(hora_mayor, '%H:%M')
            assert hora_menor < hora_mayor
            return True
        except AssertionError:
            return False

    def validar_edad_con_unidad_de_medida(self, edad, unidad_medida, limite_i, limite_s):
        """
        Método para validar la edad contra los limites de restricción
        :param edad:
        :param unidad_medida:
        :param limite_i:
        :param limite_s:
        :return:
        """
        
        if not (limite_i == 000 or limite_i == 0):
            edad_en_horas = self.convertir_edad_o_limite_en_horas(edad, unidad_medida, False)
            limite_i_en_horas = self.convertir_edad_o_limite_en_horas(str(limite_i)[1:3], str(limite_i)[0], True)
            if not edad_en_horas >= limite_i_en_horas:
                return False

        if not (limite_s == 599 or limite_s == 0):
            edad_en_horas = self.convertir_edad_o_limite_en_horas(edad, unidad_medida, False)
            limite_s_en_horas = self.convertir_edad_o_limite_en_horas(str(limite_s)[1:3], str(limite_s)[0], True)
            if not edad_en_horas <= limite_s_en_horas:
                return False

        return True

    @staticmethod
    def convertir_edad_o_limite_en_horas(edad, unidad_medida, es_limite):
        """
        Método para convertir una edad o limite en horas
        :param edad:
        :param unidad_medida:
        :param es_limite:
        :return:
        """
        if es_limite:
            if unidad_medida == '1':
                return int(edad)
            elif unidad_medida == '2':
                return int(edad) * 24
            elif unidad_medida == '3':
                return int(edad) * 730.001
            else:
                return int(edad) * 8760
        else:
            if unidad_medida == '1':
                return int(edad) * 8760
            elif unidad_medida == '2':
                return int(edad) * 730.001
            else:
                return int(edad) * 24
                


    @staticmethod
    def validar_sexo(sexo_archivo, sexo_cups):
        """
        Método para validar que el sexo sea igual a otro
        :param sexo_archivo:
        :param sexo_cups:
        :return:
        """
        try:
            if (sexo_archivo=="F" and sexo_cups=="M") or (sexo_archivo == "M" and sexo_cups=="H"):
                return True
            else:
                return False
                    
        except AssertionError:
            return False

    def _redondear_hacia_abajo(self,val):
        if val < 0:
            return ((val * -1) % 1) < 0.5
        return (val % 1) < 0.5

    def _redondear_decimales(self,val):
        try:
            ndigits=1
            if ndigits > 0:
                val *= 10 ** (ndigits - 1)
            is_positive = val > 0
            tmp_val = val
            if not is_positive:
                tmp_val *= -1
            rounded_value = math.floor(tmp_val) if self._redondear_hacia_abajo(val) else math.ceil(tmp_val)
            if not is_positive:
                rounded_value *= -1
            if ndigits > 0:
                rounded_value /= 10 ** (ndigits - 1)
            return rounded_value
        except AssertionError:
            return 0
        except ValueError:
            return 0
        except IndexError:
            return 0
        

    @staticmethod
    def validar_guiones_numero_autorizacion_ap(numero_autorizacion, codigo_cups):
        """
        Método para validar la existencia de guion con el numero de autorizacion
        :param numero_autorizacion:
        :param codigo_cups:
        :return:
        """
        codigo_cups_vacunas= ModeloFichero.obtener_instancia().obtener_cups_vacunas()
        try:
            if [codigo_cups] not in codigo_cups_vacunas:
                if numero_autorizacion != "":
                    if "-" in numero_autorizacion:
                        return 1
                    else:
                        return 2
                else:
                    return 3
            else:
                return 1
        except AssertionError:
            return 2
        except ValueError:
            return 2
        except IndexError:
            return 2
    
    @staticmethod
    def validar_guiones_numero_autorizacion(numero_autorizacion, codigo_cups):
        """
        Método para validar la existencia de guion con el numero de autorizacion
        :param numero_autorizacion:
        :param codigo_cups:
        :return:
        """
        try:
            if numero_autorizacion != "":
                if "-" in numero_autorizacion:
                    return True
                else:
                    return False
            else:
                return False                
        except AssertionError:
            return False
        except ValueError:
            return False
        except IndexError:
            return False
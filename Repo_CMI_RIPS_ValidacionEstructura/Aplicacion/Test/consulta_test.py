# -*- coding: utf-8 -*-
import unittest
from Aplicacion.Consulta.consulta import ValidacionConsulta
from Utilidades.Mocks.ConsultaMock import mock
from Aplicacion.Zip import zip


class ConsultaTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.ac_diccionario)
    AC = ValidacionConsulta()

    @unittest.expectedFailure
    def test_validar_longitudes(self):
        self.AC.validar_longitudes(mock.ac_fila_uno, 1)
        self.assertEqual(self.AC.lista_errores, [], 'Error longitudes')

    def test_validar_fechas(self):
        self.AC.validar_formato_fecha(mock.ac_fila_uno, 1)
        #self.AC.validar_fechas(mock.ac_fila_errores, 1)
        self.assertEqual(self.AC.lista_errores, [], 'Error en las fechas')

    @unittest.expectedFailure
    def test_validar_numericos(self):
        #self.AC.validar_numericos(mock.ac_fila_uno, 1)
        self.AC.validar_numericos(mock.ac_fila_errores, 1)
        self.assertEqual(self.AC.lista_errores, [], 'Error númerico')

    def test_validar_cantidad_datos(self):
        self.AC.validar_cantidad_columnas(mock.ac_fila_uno, 1)
        self.assertEqual(self.AC.lista_errores, [], 'Error cantidad datos')

    def test_verificar_campos_no_nulos(self):
        self.AC.verificar_campos_no_nulos(mock.ac_fila_uno, 1)
        #self.AC.verificar_campos_no_nulos(mock.ac_fila_errores, 1)
        self.assertEqual(self.AC.lista_errores, [], 'Campos nulos')



def suite():
    suite = unittest.TestSuite()
    suite.addTest(ConsultaTest('test_validar_cantidad_datos'))
    suite.addTest(ConsultaTest('test_verificar_campos_no_nulos'))
    suite.addTest(ConsultaTest('test_validar_longitudes'))
    suite.addTest(ConsultaTest('test_validar_fechas'))
    suite.addTest(ConsultaTest('test_validar_fecha_mayor_actual'))
    suite.addTest(ConsultaTest('test_validar_numericos'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

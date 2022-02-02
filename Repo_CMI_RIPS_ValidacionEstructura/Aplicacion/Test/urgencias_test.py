# -*- coding: utf-8 -*-
import unittest
from Aplicacion.Urgencias.urgencias import ValidacionUrgencias
from Utilidades.Mocks.mock_urgencias import mock
from Aplicacion.Zip import zip


class UrgenciasTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.au_diccionario)
    AU = ValidacionUrgencias()
    def test_validar_longitudes(self):
        self.AU.lista_errores=[]
        self.AU.validar_longitud(mock.au_fila, 1)
        self.assertEqual(self.AU.lista_errores, [], 'Error longitudes')

    def test_validar_fechas(self):
        self.AU.lista_errores=[]
        self.AU.validar_formato_fecha(mock.au_fila, 1)
        self.assertEqual(self.AU.lista_errores, [], 'Error en las fechas')

    def test_validar_horas(self):
        self.AU.lista_errores=[]
        self.AU.validar_formato_hora(mock.au_fila, 1)
        self.assertEqual(self.AU.lista_errores, [], 'Error en las fechas')

    def test_validar_cantidad_datos(self):
        self.AU.lista_errores=[]
        self.AU.validar_cantidad_columnas(mock.au_fila, 1)
        self.assertEqual(self.AU.lista_errores, [], 'Error cantidad datos')

    def test_verificar_campos_no_nulos(self):
        self.AU.lista_errores=[]
        self.AU.verificar_campos_no_nulos(mock.au_fila, 1)
        self.assertEqual(self.AU.lista_errores, [],'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_fechas(self):
        self.AU.lista_errores=[]
        self.AU.validar_formato_fecha(mock.au_fila_errores,1)
        self.assertEqual(self.AU.lista_errores, [],'formato fecha invalido')

    @unittest.expectedFailure
    def test_error_verificar_campos_no_nulos(self):
        self.AU.lista_errores=[]
        self.AU.verificar_campos_no_nulos(mock.au_fila_errores, 1)
        self.assertEqual(self.AU.lista_errores, [], 'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_longitudes(self):
        self.AU.lista_errores=[]
        self.AU.validar_longitudes(mock.au_fila_errores, 1)
        self.assertEqual(self.AU.lista_errores, [], 'Error longitudes')

    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.AU.lista_errores=[]
        self.AU.validar_cantidad_datos(mock.au_fila_incompleta, 1)
        self.assertEqual(self.AU.lista_errores, [],'Error cantidad datos')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(UrgenciasTest('test_validar_cantidad_datos'))
    suite.addTest(UrgenciasTest('test_verificar_campos_no_nulos'))
    suite.addTest(UrgenciasTest('test_validar_horas'))
    suite.addTest(UrgenciasTest('test_validar_longitudes'))
    suite.addTest(UrgenciasTest('test_validar_fechas'))
    suite.addTest(UrgenciasTest('test_validar_longitudes'))
    suite.addTest(UrgenciasTest('test_error_verificar_campos_no_nulos'))
    suite.addTest(UrgenciasTest('test_error_validar_cantidad_datos'))
    suite.addTest(UrgenciasTest('test_validar_fechas'))
    suite.addTest(UrgenciasTest('test_error_validar_fechas'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

# -*- coding: utf-8 -*-
import unittest
from Aplicacion.Transacciones.transacciones import ValidacionTransacciones
from Utilidades.Mocks.mock_transacciones import mock
from Aplicacion.Zip import zip


class TransaccionesTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.af_diccionario)
    AF = ValidacionTransacciones()
    def test_validar_longitudes(self):
        self.AF.lista_errores=[]
        self.AF.validar_longitud(mock.af_fila, 1)
        self.assertEqual(self.AF.lista_errores, [], 'Error longitudes')

    def test_validar_fechas(self):
        self.AF.lista_errores=[]
        self.AF.validar_formato_fecha(mock.af_fila, 1)
        self.assertEqual(self.AF.lista_errores, [], 'Error en las fechas')


    def test_validar_cantidad_datos(self):
        self.AF.lista_errores=[]
        self.AF.validar_cantidad_columnas(mock.af_fila, 1)
        self.assertEqual(self.AF.lista_errores, [], 'Error cantidad datos')

    def test_verificar_campos_no_nulos(self):
        self.AF.lista_errores=[]
        self.AF.verificar_campos_no_nulos(mock.af_fila, 1)
        self.assertEqual(self.AF.lista_errores, [],'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_fechas(self):
        self.AF.lista_errores=[]
        self.AF.validar_formato_fecha(mock.af_fila_errores,1)
        self.assertEqual(self.AF.lista_errores, [],'formato fecha invalido')

    @unittest.expectedFailure
    def test_error_verificar_campos_no_nulos(self):
        self.AF.lista_errores=[]
        self.AF.verificar_campos_no_nulos(mock.af_fila_errores, 1)
        self.assertEqual(self.AF.lista_errores, [], 'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_longitudes(self):
        self.AF.lista_errores=[]
        self.AF.validar_longitudes(mock.af_fila_errores, 1)
        self.assertEqual(self.AF.lista_errores, [], 'Error longitudes')

    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.AF.lista_errores=[]
        self.AF.validar_cantidad_datos(mock.af_fila_incompleta, 1)
        self.assertEqual(self.AF.lista_errores, [],'Error cantidad datos')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TransaccionesTest('test_validar_cantidad_datos'))
    suite.addTest(TransaccionesTest('test_verificar_campos_no_nulos'))
    suite.addTest(TransaccionesTest('test_validar_longitudes'))
    suite.addTest(TransaccionesTest('test_validar_fechas'))
    suite.addTest(TransaccionesTest('test_validar_longitudes'))
    suite.addTest(TransaccionesTest('test_error_verificar_campos_no_nulos'))
    suite.addTest(TransaccionesTest('test_error_validar_cantidad_datos'))
    suite.addTest(TransaccionesTest('test_validar_fechas'))
    suite.addTest(TransaccionesTest('test_error_validar_fechas'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

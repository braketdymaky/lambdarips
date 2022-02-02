# -*- coding: utf-8 -*-
import unittest
from Aplicacion.RecienNacidos.recien_nacidos import ValidacionRecienNacidos
from Utilidades.Mocks.mock_recien_nacidos import mock
from Aplicacion.Zip import zip


class ProcedimientosTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.an_diccionario)
    AN = ValidacionRecienNacidos()
    def test_validar_longitudes(self):
        self.AN.lista_errores=[]
        self.AN.validar_longitud(mock.an_fila, 1)
        self.assertEqual(self.AN.lista_errores, [], 'Error longitudes')
    @unittest.expectedFailure
    def test_validar_cantidad_datos(self):
        self.AN.lista_errores=[]
        self.AN.validar_cantidad_columnas(mock.an_fila, 1)
        self.assertEqual(self.AN.lista_errores, [], 'Error cantidad datos')
    @unittest.expectedFailure
    def test_verificar_campos_no_nulos(self):
        self.AN.lista_errores=[]
        self.AN.verificar_campos_no_nulos(mock.an_fila, 1)
        self.assertEqual(self.AN.lista_errores, [],'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_fechas(self):
        self.AN.lista_errores=[]
        self.AN.validar_formato_fecha(mock.an_fila_errores,1)
        self.assertEqual(self.AN.lista_errores, [],'formato fecha invalido')

    @unittest.expectedFailure
    def test_error_verificar_campos_no_nulos(self):
        self.AN.lista_errores=[]
        self.AN.verificar_campos_no_nulos(mock.an_fila_errores, 1)
        self.assertEqual(self.AN.lista_errores, [], 'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_longitudes(self):
        self.AN.lista_errores=[]
        self.AN.validar_longitudes(mock.an_fila_errores, 1)
        self.assertEqual(self.AN.lista_errores, [], 'Error longitudes')

    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.AN.lista_errores=[]
        self.AN.validar_cantidad_datos(mock.an_fila_incompleta, 1)
        self.assertEqual(self.AN.lista_errores, [],'Error cantidad datos')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(ProcedimientosTest('test_validar_cantidad_datos'))
    suite.addTest(ProcedimientosTest('test_verificar_campos_no_nulos'))
    suite.addTest(ProcedimientosTest('test_validar_longitudes'))
    suite.addTest(ProcedimientosTest('test_validar_fechas'))
    suite.addTest(ProcedimientosTest('test_validar_longitudes'))
    suite.addTest(ProcedimientosTest('test_error_verificar_campos_no_nulos'))
    suite.addTest(ProcedimientosTest('test_error_validar_cantidad_datos'))
    suite.addTest(ProcedimientosTest('test_validar_fechas'))
    suite.addTest(ProcedimientosTest('test_error_validar_fechas'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

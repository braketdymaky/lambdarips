# -*- coding: utf-8 -*-
import unittest
from Aplicacion.Procedimientos.procedimientos import ValidacionProcedimientos
from Utilidades.Mocks.mock_procedimientos import mock
from Aplicacion.Zip import zip


class ProcedimientosTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.ap_diccionario)
    AP = ValidacionProcedimientos()
    def test_validar_longitudes(self):
        self.AP.lista_errores=[]
        self.AP.validar_longitud(mock.ap_fila, 1)
        self.assertEqual(self.AP.lista_errores, [], 'Error longitudes')

    def test_validar_fechas(self):
        self.AP.lista_errores=[]
        self.AP.validar_formato_fecha(mock.ap_fila, 1)
        self.assertEqual(self.AP.lista_errores, [], 'Error en las fechas')


    def test_validar_cantidad_datos(self):
        self.AP.lista_errores=[]
        self.AP.validar_cantidad_columnas(mock.ap_fila, 1)
        self.assertEqual(self.AP.lista_errores, [], 'Error cantidad datos')

    def test_verificar_campos_no_nulos(self):
        self.AP.lista_errores=[]
        self.AP.verificar_campos_no_nulos(mock.ap_fila, 1)
        self.assertEqual(self.AP.lista_errores, [],'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_fechas(self):
        self.AP.lista_errores=[]
        self.AP.validar_formato_fecha(mock.ap_fila_errores,1)
        self.assertEqual(self.AP.lista_errores, [],'formato fecha invalido')

    @unittest.expectedFailure
    def test_error_verificar_campos_no_nulos(self):
        self.AP.lista_errores=[]
        self.AP.verificar_campos_no_nulos(mock.ap_fila_errores, 1)
        self.assertNotEqual(self.AP.lista_errores, [], 'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_longitudes(self):
        self.AP.lista_errores=[]
        self.AP.validar_longitudes(mock.ap_fila_errores, 1)
        self.assertEqual(self.AP.lista_errores, [], 'Error longitudes')

    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.AP.lista_errores=[]
        self.AP.validar_cantidad_datos(mock.ap_fila_incompleta, 1)
        self.assertEqual(self.AP.lista_errores, [],'Error cantidad datos')

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

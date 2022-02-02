# -*- coding: utf-8 -*-
import unittest
from Aplicacion.OtrosServicios.otros_servicios import ValidacionOtrosServicios
from Utilidades.Mocks.mock_otros_servicios import mock
from Aplicacion.Zip import zip


class OtrosServiciosTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.at_diccionario)
    AT = ValidacionOtrosServicios()
    def test_validar_longitudes(self):
        self.AT.lista_errores=[]
        self.AT.validar_longitud(mock.at_fila, 1)
        self.assertEqual(self.AT.lista_errores, [], 'Error longitudes')



    def test_validar_cantidad_datos(self):
        self.AT.lista_errores=[]
        self.AT.validar_cantidad_columnas(mock.at_fila, 1)
        self.assertEqual(self.AT.lista_errores, [], 'Error cantidad datos')

    def test_verificar_campos_no_nulos(self):
        self.AT.lista_errores=[]
        self.AT.verificar_campos_no_nulos(mock.at_fila, 1)
        self.assertEqual(self.AT.lista_errores, [],'Campos nulos')

    @unittest.expectedFailure
    def test_error_verificar_campos_no_nulos(self):
        self.AT.lista_errores=[]
        self.AT.verificar_campos_no_nulos(mock.at_fila_errores, 1)
        self.assertEqual(self.AT.lista_errores, [], 'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_longitudes(self):
        self.AT.lista_errores=[]
        self.AT.validar_longitudes(mock.at_fila_errores, 1)
        self.assertEqual(self.AT.lista_errores, [], 'Error longitudes')

    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.AT.lista_errores=[]
        self.AT.validar_cantidad_datos(mock.at_fila_incompleta, 1)
        self.assertEqual(self.AT.lista_errores, [],'Error cantidad datos')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(OtrosServiciosTest('test_validar_cantidad_datos'))
    suite.addTest(OtrosServiciosTest('test_verificar_campos_no_nulos'))
    suite.addTest(OtrosServiciosTest('test_validar_longitudes'))
    suite.addTest(OtrosServiciosTest('test_validar_fechas'))
    suite.addTest(OtrosServiciosTest('test_validar_longitudes'))
    suite.addTest(OtrosServiciosTest('test_error_verificar_campos_no_nulos'))
    suite.addTest(OtrosServiciosTest('test_error_validar_cantidad_datos'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

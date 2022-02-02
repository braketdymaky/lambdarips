# -*- coding: utf-8 -*-
import unittest
from Aplicacion.Hospitalizacion.hospitalizacion import ValidacionHospitalizacion
from Utilidades.Mocks.hospitalizaciones_mock import mock
from Aplicacion.Zip import zip


class HospitalizacionesTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.ah_diccionario)
    AH = ValidacionHospitalizacion()
    def test_validar_longitudes(self):
        self.AH.lista_errores=[]
        self.AH.validar_longitud(mock.ah_fila, 1)
        self.assertEqual(self.AH.lista_errores, [], 'Error longitudes')

    def test_validar_fechas(self):
        self.AH.lista_errores=[]
        self.AH.validar_formato_fecha(mock.ah_fila, 1)
        self.assertEqual(self.AH.lista_errores, [], 'Error en las fechas')

    def test_validar_horas(self):
        self.AH.lista_errores=[]
        self.AH.validar_formato_hora(mock.ah_fila, 1)
        self.assertEqual(self.AH.lista_errores, [], 'Error en las fechas')

    def test_validar_cantidad_datos(self):
        self.AH.lista_errores=[]
        self.AH.validar_cantidad_columnas(mock.ah_fila, 1)
        self.assertEqual(self.AH.lista_errores, [], 'Error cantidad datos')

    def test_verificar_campos_no_nulos(self):
        self.AH.lista_errores=[]
        self.AH.verificar_campos_no_nulos(mock.ah_fila, 1)
        self.assertEqual(self.AH.lista_errores, [],'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_fechas(self):
        self.AH.lista_errores=[]
        self.AH.validar_formato_fecha(mock.ah_fila_errores,1)
        self.assertEqual(self.AH.lista_errores, [],'formato fecha invalido')

    @unittest.expectedFailure
    def test_error_verificar_campos_no_nulos(self):
        self.AH.lista_errores=[]
        self.AH.verificar_campos_no_nulos(mock.ah_fila_errores, 1)
        self.assertEqual(self.AH.lista_errores, [], 'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_longitudes(self):
        self.AH.lista_errores=[]
        self.AH.validar_longitudes(mock.ah_fila_errores, 1)
        self.assertEqual(self.AH.lista_errores, [], 'Error longitudes')

    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.AH.lista_errores=[]
        self.AH.validar_cantidad_datos(mock.ah_fila_incompleta, 1)
        self.assertEqual(self.AH.lista_errores, [],'Error cantidad datos')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(HospitalizacionesTest('test_validar_cantidad_datos'))
    suite.addTest(HospitalizacionesTest('test_verificar_campos_no_nulos'))
    suite.addTest(HospitalizacionesTest('test_validar_horas'))
    suite.addTest(HospitalizacionesTest('test_validar_longitudes'))
    suite.addTest(HospitalizacionesTest('test_validar_fechas'))
    suite.addTest(HospitalizacionesTest('test_validar_longitudes'))
    suite.addTest(HospitalizacionesTest('test_error_verificar_campos_no_nulos'))
    suite.addTest(HospitalizacionesTest('test_error_validar_cantidad_datos'))
    suite.addTest(HospitalizacionesTest('test_validar_fechas'))
    suite.addTest(HospitalizacionesTest('test_error_validar_fechas'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

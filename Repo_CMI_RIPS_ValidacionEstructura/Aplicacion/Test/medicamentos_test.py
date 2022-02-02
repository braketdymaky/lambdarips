# -*- coding: utf-8 -*-
import unittest
from Aplicacion.Medicamentos.medicamentos import ValidacionMedicamentos
from Utilidades.Mocks.mock_medicamentos import mock
from Aplicacion.Zip import zip


class MedicamentosTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.am_diccionario)
    AM = ValidacionMedicamentos()
    def test_validar_longitudes(self):
        self.AM.lista_errores=[]
        self.AM.validar_longitud(mock.am_fila, 1)
        self.assertEqual(self.AM.lista_errores, [], 'Error longitudes')



    def test_validar_cantidad_datos(self):
        self.AM.lista_errores=[]
        self.AM.validar_cantidad_columnas(mock.am_fila, 1)
        self.assertEqual(self.AM.lista_errores, [], 'Error cantidad datos')

    def test_verificar_campos_no_nulos(self):
        self.AM.lista_errores=[]
        self.AM.verificar_campos_no_nulos(mock.am_fila, 1)
        self.assertEqual(self.AM.lista_errores, [],'Campos nulos')

    @unittest.expectedFailure
    def test_error_verificar_campos_no_nulos(self):
        self.AM.lista_errores=[]
        self.AM.verificar_campos_no_nulos(mock.am_fila_errores, 1)
        self.assertEqual(self.AM.lista_errores, [], 'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_longitudes(self):
        self.AM.lista_errores=[]
        self.AM.validar_longitudes(mock.am_fila_errores, 1)
        self.assertEqual(self.AM.lista_errores, [], 'Error longitudes')

    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.AM.lista_errores=[]
        self.AM.validar_cantidad_datos(mock.am_fila_incompleta, 1)
        self.assertEqual(self.AM.lista_errores, [],'Error cantidad datos')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MedicamentosTest('test_validar_cantidad_datos'))
    suite.addTest(MedicamentosTest('test_verificar_campos_no_nulos'))
    suite.addTest(MedicamentosTest('test_validar_longitudes'))
    suite.addTest(MedicamentosTest('test_validar_fechas'))
    suite.addTest(MedicamentosTest('test_validar_longitudes'))
    suite.addTest(MedicamentosTest('test_error_verificar_campos_no_nulos'))
    suite.addTest(MedicamentosTest('test_error_validar_cantidad_datos'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

# -*- coding: utf-8 -*-
import unittest
from Aplicacion.Usuarios.usuarios import ValidacionUsuarios
from Utilidades.Mocks.mock_usuarios import mock
from Aplicacion.Zip import zip


class UsuariosTest(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.us_diccionario)
    US  = ValidacionUsuarios()
    def test_validar_longitudes(self):
        self.US.lista_errores=[]
        self.US.validar_longitud(mock.us_fila, 1)
        self.assertEqual(self.US.lista_errores, [], 'Error longitudes')



    def test_validar_cantidad_datos(self):
        self.US.lista_errores=[]
        self.US.validar_cantidad_columnas(mock.us_fila, 1)
        self.assertEqual(self.US.lista_errores, [], 'Error cantidad datos')

    def test_verificar_campos_no_nulos(self):
        self.US.lista_errores=[]
        self.US.verificar_campos_no_nulos(mock.us_fila, 1)
        self.assertEqual(self.US.lista_errores, [],'Campos nulos')


    @unittest.expectedFailure
    def test_error_verificar_campos_no_nulos(self):
        self.US.lista_errores=[]
        self.US.verificar_campos_no_nulos(mock.us_fila_errores, 1)
        self.assertEqual(self.US.lista_errores, [], 'Campos nulos')

    @unittest.expectedFailure
    def test_error_validar_longitudes(self):
        self.US.lista_errores=[]
        self.US.validar_longitudes(mock.us_fila_errores, 1)
        self.assertEqual(self.US.lista_errores, [], 'Error longitudes')

    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.US.lista_errores=[]
        self.US.validar_cantidad_datos(mock.us_fila_incompleta, 1)
        self.assertEqual(self.US.lista_errores, [],'Error cantidad datos')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(UsuariosTest('test_validar_cantidad_datos'))
    suite.addTest(UsuariosTest('test_verificar_campos_no_nulos'))
    suite.addTest(UsuariosTest('test_validar_longitudes'))
    suite.addTest(UsuariosTest('test_error_verificar_campos_no_nulos'))
    suite.addTest(UsuariosTest('test_error_validar_cantidad_datos'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

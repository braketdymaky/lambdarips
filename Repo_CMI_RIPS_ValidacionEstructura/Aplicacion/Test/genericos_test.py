import unittest
from rips.Aplicación.Genericos.genericos import *


class TestMetodosGenericos(unittest.TestCase):

    # Test: La longitud del campo este sea coherente bajo el rango
    @unittest.expectedFailure
    def test_longitud_campo(self):
        self.assertTrue(validar_longitud_campo('prueba', 12, 4), True)
        self.assertTrue(validar_longitud_campo(1234567, 12), True)
        self.assertTrue(validar_longitud_campo(0.125678, 12), True)
        self.assertTrue(validar_longitud_campo(True, 12), True)

    # Test: Que el campo sea numerico
    @unittest.expectedFailure
    def test_campo_numerico(self):
        self.assertTrue(validar_es_numerico('prueba'), False)
        self.assertTrue(validar_es_numerico(1234567), True)
        self.assertTrue(validar_es_numerico(0.125678), False)  # Error por decimales, se puede setear como float

    # Test: El formato de la fecha debe ser dd/mm/aaaa
    @unittest.expectedFailure
    def test_formato_fecha(self):
        self.assertTrue(validar_formato_fecha('26/01/1998'), True)
        self.assertTrue(validar_formato_fecha('1998/01/26'), False)  # Error debido a error en formato

    # Test: El formato de la hora debe ser HH/MM
    @unittest.expectedFailure
    def test_formato_hora(self):
        self.assertTrue(validar_formato_hora('12:59'), True)
        self.assertTrue(validar_formato_hora('24:13'), False)  # Error debido a hora no permitida
        self.assertTrue(validar_formato_hora('12:60'), True)  # Error debido a minutos no permitidos
        self.assertTrue(validar_formato_hora('-12:60'), True)  # Error debido a valor negativo

    # Test: El formato de la hora debe ser HH/MM
    @unittest.expectedFailure
    def test_fecha_menor_actual(self):
        self.assertTrue(validar_fecha_menor_actual('26/01/1998'), True)
        self.assertTrue(validar_fecha_menor_actual('26/01/2020'), False)  # Error debido a que la fecha es superior

    # Test: El formato de la hora debe ser HH/MM
    @unittest.expectedFailure
    def test_fecha_menor_actual(self):
        self.assertTrue(validar_fecha_menor_fecha('26/01/1998', '26/01/2000'), True)
        self.assertTrue(validar_fecha_menor_fecha('26/01/2020', '26/01/2019'), False)
        # Error debido a que la fecha es superior

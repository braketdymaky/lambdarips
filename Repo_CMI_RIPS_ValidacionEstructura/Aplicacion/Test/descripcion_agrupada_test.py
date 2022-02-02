# -*- coding: utf-8 -*-
import unittest
from Aplicacion.Control.Control import ControlController
from Utilidades.Mocks.Mocks import mock

class WidgetTestCase(unittest.TestCase):

    CT=ControlController()
    CT.CT_model=mock.control_model




def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_crear_listas_para_validaciones'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

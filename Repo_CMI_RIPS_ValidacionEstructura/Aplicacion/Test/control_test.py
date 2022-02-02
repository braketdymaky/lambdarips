import unittest
from Aplicacion.Control.control import ValidacionControl
from Utilidades.Mocks.mock_control import mock
from Aplicacion.Zip import zip

class WidgetTestCase(unittest.TestCase):
    zip.ModeloZip.obtener_instancia().asignar_lista_registros_archivos(mock.ct_diccionario)
    CT=ValidacionControl()
    def setUp(self):
        self.widget = 15



    def test_validar_genericos(self):
        self.CT.lista_errores=[]
        linea=0
        for fila in mock.ct_list.return_value:
            self.CT.validar_longitud(fila,linea)
            self.CT.validar_codigo_habilitacion(fila,linea)
            self.assertEqual(self.CT.lista_errores,[],'error al validar longitud')
            self.assertEqual(self.CT.lista_errores,[],'codigo de habilitacion invalido')
            linea+=1


    def test_validar_fechas(self):
        self.CT.lista_errores=[]
        self.CT.validar_formato_fecha(mock.ct_list.return_value[0],0)
        self.assertEqual(self.CT.lista_errores,[], 'Error formato fecha invalido')
        self.assertEqual(self.CT.lista_errores,[], 'Error fecha mayor a la actual')

    def test_verificar_archivos_minimos(self):
        self.CT.lista_errores=[]
        lista_archvios=['AC1234567', 'AF1234567', 'AH1234567', 'AM1234567', 'AP1234567', 'AT1234567','AU1234567', 'CT1234567', 'US1234567']
        self.CT.verificar_archivos_minimos(lista_archvios)
        self.assertEqual(self.CT.lista_errores,[],'error el indicador del archivo es invalido')

    def test_validar_cantidad_datos(self):
        self.CT.lista_errores=[]
        self.CT.validar_cantidad_columnas(mock.ct_list.return_value[0],0)
        self.assertNotEqual(self.CT.lista_errores,[],'Cantidad de columnas invalida')

    def test_verificar_prefijo_archivos(self):
        self.CT.lista_errores=[]
        self.CT.ct_model.obtener_instancia().asignar_archvos_presentes(['AC', 'AF', 'AH', 'AM', 'AP', 'AT','AU', 'CT', 'US'])
        self.CT.verificar_prefijo_archivos()
        self.assertEqual(self.CT.lista_errores,[],"Prefijo de archivos invalido")

    def test_ejecutar_validaciones_de_estructura(self):
        self.CT.lista_errores=[]
        self.CT.verificar_archivos_minimos(['AC12345', 'AF12345', 'AH12345', 'AM12345', 'AP12345', 'AT12345','AU12345', 'CT12345', 'US12345'])
        self.CT.verificar_prefijo_archivos()
        self.CT.verificar_prefijo_archivos()
        self.assertEqual(self.CT.lista_errores,[],'error al generar variables Maestras')

    def test_validar_existencia_de_los_registros_del_ct_en_zip(self):
        self.CT.lista_errores=[]
        self.CT.validar_existencia_de_los_registros_del_ct_en_zip(mock.ct_list.return_value[0],1)
        self.assertNotEqual(self.CT.lista_errores,[],'Los archivos en el CT no coninciden con los presentes en el CT')


    @unittest.expectedFailure
    def test_error_validar_cantidad_datos(self):
        self.CT.lista_errores=[]
        self.CT.validar_cantidad_datos(mock.ct_fila_erronea,0)
        self.assertEqual(self.CT.ct_lista_errores,[], 'Cantidad de datos Invalida')

    @unittest.expectedFailure
    def test_error_validar_genericos(self):
        linea=0
        self.CT.lista_errores=[]
        self.CT.validar_longitudes(mock.ct_fila_erronea,linea)
        self.CT.validar_codigo_habilitacion(mock.ct_fila_erronea,linea)
        self.assertEqual(self.CT.ct_lista_errores,[],'error al validar longitudes y codigo de habilitacion')

    @unittest.expectedFailure
    def test_error_validar_fechas(self):
        self.CT.lista_errores=[]
        self.assertEqual(self.CT.validar_fechas(mock.ct_fila_erronea,0),True, 'Error formato fecha invalido')
        self.assertEqual(self.CT.validar_fecha_mayor_actual(mock.ct_fila_fecha_mayor_actual,0),True, 'Error fecha mayor a la actual')

    @unittest.expectedFailure
    def test_error_crear_listas_para_validaciones(self):
        self.CT.lista_errores=[]
        CT2=ValidacionControl()
        CT2.CT_model=mock.control_model
        CT2.CT_model.ct_lista={"prueba": "error"}
        CT2.construir_lista_archivos_presentes()
        CT2.almacenar_archivos_presentes()
        CT2.ejecutar_validaciones_de_estructura()
        self.assertIsInstance(CT2.CT_model.ct_fila_uno,cls=list)

    @unittest.expectedFailure
    def test_error_verificar_archivos_minimos(self):
        self.CT.lista_errores=[]
        CT2=ValidacionControl()
        CT2.CT_model=mock.control_model
        CT2.CT_model.CT_archivos_presentes=["AF"]
        CT2.verificar_archivos_minimos()
        self.assertEqual(CT2.ct_lista_errores,[],'archivos minimos no completos')


    @unittest.expectedFailure
    def test_error_validar_existencia_de_los_registros_del_ct_en_zip(self):
        self.CT.lista_errores=[]
        self.CT.validar_existencia_de_los_registros_del_ct_en_zip(mock.ct_fila_erronea,1)
        self.assertEqual(self.CT.lista_errores,[],'Los archivos en el CT no coninciden con los presentes en el CT')


    @unittest.expectedFailure
    def test_error_verificar_prefijo_archivos(self):
        self.CT.lista_errores=[]
        self.CT.CT_model.CT_archivos_presentes=['AC', 'ko']
        self.assertEqual(self.CT.verificar_prefijo_archivos(),True,"Prefijo de archivos invalido")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_verificar_archivos_minimos'))
    suite.addTest(WidgetTestCase('test_validar_genericos'))
    suite.addTest(WidgetTestCase('test_ejecutar_validaciones_de_estructura'))
    suite.addTest(WidgetTestCase('test_validar_fechas'))
    suite.addTest(WidgetTestCase('test_verificar_prefijo_archivos'))
    suite.addTest(WidgetTestCase('test_validar_cantidad_datos'))
    suite.addTest(WidgetTestCase('test_validar_existencia_de_los_registros_del_ct_en_zip'))
    suite.addTest(WidgetTestCase('test_error_validar_fechas'))
    suite.addTest(WidgetTestCase('test_error_validar_genericos'))
    suite.addTest(WidgetTestCase('test_error_crear_listas_para_validaciones'))
    suite.addTest(WidgetTestCase('test_error_verificar_archivos_minimos'))
    suite.addTest(WidgetTestCase('test_error_validar_cantidad_datos'))
    suite.addTest(WidgetTestCase('test_error_validar_existencia_de_los_registros_del_ct_en_zip'))
    suite.addTest(WidgetTestCase('test_error_verificar_prefijo_archivos'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

import unittest
from Aplicacion.Zip.zip import ArchivoZipServicio


class TestMetodosArchivos(unittest.TestCase):

    # Test: Campo de .zip cumpla requisitos
    @unittest.expectedFailure
    def test_nombre_zip(self):
        self.assertTrue(validar_nombre_archivo_zip(123435), 123435)  # Error por longitud de texto
        self.assertTrue(validar_nombre_archivo_zip('123456'), '123456')
        self.assertTrue(validar_nombre_archivo_zip('prueba'), 'prueba')  # Error por texto

    # Test: La extensión de los Archivo internos sea .txt
    @unittest.expectedFailure
    def test_extension_txt(self):
        self.assertTrue(validar_extension('rips/rips/172652/AP172652.TXT', '.txt'), True)
        self.assertTrue(validar_extension('rips/rips/172652/AP172652.txt', '.txt'), True)
        self.assertTrue(validar_extension('rips/rips/172652/AP172652.zip', '.zip'), True)

        # Test: El indicador/prefijo de cada archivo debe existir entre los permitidos

    @unittest.expectedFailure
    def test_indicador_archivo(self):
        self.assertTrue(validar_indicador_archivo('AC'), True)
        self.assertTrue(validar_indicador_archivo(12), False)  # Error parametro no existe en valores permitidos
        self.assertTrue(validar_indicador_archivo('ACE'), False)  # Error parametro no existe en valores permitidos

    def test_numero_remision(self):
        self.assertTrue(numero_remision())
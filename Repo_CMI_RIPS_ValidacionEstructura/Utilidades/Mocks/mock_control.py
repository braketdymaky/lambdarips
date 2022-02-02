from unittest.mock import Mock
from Dominio.Control.control import ModeloControl

mock = Mock()
mock.ct_list.return_value=[['050010210401', '27/09/2018', 'US172652', '4'], ['050010210401', '27/09/2018', 'AC172652', '10'],
        ['050010210401', '27/09/2018', 'AP172652', '40'], ['050010210401', '27/09/2018', 'AH172652', '1'],
        ['050010210401', '27/09/2018', 'AU172652', '2'], ['050010210401', '27/09/2018', 'AM172652', '28'],
        ['050010210401', '27/09/2018', 'AT172652', '85'], ['050010210401', '27/09/2018', 'AF172652', '4']]
mock.ct_fila_erronea=['050010210401xzxz', '27/09/201', 'Uy172615654646', '4']
mock.ct_fila_fecha_mayor_actual=['050010210401xzxz', '28/09/2019', 'US172615654646', '4']
mock.name_list = ['AC172652.TXT', 'AF172652.TXT', 'AH172652.TXT', 'AM172652.TXT', 'AP172652.TXT', 'AT172652.TXT',
                  'AU172652.TXT', 'CT172652.TXT', 'US172652.TXT']

mock.nombres_archivos = ['AC172652', 'AF172652', 'AH172652', 'AM172652', 'AP172652', 'AT172652','AU172652', 'CT172652', 'CT172653', 'US172652']
mock.CT_archivos_presentes = ['AC', 'AF', 'AH', 'AM', 'AP', 'AT','AU', 'CT', 'US']

mock.control_model= ModeloControl()
mock.control_model.CT_archivos_presentes=['AC', 'AF', 'AH', 'AM', 'AP', 'AT','AU', 'CT', 'US']
mock.control_model.nombres_archivos=['AC172652', 'AF172652', 'AH172652', 'AM172652', 'AP172652', 'AT172652','AU172652', 'CT172652', 'CT172653', 'US172652']
mock.control_model.name_list=['AC172652.TXT', 'AF172652.TXT', 'AH172652.TXT', 'AM172652.TXT', 'AP172652.TXT', 'AT172652.TXT','AU172652.TXT', 'CT172652.TXT', 'US172652.TXT']
mock.control_model.ct_fila_uno=['050010210401', '27/09/2018', 'US172652', '18']
mock.control_model.ct_lista=[['050010210401', '27/09/2018', 'US172652', '4'], ['050010210401', '27/09/2018', 'AC172652', '10'],
        ['050010210401', '27/09/2018', 'AP172652', '40'], ['050010210401', '27/09/2018', 'AH172652', '1'],
        ['050010210401', '27/09/2018', 'AU172652', '2'], ['050010210401', '27/09/2018', 'AM172652', '28'],
        ['050010210401', '27/09/2018', 'AT172652', '85'], ['050010210401', '27/09/2018', 'AF172652', '4']]
mock.control_model.codigo_habilitacion='050010210401'


mock.ct_diccionario = {"CT":[['050010210401', '27/09/2018', 'US172652', '4'], ['050010210401', '27/09/2018', 'AC172652', '10'],
        ['050010210401', '27/09/2018', 'AP172652', '40'], ['050010210401', '27/09/2018', 'AH172652', '1'],
        ['050010210401', '27/09/2018', 'AU172652', '2'], ['050010210401', '27/09/2018', 'AM172652', '28'],
        ['050010210401', '27/09/2018', 'AT172652', '85'], ['050010210401', '27/09/2018', 'AF172652', '4']]}
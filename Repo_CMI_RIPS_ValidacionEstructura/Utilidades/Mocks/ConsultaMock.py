from unittest.mock import Mock
from Dominio.Consulta.consulta import ModeloConsulta

mock = Mock()

mock.ac_lista = [
    ['4922194', '050010210401', 'CC', '71747668', '21/08/2018', '932-1', '890406', '10', '15', 'R688', '', '', '', '1',
     '16873.00', '0.00', '16873.00'],
    ['4922194', '050010210401', 'CC', '71747668', '15/08/2018', '932-1', '890602', '10', '15', 'B902', 'R688', '', '',
     '1', '38930.00', '0.00', '38930.00'],
    ['4922194', '050010210401', 'CC', '71747668', '14/08/2018', '932-1', '890454', '10', '15', 'B902', 'R688', '', '',
     '1', '35903.00', '0.00', '35903.00'],
    ['4922194', '050010210401', 'CC', '71747668', '27/08/2018', '932-1', '890454', '10', '15', 'B902', 'R688', '', '',
     '1', '35903.00', '0.00', '35903.00'],
    ['4922194', '050010210401', 'CC', '71747668', '16/08/2018', '932-1', '890602', '10', '15', 'B902', 'R688', '', '',
     '1', '38930.00', '0.00', '38930.00'],
    ['4922194', '050010210401', 'CC', '71747668', '31/08/2018', '932-1', '890454', '10', '15', 'B902', 'R688', '', '',
     '1', '35903.00', '0.00', '35903.00'],
    ['4922194', '050010210401', 'CC', '71747668', '14/08/2018', '932-1', '890602', '10', '15', 'B902', 'R688', '', '',
     '1', '38930.00', '0.00', '38930.00'],
    ['4922194', '050010210401', 'CC', '71747668', '01/09/2018', '932-1', '890306', '10', '15', 'B902', 'R688', '', '',
     '1', '7036.00', '0.00', '7036.00'],
    ['4922194', '050010210401', 'CC', '71747668', '01/09/2018', '932-1', '890306', '10', '15', 'B902', 'R688', '', '',
     '1', '7036.00', '0.00', '7036.00'],
    ['4929487', '050010210401', 'CC', '71620787', '19/09/2018', '1-563024000', '890701', '10', '15', 'R688', '', '', '',
     '1', '21484.00', '0.00', '21484.00']]

mock.ac_fila_uno = ['4922194', '050010210401', 'CC', '71747668', '21/05/2019', '932-1', '890406', '10', '15', 'R688', '', '', '2', '1',
     '16873.00', '0.1', '16873']

mock.ac_fila_errores = ['4922198', '050010210401', 'TT', '717476618', '01/45/2030', '', '', '10', '154', 'R6Z88','asd', 'dd', '',
    '3.0', '-16873.00', '0.00', 'a1687300']

mock.consulta_modelo = ModeloConsulta()

mock.ac_diccionario = {"AC":[
    ['4922194', '050010210401', 'CC', '71747668', '21/08/2018', '932-1', '890406', '10', '15', 'R688', '', '', '', '1',
     '16873.00', '0.00', '16873.00'],
    ['4922194', '050010210401', 'CC', '71747668', '15/08/2018', '932-1', '890602', '10', '15', 'B902', 'R688', '', '',
     '1', '38930.00', '0.00', '38930.00'],
    ['4922194', '050010210401', 'CC', '71747668', '14/08/2018', '932-1', '890454', '10', '15', 'B902', 'R688', '', '',
     '1', '35903.00', '0.00', '35903.00'],
    ['4922194', '050010210401', 'CC', '71747668', '27/08/2018', '932-1', '890454', '10', '15', 'B902', 'R688', '', '',
     '1', '35903.00', '0.00', '35903.00'],
    ['4922194', '050010210401', 'CC', '71747668', '16/08/2018', '932-1', '890602', '10', '15', 'B902', 'R688', '', '',
     '1', '38930.00', '0.00', '38930.00'],
    ['4922194', '050010210401', 'CC', '71747668', '31/08/2018', '932-1', '890454', '10', '15', 'B902', 'R688', '', '',
     '1', '35903.00', '0.00', '35903.00'],
    ['4922194', '050010210401', 'CC', '71747668', '14/08/2018', '932-1', '890602', '10', '15', 'B902', 'R688', '', '',
     '1', '38930.00', '0.00', '38930.00'],
    ['4922194', '050010210401', 'CC', '71747668', '01/09/2018', '932-1', '890306', '10', '15', 'B902', 'R688', '', '',
     '1', '7036.00', '0.00', '7036.00'],
    ['4922194', '050010210401', 'CC', '71747668', '01/09/2018', '932-1', '890306', '10', '15', 'B902', 'R688', '', '',
     '1', '7036.00', '0.00', '7036.00'],
    ['4929487', '050010210401', 'CC', '71620787', '19/09/2018', '1-563024000', '890701', '10', '15', 'R688', '', '', '',
     '1', '21484.00', '0.00', '21484.00']]}

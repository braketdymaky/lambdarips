from unittest.mock import Mock

mock = Mock()

mock.at_fila = ['4922194','050010210401','CC','71747668','932-1','1','534','CATETER IV #20','1','3438.00','3438.00']

mock.at_fila_errores = ['4922194aaaaaaaaaaaaaaaaaa','05001021040aaaaaaaaaaaaaaaaaaaaaaaaa1','CCaaaaaaaaaaaaaaaaaaa','71747668aaaaaaaaaaaaaa','932-1aaaaaaaaaaaaaaaaaa','1aaaaaaaaaaa','','','1aaaaaaaaaaaaa','343aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8.00','34aaaaaaaaaaaaaaaaaaa38.00']
mock.at_fila_incompleta = ['4922194','050010210401','CC','71747668','932-1','1','','CATETER IV #20','1']
mock.at_diccionario={"AT":[['4922194','050010210401','CC','71747668','932-1','1','534','CATETER IV #20','1','3438.00','3438.00']]}

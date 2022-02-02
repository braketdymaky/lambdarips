from unittest.mock import Mock

mock = Mock()

mock.am_fila = ['4922194','050010210401','CC','71747668','932-1','36241-2','1','ENOXAPARINA Sln Iny 40 mg','INYECTABLE','40 MG','JERINGA','18','34164.00','614952.00']

mock.am_fila_errores = ['4922194,hj,jk,kj,jk,jk,j','050010210401,kj,jk,jk,kj,jk,','CC,kjkhjhgjgjgjg','71747668jhgjghjghjghjgg','15/08lkliopiolloiloilioliolol','932-1jghjghjghjgh','','2dsadasdsa','2dasdasdasdsadadasdasdsadasds','','','dsadsadasdasdasdasdasdasd','dsdsadasdasdasdasdasdasdasda','1sdadasdasdasdasdsadasdsasd','22978.00']

mock.am_fila_incompleta = ['4922194','050010210401','869500','2','2','','R688','','','1','22978.00']

mock.am_diccionario = {"AM":[['4922194','050010210401','CC','71747668','932-1','36241-2','1','ENOXAPARINA Sln Iny 40 mg','INYECTABLE','40 MG','JERINGA','18','34164.00','614952.00']]}

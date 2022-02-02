from enum import Enum
from collections import namedtuple

TipoId = namedtuple('TipoId', ['longitud', 'nombre'])


class TipoIdEnum(Enum):
    CC = TipoId(10, 'CC')
    AS = TipoId(12, 'AS')
    CE = TipoId(10, 'CE')
    PA = TipoId(16, 'PA')
    CD = TipoId(16, 'CD')
    SC = TipoId(16, 'SC')
    RC = TipoId(11, 'RC')
    TI = TipoId(11, 'TI')
    CN = TipoId(9, 'CN')
    PE = TipoId(15, 'PE')
    MS = TipoId(10, 'MS')

    # Método para obtener el valor del ID asignado al enumerado
    @property
    def obtener_longitud(self):
        return self.value.longitud

    # Método para obtener el nombre asignado al enumerado
    @property
    def obtener_nombre(self):
        return self.value.nombre

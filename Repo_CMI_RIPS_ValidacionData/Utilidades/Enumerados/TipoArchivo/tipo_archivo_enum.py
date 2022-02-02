from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
TipoArchivos = namedtuple('TipoArchivos', ['id', 'nombre'])


class TipoArchivosEnum(Enum):
    AC = TipoArchivos(1, 'AC')  # Consulta
    AF = TipoArchivos(2, 'AF')  # Transacciones
    AH = TipoArchivos(3, 'AH')  # Hospitalizaciones
    AM = TipoArchivos(4, 'AM')  # Medicamentos
    AP = TipoArchivos(5, 'AP')  # Procedimientos
    AT = TipoArchivos(6, 'AT')  # Otros Servicios
    AU = TipoArchivos(7, 'AU')  # Urgencias
    CT = TipoArchivos(8, 'CT')  # Control
    US = TipoArchivos(9, 'US')  # Usuarios
    AD = TipoArchivos(10, 'AD')  # Descripcion agrupada
    AN = TipoArchivos(11, 'AN')  # Recien nacidos

    # Método para obtener el valor del ID asignado al enumerado
    @property
    def obtener_valor(self):
        return self.value.id

    # Método para obtener el nombre asignado al enumerado
    @property
    def obtener_nombre(self):
        return self.value.nombre

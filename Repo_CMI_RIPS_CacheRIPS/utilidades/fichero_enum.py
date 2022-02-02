from enum import Enum
from collections import namedtuple

# Se asigna el formato a utilizar para el enumerado
Fichero = namedtuple('Fichero', ['nombre'])


class FicheroEnum(Enum):
    TIPO_ARCHIVO = Fichero('tipo_archivo')
    ERRORES = Fichero('errores')
    TIPO_USUARIO = Fichero('tipo_usuario')
    TIPO_IDENTIFICACION_USUARIO = Fichero('tipo_identificacion_usuario')
    UNIDAD_MEDIDA_EDAD = Fichero('unidad_medidad_edad')
    ZONA_RESIDENCIAL = Fichero('zona_residencial')
    SEXO = Fichero('sexo')
    TIPO_IDENTIFICACION_PRESTADOR = Fichero('tipo_identificacion_prestador')
    CODIGO_CONCEPTO = Fichero('codigo_concepto')
    FINALIDAD_CONSULTA = Fichero('finalidad_consulta')
    DIAGNOSTICO_PRINCIPAL = Fichero('diagnostico_principal')
    CONTROL_PRENATAL = Fichero('control_prenatal')
    CAUSA_EXTERNA = Fichero('causa_externa')
    TIPO_MEDICAMENTO = Fichero('tipo_medicamento')
    TIPO_SERVICIO = Fichero('tipo_servicio')
    CIE10 = Fichero('cie10')
    FORMA_REALIZACION_ACTO_QUIRURJICO = Fichero('forma_quirurjico')
    PERSONAL_ATIENDE = Fichero('personal_atiende')
    AMBITO_PROCEDIMIENTO = Fichero('ambito_procedimiento')
    FINALIDAD_PROCEDIMIENTO = Fichero('finalidad_procedimiento')
    CUPS = Fichero('cups')
    VIA_INGRESO = Fichero('via_ingreso')
    ESTADO_SALIDA = Fichero('estado_salida')
    DESTINO_USUARIO = Fichero('destino_usuario')
    EAPB = Fichero('eapb')
    DEPARTAMENTO = Fichero('departamento')
    MUNICIPIO = Fichero('municipio')
    VACUNAS_CUPS = Fichero('vacunas_cups')

    # Método para obtener el nombre asignado al enumerado
    @property
    def obtener_nombre(self):
        return self.value.nombre

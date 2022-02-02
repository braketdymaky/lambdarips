import io
import zipfile
import pickle
import boto3
from Utilidades.Enumerados.Ficheros.fichero_enum import FicheroEnum as FE
from Dominio.Fichero.fichero import ModeloFichero


class Datos:
    def obtener_listas_parametrizadas(self):
        """
        Metodo para asignar mediante conexi?n al bucket de S3 las listas necesarias para validaciones
        :return:
        """
        bucket = 'cmirips-dev-02'
        key = 'Ficheros/ficheros.zip'
        model = ModeloFichero.obtener_instancia()
        zipp = self.obtener_zip(bucket, key)
        if zipp is not None:
            with io.BytesIO(zipp.read()) as tf:
                tf.seek(0)
                with zipfile.ZipFile(tf, mode='r') as zipf:
                    for finfo in zipf.infolist():
                        ifile = zipf.open(finfo)
                        lista_tupla = pickle.load(ifile)
                        if ifile.name == FE.TIPO_ARCHIVO.obtener_descripcion:
                            model.asignar_tipo_archivo(lista_tupla)
                        if ifile.name == FE.ERRORES.obtener_descripcion:
                            model.asignar_errores(lista_tupla)
                        if ifile.name == FE.TIPO_USUARIO.obtener_descripcion:
                            model.asignar_tipo_usuario(lista_tupla)
                        if ifile.name == FE.TIPO_IDENTIFICACION_USUARIO.obtener_descripcion:
                            model.asignar_tipo_id_usuario(lista_tupla)
                        if ifile.name == FE.UNIDAD_MEDIDA_EDAD.obtener_descripcion:
                            model.asignar_unidad_medida(lista_tupla)
                        if ifile.name == FE.ZONA_RESIDENCIAL.obtener_descripcion:
                            model.asignar_zona_residencial(lista_tupla)
                        if ifile.name == FE.SEXO.obtener_descripcion:
                            model.asignar_sexo(lista_tupla)
                        if ifile.name == FE.TIPO_IDENTIFICACION_PRESTADOR.obtener_descripcion:
                            model.asignar_tipo_id_prestador(lista_tupla)
                        if ifile.name == FE.CODIGO_CONCEPTO.obtener_descripcion:
                            model.asignar_codigo_concepto(lista_tupla)
                        if ifile.name == FE.FINALIDAD_CONSULTA.obtener_descripcion:
                            model.asignar_finalidad_consulta(lista_tupla)
                        if ifile.name == FE.DIAGNOSTICO_PRINCIPAL.obtener_descripcion:
                            model.asignar_diagnostico_principal(lista_tupla)
                        if ifile.name == FE.CONTROL_PRENATAL.obtener_descripcion:
                            model.asignar_control_prenatal(lista_tupla)
                        if ifile.name == FE.CAUSA_EXTERNA.obtener_descripcion:
                            model.asignar_causa_externa(lista_tupla)
                        if ifile.name == FE.TIPO_MEDICAMENTO.obtener_descripcion:
                            model.asignar_tipo_medicamento(lista_tupla)
                        if ifile.name == FE.TIPO_SERVICIO.obtener_descripcion:
                            model.asignar_tipo_servicio(lista_tupla)
                        if ifile.name == FE.CIE10.obtener_descripcion:
                            model.asignar_cie10(lista_tupla)
                        if ifile.name == FE.FORMA_REALIZACION_ACTO_QUIRURJICO.obtener_descripcion:
                            model.asignar_forma_acto_quirurjico(lista_tupla)
                        if ifile.name == FE.PERSONAL_ATIENDE.obtener_descripcion:
                            model.asignar_personal_atiende(lista_tupla)
                        if ifile.name == FE.AMBITO_PROCEDIMIENTO.obtener_descripcion:
                            model.asignar_ambito_procedimiento(lista_tupla)
                        if ifile.name == FE.FINALIDAD_PROCEDIMIENTO.obtener_descripcion:
                            model.asignar_finalidad_procedimiento(lista_tupla)
                        if ifile.name == FE.CUPS.obtener_descripcion:
                            model.asignar_cups(lista_tupla)
                        if ifile.name == FE.CUPS_VACUNAS.obtener_descripcion:
                            model.asignar_cups_vacunas(lista_tupla)
                        if ifile.name == FE.VIA_INGRESO.obtener_descripcion:
                            model.asignar_via_ingreso(lista_tupla)
                        if ifile.name == FE.ESTADO_SALIDA.obtener_descripcion:
                            model.asignar_estado_salida(lista_tupla)
                        if ifile.name == FE.DESTINO_USUARIO.obtener_descripcion:
                            model.asignar_destino_usuario(lista_tupla)
                        if ifile.name == FE.DEPARTAMENTO.obtener_descripcion:
                            model.asignar_departmamento(lista_tupla)
                        if ifile.name == FE.MUNICIPIO.obtener_descripcion:
                            model.asignar_municipio(lista_tupla)
                        if ifile.name == FE.EAPB.obtener_descripcion:
                            model.asignar_eapb(lista_tupla)                        
                            

    def obtener_zip(self, bucket, key):
        """
        Obtener zip, mediante conexi?n a bucket de s3
        :param bucket:
        :param key:
        :return:
        """
        s3 = boto3.client('s3')
        try:
            archivo = s3.get_object(Bucket=bucket, Key=key)
        except Exception as e:
            return None
        return archivo['Body']

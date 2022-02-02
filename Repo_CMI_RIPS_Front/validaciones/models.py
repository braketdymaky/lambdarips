from django.db import models


class TripsValidaciones(models.Model):
    cdcodigo = models.IntegerField(db_column='CDCODIGO', primary_key=True)  # Field name made lowercase.
    dsdescripcion = models.CharField(db_column='DSDESCRIPCION', max_length=250)  # Field name made lowercase.
    dstipo = models.CharField(db_column='DSTIPO', max_length=10)  # Field name made lowercase.
    dsarchivo = models.CharField(db_column='DSARCHIVO', max_length=3)  # Field name made lowercase.
    sndinamico = models.IntegerField(db_column='SNDINAMICO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIPS_VALIDACIONES'


class TripsClientesEapb(models.Model):
    cdid = models.AutoField(db_column='CDID', primary_key=True)  # Field name made lowercase.
    dstipo_administradora = models.CharField(db_column='DSTIPO_ADMINISTRADORA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dscodigo_entidad = models.CharField(db_column='DSCODIGO_ENTIDAD', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dsnit = models.CharField(db_column='DSNIT', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dsadministradora = models.CharField(db_column='DSADMINISTRADORA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dsnombre_aporte_linea = models.CharField(db_column='DSNOMBRE_APORTE_LINEA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    snactivo = models.IntegerField(db_column='SNACTIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIPS_CLIENTES_EAPB'



class TripsDinamismo(models.Model):
    cdid = models.AutoField(db_column='CDID', primary_key=True)  # Field name made lowercase.
    cdidcliente = models.ForeignKey(TripsClientesEapb, models.DO_NOTHING, db_column='CDIDCLIENTE')  # Field name made lowercase.
    nmcod_metodo = models.CharField(db_column='NMCOD_METODO',  max_length=900, blank=True, null=True)  # Field name made lowercase.
    snactive = models.IntegerField(db_column='SNACTIVE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIPS_DINAMISMO'


class TripsRegistrosValidados(models.Model):
    cdid = models.AutoField(db_column='CDID', primary_key=True)  # Field name made lowercase.
    dsnumero_remision = models.CharField(db_column='DSNUMERO_REMISION', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fefecha_registro = models.DateTimeField(db_column='FEFECHA_REGISTRO', blank=True, null=True)  # Field name made lowercase.
    cdclientes = models.ForeignKey(TripsClientesEapb, models.DO_NOTHING, db_column='CDCLIENTES_ID')  # Field name made lowercase.
    nmcodigo_prestador = models.CharField(db_column='NMCODIGO_PRESTADOR', max_length=12)  # Field name made lowercase.
    cdid_dinamismo = models.ForeignKey(TripsDinamismo, models.DO_NOTHING, db_column='CDID_DINAMISMO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRIPS_REGISTROS_VALIDADOS'

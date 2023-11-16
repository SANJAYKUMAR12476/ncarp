from django.db import models


class DataSource(models.Model):
    id = models.AutoField(primary_key=True)
    sourcetype = models.CharField(max_length=255)
    processingtype = models.CharField(max_length=255)
    parameterid = models.IntegerField()
    parametername = models.CharField(max_length=255)
    parametertable = models.CharField(max_length=255)
    sharedmemoryid = models.IntegerField()
    isactive = models.BooleanField()

    class Meta:
        db_table = 'hierarchy\".\"datasource'
        managed = False
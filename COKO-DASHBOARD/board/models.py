# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Corona(models.Model):
    deathcnt = models.IntegerField(db_column='deathCnt', blank=True, null=True)  # Field name made lowercase.
    defcnt = models.TextField(db_column='defCnt', blank=True, null=True)  # Field name made lowercase.
    gubun = models.TextField(blank=True, null=True)
    gubuncn = models.TextField(db_column='gubunCn', blank=True, null=True)  # Field name made lowercase.
    gubunen = models.TextField(db_column='gubunEn', blank=True, null=True)  # Field name made lowercase.
    incdec = models.TextField(db_column='incDec', blank=True, null=True)  # Field name made lowercase.
    isolclearcnt = models.IntegerField(db_column='isolClearCnt', blank=True, null=True)  # Field name made lowercase.
    isolingcnt = models.TextField(db_column='isolIngCnt', blank=True, null=True)  # Field name made lowercase.
    localocccnt = models.IntegerField(db_column='localOccCnt', blank=True, null=True)  # Field name made lowercase.
    overflowcnt = models.IntegerField(db_column='overFlowCnt', blank=True, null=True)  # Field name made lowercase.
    qurrate = models.TextField(db_column='qurRate', blank=True, null=True)  # Field name made lowercase.
    stdday = models.DateTimeField(db_column='stdDay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corona'


class CoronaCon(models.Model):
    jcg_dt = models.DateTimeField(db_column='JCG_DT', blank=True, null=True)  # Field name made lowercase.
    variable = models.TextField(blank=True, null=True)
    con = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corona_con'


class News(models.Model):
    title = models.TextField(blank=True, null=True)
    originallink = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pubdate = models.DateTimeField(db_column='pubDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news'

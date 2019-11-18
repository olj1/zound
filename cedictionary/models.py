# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Entries(models.Model):
    id = models.IntegerField(primary_key=True, serialize=True)
    traditional = models.TextField(blank=True, null=True)
    simplified = models.TextField(blank=True, null=True)
    pinyin = models.TextField(blank=True, null=True)
    english = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entries'

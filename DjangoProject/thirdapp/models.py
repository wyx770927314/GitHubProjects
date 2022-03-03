from django.db import models


# Create your models here.
class PersonInfo(models.Model):
    class Meta:
        db_table = 'person'

    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=20, db_column='name')
    age = models.IntegerField(db_column='age')
    hobby = models.CharField(max_length=20,db_column='hobby')

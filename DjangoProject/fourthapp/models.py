from django.db import models


# Create your models here.
class Car(models.Model):
    class Meta:
        db_table = 'car'

    id = models.AutoField(primary_key=True, db_column='id')
    age = models.IntegerField(db_column='age')
    name = models.CharField(max_length=20, db_column='name')
    date = models.DateField(db_column='date')
    color = models.CharField(max_length=20,db_column='color')
    type = models.CharField(max_length=20, db_column='type')
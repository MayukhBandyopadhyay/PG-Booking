from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    pwd=models.CharField(max_length=50)
    class Meta:
        db_table="user"
class booker(models.Model):
    name=models.CharField(max_length=100)
    phno=models.IntegerField()
    email=models.EmailField()
    pwd=models.CharField(max_length=50)
    adh=models.IntegerField()
    addr=models.CharField(max_length=100)
    class Meta:
        db_table="booker"

class room(models.Model):
    name=models.CharField(max_length=100,blank=True)
    no=models.IntegerField()
    capacity=models.IntegerField()
    startdate=models.DateField(null=True)
    enddate=models.DateField(null=True)
    def duration(u):
        return(u.enddate-u.startdate).days
    class Meta:
        db_table="room"


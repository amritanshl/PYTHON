from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=200)
    img= models.ImageField(upload_to='imgs')
    desc =  models.TextField()
    price= models.FloatField()
    offer= models.BooleanField(default=False)

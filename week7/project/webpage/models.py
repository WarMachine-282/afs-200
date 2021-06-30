from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    imgURL = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()


class Ideas(models.Model):
    name = models.CharField(max_length=100)
    # imgURL = models.ImageField(upload_to='pics')
    desc = models.TextField()
    # price = models.IntegerField()
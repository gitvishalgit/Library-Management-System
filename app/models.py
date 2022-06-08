from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField(unique=True)
    category = models.CharField(max_length=100)
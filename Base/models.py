from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=100)
    Number=models.IntegerField()
    content=models.TextField(max_length=400) 


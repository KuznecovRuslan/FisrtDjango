from django.db import models

# Create your models here.
class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   color = models.CharField(max_length=30, null=True, default="black")
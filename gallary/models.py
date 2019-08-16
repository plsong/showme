from django.db import models

# Create your models here.


class Gallary(models.Model):
    description=models.CharField(max_length=100)
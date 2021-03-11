from django.db import models

# Create your models here.
class phonenum(models.Model):
    number = models.CharField(max_length=10)

class inputstring(models.Model):
    source = models.TextField()


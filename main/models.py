from django.db import models

# Create your models here.
class AddNew(models.Model):
    code = models.CharField(max_length=999999999999)
    url = models.CharField(max_length=100)

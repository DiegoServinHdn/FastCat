from django.db import models

# Create your models here.

class Workspace(models.Model):
    code = models.CharField(max_length=5, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
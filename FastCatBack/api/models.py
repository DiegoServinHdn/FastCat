from django.db import models
from django.db.models import deletion
import string 
import random

def generate_unique_code(lenght=5):
    while True:
        code =  ''.join(random.choices(string.ascii_uppercase + string.digits, k=lenght))
        if Workspace.objects.filter(code=code).count() == 0:
            return code

# Create your models here.

class Workspace(models.Model):
    code = models.CharField(max_length=5, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_edit = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
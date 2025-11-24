from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class Role(models.Model):

    name = models.CharField(max_length=20)
    Description = models.TextField()

    def __str__(self):
       return f"{self.name}"

class customUser(AbstractUser):
    
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING , blank=True , null = True)

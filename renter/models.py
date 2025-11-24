from django.db import models
from user_mgmt.models import customUser
from books.models import books

# Create your models here.

class rental(models.Model):
    
    user = models.ForeignKey(customUser , on_delete=models.DO_NOTHING)
    book = models.ForeignKey(books , on_delete=models.CASCADE)
    rent_date = models.DateField(auto_now=True)
    return_date =  models.DateField(null=True ,blank= True)
    fine_to_pay = models.FloatField(default=0)
    count = models.IntegerField(default=1)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
       return f"{self.book}"

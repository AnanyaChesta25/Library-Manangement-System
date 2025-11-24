from django.db import models



# Create your models here.
class book_category(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
       return f"{self.name}"

class books(models.Model):

    title = models.CharField(max_length=50)
    img_url = models.TextField(max_length=150 , default='book_url')
    author = models.CharField(max_length=30)
    year = models.IntegerField()
    count = models.IntegerField(default=1)
    cost =  models.FloatField()
    category = models.ForeignKey(book_category , on_delete=models.DO_NOTHING ,blank=True , null = True)

    def __str__(self):
       return f"{self.title}"
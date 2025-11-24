from django.contrib import admin

# Register your models here.
from .models import books,book_category

admin.site.register(books)
admin.site.register(book_category)
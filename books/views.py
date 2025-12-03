from django.shortcuts import render,redirect
from .models import books,book_category
# Create your views here.

def homepage(request):

    book = books.objects.all()
    return render(request , 'homepage.html', context={"books":book})

def search(request):
    
    data = request.GET
    print(data)
    search = data.get('search','')
     
    if search =='':
      book = books.objects.none()

    elif search == book_category.objects.filter(name = search):
      se = book_category.objects.filter(name = search)
      book = books.objects.filter(category = se)

    else:
       book = books.objects.filter(title__contains = search) 
       
    return render(request,'search.html',context={"books":book})

def home(request):
    
    book = books.objects.all()
    return render(request , 'home.html', context={"books":book})

def admin_home(request):
    
    if request.user.is_superuser :
      book = books.objects.all()
      return render(request , 'Admin/admin_home.html', context={"books":book})
    
    else: 
     return redirect("home")
    

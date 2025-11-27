from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import rental
from books.models import books
from .models import rental
from datetime import timedelta
from django.http import HttpResponse

# Create your views here.

def add_rental(request , book_id ):

    #  if request.user.is_authenticated:
    #   query = books.objects.filter(id=book_id)
      
    #   user = request.user
    #   books = query[0]
    #   query.count -= 1
    #   query.save()

    #   existing_cart_items , created_status = rental.objects.get_or_create(
    #      user = user,
    #      book = books,
    #      return_date = rental.rent_date + timedelta(days=15)
    #      )
      
    #   if not created_status:
    #        return render(request,'rental/open_rental.html',context={"error_message":"You can rent one book at a time."})
    #   else:
    #     rentals = rental.objects.all()
    #     return render(request,'rental/renter_ui.html',context={"rental":rentals})  
    if request.user.is_authenticated:
        query = books.objects.filter(id=book_id)

        if not query.exists():
            return HttpResponse("<h1>Book not found.</h1>")

        book = query.first()

        # Decrement book count and save
        book.count -= 1
        book.save()

        # Create or get rental
        rental_obj, created_status = rental.objects.get_or_create(
            user=request.user,
            book=book,
            # defaults={"return_date": book.rent_date + timedelta(days=15)}
            # return_date = rental.rent_date + timedelta(days=15)

        )

        if not created_status:
            selected_books = books.objects.filter(id= book_id)
            book = selected_books[0]
            return render(request, 'rental/open_rental.html', context={
                "error_message": "You can rent one book at a time.",
                "book":book
            })
        else:
            rental_obj.return_date = rental_obj.rent_date + timedelta(days=15)
            rental_obj.save()
            print(rental_obj.return_date)
            rentals = rental.objects.all()
            return render(request, 'rental/open_rental.html', context={"success_message": "Your book has be issued , go and check in MyBooks page",
                "book":book})
    
    return HttpResponse("<h1>You are not authenticated</h1>")

      

def open_rental(request , book_id):
   
    selected_books = books.objects.filter(id= book_id)
    book = selected_books[0]

    return render(request,'rental/open_rental.html',context={'book':book})

def show_rental(request):
    
  if request.method == 'GET':
    selected_books = rental.objects.all()
    return render(request,'rental/renter_ui.html',context={'renter':selected_books})
 
  elif request.method == 'POST':

        renter_id = request.POST.get("renter_id")
        renter = rental.objects.get(id=renter_id)
        renter.is_returned = True
        renter.return_date = timezone.now().date()
        renter.save()
        return redirect('show_rental')
  
  return ("<h1>Something went Wrong</h1>")


# def renter_list(request):
#     if request.method == 'GET':
#         return render(request,'rental/renter_ui.html')  
    
#     elif request.method == 'POST':

#         renter_id = request.POST.get("renter_id")
#         renter = rental.objects.get(id=renter_id)
#         renter.is_returned = True
#         renter.return_date = timezone.now().date()
#         renter.save()
#         return redirect('rental/renter_ui.html')

#     renters = rental.objects.all()
#     return render(request, 'rental/renter_ui.html', {'renter': renters})

from django.shortcuts import render,redirect
from .models import Role,customUser
from django.contrib.auth import authenticate, login

# Create your views here.
def role(request):
    
    roles = Role.objects.all()
   

    if request.method == 'GET':
     return render(request,'register.html', context={"role":roles})

def register(request):
     
     if request.method == 'GET':
      return render(request,'user/register.html')
     
     elif request.method == 'POST':

        data = request.POST

        username = data['username'] 
        first_name = data['firstname'] 
        last_name = data['lastname']
        password = data['password'] 
        role = data.get('role')

        role_instance= Role.objects.get(name = role)

        user = customUser.objects.create(username = username , first_name = first_name, last_name = last_name , role =role_instance )
        user.set_password(password)
        user.save()

        return redirect("login")
     

def login_page(request):

  # if request.method == 'GET':   
  #   return render(request,'user/login.html')
  
  # if request.method == 'POST':
     
  #     data = request.POST

  #     username = data.get('username' ,'')
  #     password = data.get('password','')

  #     valid = authenticate(request, username = username , password = password)
  #     print(valid,"-------->>>>")

  #     if valid is None:
  #        print("Invalid Crenditals")
  #        return render(request, 'user/login.html', context={"error_message":"Invalid Crenditals.You need to register first."})

  #     else:
         
  #        login(request, valid)
  #        return redirect("home")

 
    if request.method == 'GET':
        return render(request, 'user/login.html')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        print(user, "-------->>>>")

        if user is None:
            # Invalid credentials
            print("Invalid Credentials")
            return render(request, 'user/login.html', {
                "error_message": "Invalid Credentials. You need to register first."
            })

        # Login successful
        login(request, user)

        # Redirect based on user type
        if user.is_superuser:
            # Superuser → admin dashboard
            return redirect("admin_home")  # replace with your admin URL name
        else:
            # Normal user → regular home page
            return redirect("home")
      
def myprofile_page(request):
   
    if not request.user.is_authenticated:
        return redirect('login') 
  
    return render(request, 'user/myprofile.html', {"user":request.user})      

from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import cust_account
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def store(request):
    return render(request,'store.html')


def signup(request):
    return render(request,'signup.html')

def create_acc(request):
    address=request.POST['address']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    phone_number=request.POST['phone_number']
    password=request.POST['password']
    fn=str(first_name)+str(last_name)
    user=User.objects.create_user(username=fn.lower(),first_name=first_name,last_name=last_name,password=password)
    User.save(user)
    acc=cust_account(address=address,first_name=first_name,last_name=last_name,phone_number=phone_number,total_Order_number=0)
    acc.save(acc)
    return redirect('/login')

def profile_land(request):
    profile=cust_account.objects.all()

    return render(request,'Profile_Landing.html',{'pros':profile})

def admin(request):
    acs = cust_account.objects.all()
    return render(request,'admin.html',{'accs':acs})

def login(request):
    return render(request,'login.html')

def login_acc(request):
    username=request.POST['username']
    password = request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        print("Correct user")
        return redirect('/')
    else:
        print("Invalid Username or Password")
        return redirect('/')

def forgot_pass(request):
    return render(request,'forgot_pass.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def buycp1(request):
    return render(request,'product_page.html')
def buycp2(request):
    return render(request,'product_page.html')
def buycp3(request):
    return render(request,'product_page.html')
def buysp1(request):
    return render(request,'product_page.html')
def buysp2(request):
    return render(request,'product_page.html')
def buysp3(request):
    return render(request,'product_page.html')
def buysp4(request):
    return render(request,'product_page.html')
def buybp1(request):
    return render(request,'product_page.html')
def buybp2(request):
    return render(request,'product_page.html')
def buybp3(request):
    return render(request,'product_page.html')
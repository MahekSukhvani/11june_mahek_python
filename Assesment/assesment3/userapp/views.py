from django.shortcuts import render,redirect
from .form import *

# Create your views here.

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        data=userdata(request.POST)
        if data.is_valid():
            data.save()
            print("data Saved Succesfully!")
            return redirect('login.html')
        else:
            print("Data Savaing unsuccesfull!")

    return render(request,'signup.html')


def login(request):

    if request.method=='POST':
        eml=request.POST['email']
        pas=request.POST['pas']

        data=signup_data.objects.filter(email=eml,pas=pas)

        if data.exists():
            print('Login SUccess')
            request.session["user"]=eml
            return redirect('dashboard')

        else:
            print('Can not able to login')


    return render(request,'login.html')




def dashboard(request):
    return render(request,'dashboard.html')
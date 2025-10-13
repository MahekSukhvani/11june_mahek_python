from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
import random
from django.core.mail import send_mail
from laboratory import settings

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def about(request):
    return render(request,'about.html')

def booktest(request):
    return render(request,'booktest.html')

def reports(request):
    return render(request,'reports.html')

def contact(request):
    return render(request,'contact.html')

def login(request):

    if request.method=='POST':
        eml=request.POST['email']
        pas=request.POST['password']

        data=userrdata.objects.filter(email=eml,password=pas)

        if data.exists():
            print('Login SUccess')
            request.session["user"]=eml
            return redirect('/')
        else:
            print('Can not able to login')


    return render(request,'login.html')

def signup(request):

    if request.method=='POST':
        user=userform(request.POST)
        if user.is_valid():
            # Store form data in session
            request.session['form_data'] = request.POST  

            #otp verify

            otp=random.randint(1111,9999)
            request.session['otp'] = otp 

            sub="Your One Time Pasword"
            msg=f"Dear User!\n\nThanks for register our service!\nFor account verification, Your one time password is {otp}.\n\nThanks & Regards\nMediScan Team\n+91 9664872519 | mediscanportal@gmail.com"
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST["email"]]

            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
            print("Mail Send Succesfully")
            return redirect('otp')
    

        else:
            print(user.errors)


    return render(request,'signup.html')


def userlogout(request):
    logout(request)
    return redirect('login')

def otp(request):
    if request.method == 'POST':
        # Get each digit from 4 input boxes
        digit1 = request.POST.get('otp1', '')
        digit2 = request.POST.get('otp2', '')
        digit3 = request.POST.get('otp3', '')
        digit4 = request.POST.get('otp4', '')

        entered_otp = f"{digit1}{digit2}{digit3}{digit4}"
        otp = request.session.get('otp')                 
        form_data = request.session.get('form_data')     

        if otp and str(otp) == str(entered_otp):               
            form = userform(form_data)                
            if form.is_valid():                          
                form.save()                              
                print("Signup Successfully & Data Saved!")
                request.session.pop('otp', None)
                request.session.pop('form_data', None)

                return redirect("login")   
            else:
                print(form.errors)             
        else:
            print("Error! OTP Verification failed... Try again!")
    
    return render(request,'otp.html')


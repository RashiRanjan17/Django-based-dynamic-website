from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages
from .forms import CustomerRegistrationForm, LoginForm, LoginForms
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.views.generic import View
from django.contrib.auth import authenticate , login , logout

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratutalions!! Registered Sucessfully')
            form.save()   
        return redirect('login')  

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)           

class LoginView(View):
    def get(self,request):
        form = LoginForms()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        form = LoginForms(request.POST)
        if form.is_valid():
            messages.success(request,'Congratutalions!! Registered Sucessfully')
            form.save()   
        return render(request,'login.html',{'form':form})  




def index(request):
    context={
        'variable': 'This is sent' 
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is my homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about")    

def service(request):
    return render(request,'service.html')
    #return HttpResponse("this is service")   

def profile(request):
    return render(request,'profile.html')

def contact(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')

    




        

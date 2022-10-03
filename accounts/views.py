
from django.shortcuts import render,redirect
from .forms import SighUpForm
from .models import Profile
from django.contrib.auth import authenticate,login

def sighup(request):
    if request.method =="POST":
        form =  SighUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect("/accounts/profile")
            
    else:
        form = SighUpForm()
    
    return render(request,"registration/sighup.html",{"form":form})
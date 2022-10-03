
from django.shortcuts import render,redirect
from .forms import SighUpForm,EditProfileInfo,EditUserInfo
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

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,"profile/profile.html",{"profile":profile})

def profile_edit(request):
    p = Profile.objects.get(user= request.user)
    if request.method == "POST":
        UserForm = EditUserInfo(request.POST,instance=request.user)
        ProfileForm = EditProfileInfo(request.POST,instance=p)
        if UserForm.is_valid() and ProfileForm.is_valid():
            UserForm.save()
            ProfileForm.save(commit=False)
            ProfileForm.user = request.user
            ProfileForm.save()
            return redirect("/accounts/profile")
    else:# show form
        UserForm = EditUserInfo(instance=request.user)
        ProfileForm = EditProfileInfo(instance=p)
    
    return render(request,"profile/profile_edit.html",
    {'userform':UserForm,'profileform':ProfileForm})

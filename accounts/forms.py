from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


#form to sigh up page
class SighUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ["username","email","password1","password2"]

#forms to edit profile page

class EditUserInfo(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email",'first_name','last_name']

class EditProfileInfo(forms.ModelForm):
    class Meta:
        model =Profile
        fields = ["phone",'address']

from django import forms
from django.contrib.auth.models import User
from coreapp.models import Restaurant

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name","last_name","id")
    
class RestaurantForm(forms.ModelForm):
    class Meta:
        model  = Restaurant
        fields = {"name", "address", "logo"}
from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserCreationForm
from .models import Books,Review,Profile




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

User._meta.get_field('email')._unique = True 


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
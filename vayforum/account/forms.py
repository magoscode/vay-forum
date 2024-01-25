from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, CustomUserCreationForm 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")


# unique email
        
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

#email validation
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if CustomUser.objects.filter(email = email).exists():

            raise forms.ValidationError('Email nis dats')
        
        if len(email >= 350):
            raise forms.ValidationError("Email deech du")


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")



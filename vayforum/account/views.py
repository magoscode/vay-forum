from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomUserLoginForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password = form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect("home")

    else:
        form = CustomUserLoginForm()
    return render(request, "account/login.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        
    else:
        form = CustomUserCreationForm()

    return render(request, "account/register.html", {"form": form})



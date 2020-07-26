from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomRegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created, Login To Get Started!!"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request,"register.html",{'register_form': register_form})

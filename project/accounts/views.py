from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import Login_Form


# Create your views here.
def doctors_list(request):
    doctors=User.objects.all()
    return render(request,'user/doctors_list.html',{'accounts':doctors})

def home(request):
    doctors=User.objects.all()
    return render(request,'robot/home.html',{'robots':doctors})

def user_login(request):
    form=Login_Form()
    return render(request,'user/login.html',{
        'form':form

    })
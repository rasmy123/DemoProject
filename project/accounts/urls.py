from django.urls import path

from .import views

app_name='accounts'
urlpatterns = [
    path('accounts/',views.doctors_list,name='doctors_list'),
    path('login/',views.user_login,name='login'),
    path('home/',views.home,name='home'),
   
]


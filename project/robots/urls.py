from django.urls import path

from .import views
from .models import Schedule

app_name='robots'
urlpatterns = [ 

   
  # TEMPORARY
    path('', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),
    path('calendar', views.calendar, name='calendar'),

    path('home',views.Robot_Listing,name='home'),
    path('<int:id>/',views.Robot_Details,name='robot_details'),
    path('robot_list/',views.Robot_List,name='robot_list'),
    path('location_list/',views.Location_List,name='location_list'),
    path('category_list/',views.Category_List,name='category_list'),
    path('Schedule_Details/',views.Schedule_Details,name='schedule_details'),
    path('schedule_Submit/',views.schedule_Submit,name='schedule_Submit'),
    path('Robot_Search/',views.Robot_Search,name='Robot_Search'),
    path('schedule_list/',views.Schedule_List,name='schedule_list'),
    path('schedule_edit/<Process_ID>/',views.Schedule_edit,name='schedule_edit'),
    path('schedule_update/',views.Schedule_Update,name='schedule_update'),
    path('schedule_delete/<Process_ID>/',views.Schedule_Delete,name='schedule_delete'),
    path('robot_listing_search/',views.Robot_Listing_Search,name='robot_listing_search'),
    path('history_list/',views.History_List,name='history_list'),
    path('history_listing_search/',views.History_Listing_Search,name='history_listing_search'),
    path('history_details/<Process_ID>/',views.History_Details,name='history_details'),
]
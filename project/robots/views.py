from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from robots.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token
from robots.graph_helper import get_user, get_calendar_events
import dateutil.parser



from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from robots.models import Robot
from robots.models import Category
from robots.models import Location
from django.db import connection
from .models import Schedule
from .models import History

def home(request):
      context = initialize_context(request)
      return render(request, 'robot/home.html', context)
# </HomeViewSnippet>

# <InitializeContextSnippet>
def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)

  if error != None:
    context['errors'] = []
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', {'is_authenticated': False})
  return context
# </InitializeContextSnippet>

# <SignInViewSnippet>
def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  print(sign_in_url)
  return HttpResponseRedirect(sign_in_url)
# </SignInViewSnippet>

# <SignOutViewSnippet>
def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('robots:signin'))
# </SignOutViewSnippet>

# <CallbackViewSnippet>
def callback(request):
  # Get the state saved in session
  print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
  expected_state = request.session.pop('auth_state', '')
  print(expected_state)
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)
  
  # Get the user's profile
  user = get_user(token)
  print(user)
  # Save token and user
  store_token(request, token)
  store_user(request, user)

  return HttpResponseRedirect(reverse('robots:home'))
# </CallbackViewSnippet>

# <CalendarViewSnippet>
def calendar(request):
  context = initialize_context(request)

  token = get_token(request)

  events = get_calendar_events(token)

  if events:
    # Convert the ISO 8601 date times to a datetime object
    # This allows the Django template to format the value nicely
    for event in events['value']:
      event['start']['dateTime'] = dateutil.parser.parse(event['start']['dateTime'])
      event['end']['dateTime'] = dateutil.parser.parse(event['end']['dateTime'])

    context['events'] = events['value']

  return render(request, 'robots/calendar.html', context)
# </CalendarViewSnippet>





# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def Robot_Listing(request):
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM robots_robot" )
      Robot_list = dictfetchall(cursor)

      cursor.execute("SELECT * FROM robots_Category")
      Category_list = dictfetchall(cursor)

      cursor.execute("SELECT * FROM robots_Location")
      Location_list = dictfetchall(cursor)
      context = initialize_context(request)
    return render(request,'robot/home.html',{'context':context,'Robot_list':Robot_list,'Category_list':Category_list,'Location_list':Location_list})

def Robot_List(request):
    with connection.cursor() as cursor:
      cursor.execute("SELECT * FROM robots_robot" )
      Robot_list = dictfetchall(cursor)

      cursor.execute("SELECT * FROM robots_Category")
      Category_list = dictfetchall(cursor)

      cursor.execute("SELECT * FROM robots_Location")
      Location_list = dictfetchall(cursor)
    return render(request,'robot/robot_list.html',{'Robot_list':Robot_list,'Category_list':Category_list,'Location_list':Location_list})

def Location_List(request):
    with connection.cursor() as cursor: 

      cursor.execute("SELECT * FROM robots_Location")
      Location_list = dictfetchall(cursor)
    return render(request,'robot/location_list.html',{'Location_list':Location_list})

def Category_List(request):
    with connection.cursor() as cursor: 

      cursor.execute("SELECT * FROM robots_Category")
      category_list = dictfetchall(cursor)
    return render(request,'robot/category_list.html',{'category_list':category_list})

def Schedule_List(request):
      schedule_list=Schedule.objects.all().order_by('-Schedule')

      return render(request,'robot/schedule_list.html',{'schedule_list':schedule_list})
def Robot_Details(request,id):
      robot_details = Robot.objects.get(id=id)
      category=Category.objects.get(id=robot_details.Category_id)
      location=Location.objects.get(id=robot_details.Location_id)
      return render(request,'robot/robot_details.html',{'robot_details':robot_details,'category':category,'location':location})

def Schedule_Details(request):
      with connection.cursor() as cursor: 
        cursor.execute("SELECT * FROM robots_Location")
        location=dictfetchall(cursor)
        cursor.execute("SELECT * FROM robots_Category")
        category = dictfetchall(cursor)  
        return render(request,'robot/schedule_details.html',{'category':category,'location':location})


def schedule_Submit(request):
     
      if request.method=="POST":
            if request.POST.get('Schedule') and request.POST.get('ProcessId') :                
                 
                  d=Schedule(Process_ID=request.POST.get('ProcessId'),Schedule=request.POST.get('Schedule'),Flag=False,Robot_id=request.POST.get('id'))
                  d.save()
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT * FROM robots_schedule")
                        schedule_list = dictfetchall(cursor)
                        return render(request,'robot/schedule_list.html',{'schedule_list':schedule_list})
            else:
              return render(request,'robot/schedule_details.html')
      else:
        return render(request,'robot/schedule_details.html')



def Robot_Search(request):
     
      if request.method=="POST":
            if request.POST.get('RobotName') :
                  robot_name=request.POST.get('RobotName')
                  robot_details = Robot.objects.get(Name=robot_name)                  
                  robot_id=robot_details.id
                  categoryName=Category.objects.get(id=robot_details.Category_id)
                  locationName=Location.objects.get(id=robot_details.Location_id)               
                  return render(request,'robot/schedule_details.html',{'robot_details':robot_details,'categoryName':categoryName,'locationName':locationName})
            pass
      else:
        return render(request,'robot/schedule_details.html',{'robot_details':robot_details})
def Robot_Listing_Search(request):
     
      if request.method=="POST":
            if request.POST.get('RobotName') :
                  robot_name=request.POST.get('RobotName')
                  robot_details = Robot.objects.get(Name=robot_name) 
                                 
                  robot_id=robot_details.id
                  categoryName=Category.objects.get(id=robot_details.Category_id)
                  locationName=Location.objects.get(id=robot_details.Location_id)
                  with connection.cursor() as cursor:
                        cursor.execute("SELECT * FROM robots_robot where Name='"+robot_name+"'" )
                        Robot_list = dictfetchall(cursor)               
                  return render(request,'robot/robot_list.html',{'Robot_list':Robot_list})
            pass
      else:
        return render(request,'robot/robot_list.html')
def History_List(request):
    with connection.cursor() as cursor:
      cursor.execute("select  [Start],[Stop],[Forward],[Backward],[Backward_Error],[Status],[Process_ID_id],[Robot_id], (select name from robots_robot where id= robot_id)from robots_history" )
      history_list = dictfetchall(cursor)

      cursor.execute("SELECT * FROM robots_Category")
      Category_list = dictfetchall(cursor)

      cursor.execute("SELECT * FROM robots_Location")
      Location_list = dictfetchall(cursor)
    return render(request,'robot/history_list.html',{'history_list':history_list,'Category_list':Category_list,'Location_list':Location_list})

def History_Listing_Search(request):
     
      if request.method=="POST":
            if request.POST.get('ProcessId') :
                  process_id=request.POST.get('ProcessId')                  
                  if History.objects.filter(Process_ID_id=process_id).exists():                        
                        robot_id= (History.objects.get(Process_ID=process_id)).Robot_id
                        robot_name=Robot.objects.get(id=robot_id) 
                        with connection.cursor() as cursor:
                          cursor.execute("select  [Start],[Stop],[Forward],[Backward],[Backward_Error],[Status],[Process_ID_id],Robot_id, (select name from robots_robot where id= robot_id)from robots_history where Process_ID_id='"+process_id+"'" )
                          history_list = dictfetchall(cursor)                                  
                  else:
                        return render(request,'robot/history_list.html')
                                            
                  return render(request,'robot/history_list.html',{'history_list':history_list,'robot_name':robot_name})
            pass
      else:
        return render(request,'robot/history_list.html')

def History_Details(request,Process_ID):
      history_details = History.objects.get(Process_ID=Process_ID)
      robot_id=history_details.Robot_id
      robot_details = Robot.objects.get(id=robot_id)
      category=Category.objects.get(id=robot_details.Category_id)
      location=Location.objects.get(id=robot_details.Location_id)      
      robot_name=Robot.objects.get(id=robot_id)
      return render(request,'robot/history_details.html',{'history_details':history_details,'category':category,'location':location,'robot_name':robot_name})
   
def Schedule_edit(request,Process_ID):
     
      schedule_details = Schedule.objects.get(Process_ID=Process_ID)
      robot_id=schedule_details.Robot_id
      robot_details = Robot.objects.get(id=robot_id)
      category=Category.objects.get(id=robot_details.Category_id)
      location=Location.objects.get(id=robot_details.Location_id)      
      robot_name=Robot.objects.get(id=robot_id)
      return render(request,'robot/schedule_edit.html',{'robot_details':robot_details,'schedule_details':schedule_details,'category':category,'location':location})

def Schedule_Update(request):
     
      if request.method=="POST":
            if request.POST.get('Schedule') and request.POST.get('ProcessId') : 
               
                 ''' a= Schedule.objects.get(Process_ID=request.POST.get('ProcessId'))
                 a.Schedule=request.POST.get('Schedule')
                 a.save() '''
                 
                 schedule_time = datetime.strptime(request.POST.get('Schedule'),'%m/%d/%Y %H:%M %p')
                 Schedule.objects.filter(Process_ID=request.POST.get('ProcessId')).update(Schedule=schedule_time)
                 with connection.cursor() as cursor:
                   cursor.execute("SELECT * FROM robots_schedule order by schedule desc")
                   schedule_list = dictfetchall(cursor)
            return render(request,'robot/schedule_list.html',{'schedule_list':schedule_list})
            pass
      else:
        return render(request,'robot/schedule_list.html')
def Schedule_Delete(request,Process_ID):
      Schedule.objects.filter(Process_ID=Process_ID).delete()
      with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM robots_schedule")
            schedule_list = dictfetchall(cursor)
      return render(request,'robot/schedule_list.html',{'schedule_list':schedule_list})
            
    

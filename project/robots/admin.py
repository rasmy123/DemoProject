from django.contrib import admin
 


# Register your models here.
from .models import Robot
admin.site.register(Robot)

from .models import Category
admin.site.register(Category)

from .models import Location
admin.site.register(Location)

from .models import Schedule
admin.site.register(Schedule)

from .models import History
admin.site.register(History)


admin.site.site_header="LUCA ROBOTICS Admin"
admin.site.site_title="LUCA ROBOTICS Admin"
admin.site.site_url = 'http://127.0.0.1:8000/robots/home'
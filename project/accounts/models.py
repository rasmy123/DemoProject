from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _



class Profile( models.Model):
    user=models.OneToOneField  (User,verbose_name=("User"),on_delete=models.CASCADE)   
    name=models.CharField(_("Full Name:"),max_length=50) 
    address=models.CharField(_("Address:"),max_length=50)
    who_is_me=models.TextField(_("Notes:"),max_length=500) 
   
    def __str__ (self):
            return self.name
class Meta:
    verbose_name=_("Profile")
    verbose_name_plural=_("Profiles")


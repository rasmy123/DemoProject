from django.db import models
STATUS_CHOICES = [
    ('IOT', 'INTERNET OF THINGS'),
    ('MANUAL', 'MANUAL'),
    ('SWITCH', 'SWICTH CLICK'),
    ('LS', 'LOCAL SCHEDULE'),
    
]


class Category(models.Model):
    Name=models.CharField(max_length=50)
    Description=models.TextField(max_length=500,null=True,blank=True)
    def __str__ (self):
            return self.Name

class Location(models.Model):
    Name=models.CharField(max_length=50)
    Group=models.CharField(max_length=50,null=True,blank=True)
    Description=models.TextField(max_length=500,null=True,blank=True)
    def __str__ (self):
            return self.Name
class Robot( models.Model):
    Name=models.CharField(max_length=50)
    Model=models.CharField(max_length=50) 
    SN=models.CharField(max_length=50) 
    Software=models.CharField(max_length=50,null=True,blank=True)
    MAC=models.CharField(max_length=50,null=True,blank=True) 
    Category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)   
    Location=models.ForeignKey(Location,on_delete=models.SET_NULL,null=True,blank=True)  
    Description=models.TextField(null=True,blank=True)
   
    def __str__ (self):
        return self.Name
class Schedule(models.Model):
    
    Process_ID=models.CharField(primary_key=True,max_length=100)  
    Schedule=models.DateTimeField()
    Flag=models.BooleanField(default=False)
    Robot=models.ForeignKey(Robot,on_delete=models.SET_NULL,null=True)

    def __str__ (self):
        return str(self.Process_ID)
        
class History(models.Model):
    Process_ID=models.ForeignKey(Schedule,on_delete=models.SET_NULL,null=True) 
    Robot=models.ForeignKey(Robot,on_delete=models.SET_NULL,null=True)
    Start=models.DateTimeField(null=True,blank=True)
    Stop=models.DateTimeField(null=True,blank=True)
    Forward=models.DateTimeField(null=True,blank=True)
    Backward=models.DateTimeField(null=True,blank=True)
    Backward_Error=models.DateTimeField(null=True,blank=True)
    Status=models.CharField(max_length=50,choices=STATUS_CHOICES)

    def __str__ (self):
        return str(self.Process_ID)




        





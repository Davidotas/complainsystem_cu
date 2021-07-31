from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from six import python_2_unicode_compatible

from django.core.validators import RegexValidator
from datetime import datetime

class Meta:

    app_label = 'HelpDesk'
class Profile(models.Model):
    typeuser =(('student','student'),('staff', 'staff'),('admin', 'admin'))
    Departments=(('CSIS',"CSIS"),('Academic',"Academic"),('Student Affairs',"Student Affairs"),('Finance',"Finance"),('Other',"Other"))
    COL=(('CoE','COE'),('CDS','CDS'),('CST','CST')) #change college names

    Department=models.CharField(choices=Departments,null=True,max_length=200)
    user =models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    college=models.CharField(max_length=29,choices=COL,blank=True)

    type_user=models.CharField(max_length=20,default='student',choices=typeuser)

    CB=(('STAFF',"STAFF"),('STUDENT',"STUDENT"),('GUEST',"GUEST"),('OTHER',"OTHER"))

    Course=models.CharField(choices=CB,max_length=29,default='COM')

    def __str__(self):
        return self.college

    def __str__(self):
        return self.user.username
    
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

'''@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()'''


class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    Departments=(('CSIS',"CSIS"),('Academic',"Academic"),('Student Affairs',"Student Affairs"),('Finance',"Finance"),('Other',"Other"))
    
    Subject=models.CharField(max_length=200,blank=False,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    
    Department=models.CharField(choices=Departments,null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    
   
    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.now()
        super(Complaint, self).save(*args, **kwargs)
    
    def __str__(self):
     	return self.get_Department_display()
    def __str__(self):
 	    return str(self.user)

class Grievance(models.Model):
    guser=models.OneToOneField(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.guser
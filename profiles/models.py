from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Institute(models.Model):
    name = models.CharField(max_length=50)
    affiliationno = models.CharField(max_length=10)
    Pincode = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

class StudentProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50,default="")
    lastName = models.CharField(max_length=50,default="")
    mail = models.EmailField(default="")
    phone = models.IntegerField(default=0)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE,default="")
    rollNumber = models.CharField(max_length=15,default="")
    address = models.CharField(max_length=50,default="")
    Pincode = models.IntegerField(default=0)
    batch = models.CharField(max_length=8,default="",blank=True)
    
    def __str__(self) -> str:
        return self.firstName
    
    def save(self,*args,**kwargs):
        group = Group.objects.get(name='student')
        self.user.groups.add(group)
        self.user.email = self.mail
        self.user.save()
        return super().save(*args, **kwargs)



class TeacherProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50,default="")
    lastName = models.CharField(max_length=50,default="")
    mail = models.EmailField(default="")
    
    def __str__(self) -> str:
        return self.name
    
    def save(self,*args,**kwargs):
        group = Group.objects.get(name='student')
        self.user.groups.add(group)
        self.user.email = self.mail
        self.user.save()
        return super().save(*args, **kwargs)
    

from cv2 import exp
from django.db import models
# from django.contrib.auth.models import AbstractBaseUser

GENDER = [('Male','M'),("Female",'F'),("Other",'O')]
ED = [('Mtriculate','M'),("Intermediat","I"),("Graduate","G")]
Exp = [("0-2 Years",'poor'),("2-4 years","Intermediat"),("4-6 Years","Good")]

# Create your models here.
class senior_citizen(models.Model):
    name = models.CharField("Name",max_length=120)
    number = models.CharField("Phone",max_length=10,primary_key=True)
    age = models.IntegerField("Age")
    gender = models.CharField("Gender",choices=GENDER,max_length=10)
    address1 = models.CharField("Address line 1",max_length=1024)
    address2 = models.CharField("Address line 2",max_length=1024)
    pin_code = models.CharField("Pincode",max_length=7)
    city = models.CharField("City",max_length=50)
    
    profile_pic = models.ImageField(blank=True,upload_to = "media/profile_pics_senior", null=True)
    password = models.CharField(max_length=12)

    
    def __str__(self):
        return self.name

class relative(models.Model):
    name = models.CharField("Name",max_length=120)
    number = models.CharField("Phone",max_length=10,primary_key=True)
    age = models.IntegerField("Age")
    gender = models.CharField("Gender",choices=GENDER,max_length=10)
    address1 = models.CharField("Address line 1",max_length=1024)
    address2 = models.CharField("Address line 2",max_length=1024)
    pin_code = models.CharField("Pincode",max_length=7)
    city = models.CharField("City",max_length=50)
    password = models.CharField(max_length=12)
    profile_pic = models.ImageField(blank=True,upload_to = "media/profile_pics_relative")
    
    def __str__(self):
        return self.name

class CareTakerInfo(models.Model):

    name = models.CharField("Name",max_length=50)
    number = models.CharField("Phone",max_length=10)
    age = models.IntegerField("Age")
    gender = models.CharField("Gender",choices=GENDER,max_length=10)
    adhar_num = models.CharField("Adhaar",max_length=12,primary_key=True)
    bank_num = models.CharField("Bank Account",max_length=20)

    Ed_q = models.CharField("Educational Qualifications",choices=ED,max_length=50)
    exp = models.CharField("Experience",choices=Exp,max_length=120)

    address1 = models.CharField("Address line 1",max_length=1024)
    address2 = models.CharField("Address line 2",max_length=1024)
    pin_code = models.CharField("Pincode",max_length=7)
    city = models.CharField(max_length=50)
    
    resume_drive = models.URLField("Resume drive link",blank=True)
    profile_pic = models.ImageField(blank=True,upload_to = "media/profile_pics_caretaker")
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.name
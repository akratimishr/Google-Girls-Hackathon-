from unicodedata import name
from django.forms import Form
from django.shortcuts import render
from matplotlib.pyplot import title

from basic.models import CareTakerInfo, senior_citizen
# from . import forms
# from .models import AccessRecord
# from basic.form1 import UserForm, UserProfileInfoForm

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from basic.all_forms import Form_senior, form_CareTakerInfo, form_relative, senior_login

# Create your views here.


def index(request):
    return render(request, 'basic/index.html')


def form1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phonenum = request.POST.get("Phonenum")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        Address_Line_1 = request.POST.get("Address Line 1")
        Address_Line_2 = request.POST.get("Address Line 1")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pin = request.POST.get("pin")
        photo = request.POST.get("photo")

        senior_citizen.objects.create(name=name,
                                      number=phonenum,
                                      age=age,
                                      gender=gender,
                                      address1=Address_Line_1,
                                      address2=Address_Line_2,
                                      pin_code=pin,
                                      city=city,
                                      state=state,
                                      profile_pic=photo)

    contex = {}
    return render(request, 'basic/form1.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("basic:home"))


def login_relative(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username , password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("basic:home"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and fail")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,"basic/login_relative.html",{})


def login_citizen(request):
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username , password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("basic:home"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and fail")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,"basic/login_citizen.html",{})


def login_care(request):
    if request.method == "POST":
        user_form = senior_login(data=request.POST)
        username = user_form["username"]
        password = user_form["password"]

        user = authenticate(username=username , password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("basic:home"))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and fail")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,"basic/login_caretaker.html",{})


def register_senior(request):
    registered = False

    if request.method == "POST":
        user_form = Form_senior(data=request.POST)
        temp=request.POST['gender']
        print(temp)
        if user_form.is_valid():
            user = user_form.save()
            user.password = make_password('password')

            if "profile_pic" in request.FILES:
                user.profile_pic = request.FILES["profile_pic"]

            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = Form_senior()

    return render(request,"basic/senior_register.html",
                            {"user_form": user_form,
                            "registered": registered,})


def register_caretaker(request):
    registered = False

    if request.method == "POST":
        user_form = form_CareTakerInfo(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.password = make_password('password')

            if "profile_pic" in request.FILES:
                user.profile_pic = request.FILES["profile_pic"]

            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = form_CareTakerInfo()

    return render(request,"basic/ctaker_register.html",
                            {"user_form": user_form,
                            "registered": registered,})


def register_relative(request):
    registered = False

    if request.method == "POST":
        user_form = form_relative(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.password = make_password('password')

            if "profile_pic" in request.FILES:
                user.profile_pic = request.FILES["profile_pic"]

            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = form_relative()

    return render(request,"basic/relative_register.html",
                            {"user_form": user_form,
                            "registered": registered,})



def record(request):

    caretaker_info = CareTakerInfo.objects.order_by('name')
    date_dict = {"access_records": caretaker_info}
    return render(request,"basic/services.html",context=date_dict)
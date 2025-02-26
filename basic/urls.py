from os import name
from django.urls import path
from .views import index, login_care, login_relative,login_citizen, record, register_caretaker, register_relative, register_senior

app_name = 'basic'
urlpatterns = [
    path("",index, name="home"),
    path("relative_login/",login_relative,name="login_relative"),
    path("citizen_login/",login_citizen,name="login_citizen"),
    path("caretaker_login/",login_care,name="login_care"),
    path("relative_register/",register_relative,name="register_relative"),
    path("relative_senior_citizen/",register_senior,name="register_citizen"),
    path("register_caretaker/",register_caretaker,name="register_care"),
    path("services/",record,name="records"),
]
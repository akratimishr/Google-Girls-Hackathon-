from django.contrib import admin

from basic.models import CareTakerInfo, relative, senior_citizen

# Register your models here.
admin.site.register(senior_citizen)
admin.site.register(relative)
admin.site.register(CareTakerInfo)
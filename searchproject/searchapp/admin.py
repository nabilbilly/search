from django.contrib import admin

# Register your models here.
from .models import *

class CityAdmin(admin.ModelAdmin):
    list_display = ("name","state")

admin.site.register(City,CityAdmin)
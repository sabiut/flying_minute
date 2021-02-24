from django.contrib import admin

from django.contrib import admin
from django.contrib.admin import site
from .models import *

admin.site.register(BoardMembers)
admin.site.register(fly_minute)
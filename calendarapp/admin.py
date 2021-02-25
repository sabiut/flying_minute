from django.contrib import admin
from django.contrib.admin import site
from .models import *

admin.site.register(Event)
admin.site.register(EventMember)
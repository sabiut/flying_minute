from django.contrib import admin

from django.contrib import admin
from django.contrib.admin import site
from .models import *
from calendarapp.models import IndicatePresence

admin.site.register(BoardMembers)
admin.site.register(fly_minute)
admin.site.register(MembersPresent)
admin.site.register(Comments)
admin.site.register(IndicatePresence)

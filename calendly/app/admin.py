from django.contrib import admin
from .models import User, CalendarEvents

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['date', 'start_time', 'end_time', 'reason']

admin.site.register(User)
admin.site.register(CalendarEvents, EventAdmin)

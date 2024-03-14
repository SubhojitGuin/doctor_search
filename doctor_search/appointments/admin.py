from django.contrib import admin
from .models import Appointment


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date', 'start_time', 'end_time', 'notes',)
    search_fields = ('doctor', 'patient', 'date', 'start_time', 'end_time', 'notes',)
    list_filter = ('doctor', 'patient', 'date',)
    ordering = ('date', 'start_time',)


admin.site.register(Appointment, AppointmentAdmin)

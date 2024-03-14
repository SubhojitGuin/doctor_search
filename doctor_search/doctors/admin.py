from django.contrib import admin
from .models import Doctor


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'email', 'phone_number', 'address', 'website', 'description', 'user',)
    search_fields = ('name', 'specialty', 'email', 'phone_number', 'address', 'website', 'description',)
    list_filter = ('specialty', 'user', 'name',)
    ordering = ('name',)


admin.site.register(Doctor, DoctorAdmin)


# class DayAdmin(admin.ModelAdmin):
#     list_display = ('day',)
#     search_fields = ('day',)
#     list_filter = ('day',)
#     ordering = ('day',)
#
# admin.site.register(Day, DayAdmin)
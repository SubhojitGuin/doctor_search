from django.contrib import admin
from .models import User


# Register your models here.
# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',)
    search_fields = ('username', 'email', 'first_name', 'last_name',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    ordering = ('username',)


admin.site.register(User, UserAdmin)

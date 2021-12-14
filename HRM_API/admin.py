from django.contrib import admin
from .models import Employee,Department,Attendance, Employer, User

# Register your models here.
# admin.site.register([Employee,Department,Attendance, User])

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', )

@admin.register(Employer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', )

@admin.register(Employee)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', )

@admin.register(Department)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'history', )

# @admin.register(Attendance)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'last_name', 'first_name', )

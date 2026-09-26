from django.contrib import admin

# Register your models here.
from .models import Student

# Making class named StudentAdmin just to set list display
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "gender")

admin.site.register(Student, StudentAdmin)



# Lets say if we didn't made class so we can register admin by simple writing:
# admin.site.register(Student)
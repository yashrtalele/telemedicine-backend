from django.contrib import admin
from .models import Doctors
# Register your models here.
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['did', 'email', 'phone', 'availability']

admin.site.register(Doctors, DoctorsAdmin)
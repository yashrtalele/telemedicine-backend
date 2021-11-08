from django.contrib import admin
from .models import Patients
# Register your models here.
class PatientsAdmin(admin.ModelAdmin):
    list_display = ['pid', 'email', 'phone']

admin.site.register(Patients, PatientsAdmin)
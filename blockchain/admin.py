from django.contrib import admin
from .models import FileHash
# Register your models here.
class FileHashAdmin(admin.ModelAdmin):
    list_display = ['doctor_id', 'patient_id', 'file_ipfs_hash', 'tx_hash']

admin.site.register(FileHash, FileHashAdmin)
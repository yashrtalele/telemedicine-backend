from django.db import models

# Create your models here.
class FileHash(models.Model):
    doctor_id = models.UUIDField()
    patient_id = models.UUIDField()
    file_ipfs_hash=models.TextField(null=True)
    tx_hash = models.TextField()

    class Meta:
        verbose_name_plural = "Blockchain"

class File(models.Model):
    doctor_id = models.UUIDField(null=False, default=None)
    patient_id = models.UUIDField(null=False, default=None)
    file = models.FileField(upload_to="blockchain/", null=True, default=None)
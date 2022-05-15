from django.db import models

# Create your models here.
class FileHash(models.Model):
    doctor_id = models.UUIDField()
    patient_id = models.UUIDField()
    tx_hash = models.TextField()

    class Meta:
        verbose_name_plural = "Blockchain"
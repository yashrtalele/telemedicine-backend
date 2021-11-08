from django.db import models

# Create your models here.
class Patients(models.Model):
    pid = models.UUIDField(primary_key=True, unique = True)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=255, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.IntegerField()
    blood_group = models.CharField(max_length=60)
    height = models.DecimalField(decimal_places=2, max_digits=4)
    weight = models.DecimalField(decimal_places=2, max_digits=4)
    allergies = models.TextField()

    class Meta:
        verbose_name_plural = "Patients"

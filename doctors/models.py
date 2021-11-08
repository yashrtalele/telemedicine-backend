from django.db import models

# Create your models here.
class Doctors(models.Model):
    did = models.UUIDField(primary_key=True, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=255, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.IntegerField()
    education = models.TextField()
    qualification = models.TextField()
    specialty = models.TextField()
    experience = models.IntegerField()
    availability = models.BooleanField(default=True)
    rmp = models.CharField(max_length=255, unique=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Doctors"
from rest_framework import serializers
from .models import Patients

class PatientsSerializer(serializers.ModelSerializer):
    pid = serializers.UUIDField()
    email = serializers.EmailField(max_length=255, min_length=3)
    phone = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    pincode = serializers.IntegerField()
    blood_group = serializers.CharField(max_length=60)
    height = serializers.DecimalField(decimal_places=2, max_digits=4)
    weight = serializers.DecimalField(decimal_places=2, max_digits=4)
    allergies = serializers.CharField()

    class Meta:
        model = Patients
        fields = ['pid', 'email', 'phone', 'first_name', 'last_name', 'gender', 'address', 'city', 
        'pincode', 'blood_group', 'height', 'weight', 'allergies']
from rest_framework import serializers
from .models import Doctors

class DoctorsSerializer(serializers.ModelSerializer):
    did = serializers.UUIDField()
    email = serializers.EmailField(max_length=255, min_length=3)
    phone = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    pincode = serializers.IntegerField()
    education = serializers.CharField()
    qualification = serializers.CharField()
    specialty = serializers.CharField()
    experience = serializers.IntegerField()
    availability = serializers.BooleanField(default=True)
    rmp = serializers.CharField(max_length=255)

    class Meta:
        model = Doctors
        fields = ['did', 'email', 'phone', 'first_name', 'last_name', 'gender', 'address', 'city', 
        'pincode', 'education', 'specialty', 'qualification', 'experience', 'availability', 'rmp']
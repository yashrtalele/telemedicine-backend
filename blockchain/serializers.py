from rest_framework import serializers
from .models import FileHash

class FileHashSerializer(serializers.ModelSerializer):
    doctor_id = serializers.UUIDField()
    patient_id = serializers.UUIDField()
    tx_hash = serializers.CharField()

    class Meta:
        model = FileHash
        fields = ['doctor_id', 'patient_id', 'tx_hash']
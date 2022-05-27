from rest_framework import serializers
from .models import FileHash, File

class FileHashSerializer(serializers.ModelSerializer):
    doctor_id = serializers.UUIDField()
    patient_id = serializers.UUIDField()
    file_ipfs_hash = serializers.CharField()
    tx_hash = serializers.CharField()

    class Meta:
        model = FileHash
        fields = ['doctor_id', 'patient_id', 'file_ipfs_hash', 'tx_hash']

class FileSerializer(serializers.ModelSerializer):
    doctor_id = serializers.UUIDField()
    patient_id = serializers.UUIDField()
    file = serializers.FileField()
    
    class Meta:
        model = File
        fields = ['file', 'doctor_id', 'patient_id']
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .models import Patients
from .serializers import PatientsSerializer
from .renderers import UserRenderer

# Create your views here.
class PatientsView(generics.GenericAPIView):
    serializer_class = PatientsSerializer
    renderer_classes = (UserRenderer,)

    def get(self, format=None):
        patients = Patients.objects.all()
        serializer = PatientsSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetPatient(generics.GenericAPIView):
    serializer_class = PatientsSerializer
    renderer_classes = (UserRenderer,)

    def get(self, request, id, format=None):
        patient = get_object_or_404(Patients, pk=id)
        serializer = PatientsSerializer(patient)
        return Response(serializer.data, status=HTTP_200_OK)
    
class CreatePatient(generics.GenericAPIView):
    serializer_class = PatientsSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        data = request.data
        serializer = PatientsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class DeletePatient(generics.GenericAPIView):
    serializer_class = PatientsSerializer
    renderer_classes = (UserRenderer,)

    def delete(self, request, id, format=None):
        patient = get_object_or_404(Patients, pk=id)
        patient.delete()
        return Response(status.HTTP_200_OK)

class UpdatePatient(generics.GenericAPIView):
    serializer_class = PatientsSerializer
    renderer_classes = (UserRenderer,)

    def put(self, request, id, format=None):
        patient = get_object_or_404(Patients, pk=id)
        serializer = PatientsSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .models import Doctors
from .serializers import DoctorsSerializer
from .renderers import UserRenderer

# Create your views here.
class DoctorsView(generics.GenericAPIView):
    serializer_class = DoctorsSerializer
    renderer_classes = (UserRenderer,)
    def get(self, format=None):
        doctors = Doctors.objects.all()
        serializer = DoctorsSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetDoctor(generics.GenericAPIView):
    serializer_class = DoctorsSerializer
    renderer_classes = (UserRenderer,)
    def get(self, request, id, format=None):
        doctor = get_object_or_404(Doctors, pk=id)
        serializer = DoctorsSerializer(doctor)
        return Response(serializer.data)

class CreateDoctor(generics.GenericAPIView):
    serializer_class = DoctorsSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        data = request.data
        serializer = DoctorsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeleteDoctor(generics.GenericAPIView):
    serializer_class = DoctorsSerializer
    renderer_classes = (UserRenderer,)

    def delete(self, request, id, format=None):
        doctor = get_object_or_404(Doctors, pk=id)
        doctor.delete()
        return Response(status.HTTP_200_OK)

class UpdateDoctor(generics.GenericAPIView):
    serializer_class = DoctorsSerializer
    renderer_classes = (UserRenderer,)
    
    def put(self, request, id, format=None):
        doctor = get_object_or_404(Doctors, pk=id)
        serializer = DoctorsSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
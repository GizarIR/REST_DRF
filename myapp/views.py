from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *


class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SClassViewset(viewsets.ModelViewSet):
    queryset = SClass.objects.all()
    serializer_class = SClassSerializer

class StudentViewest(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = SClassSerializer

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import  Response
from rest_framework import status

from .serializers import *
from .models import *


class SchoolViewset(viewsets.ModelViewSet):
    # (минимальные настройки)
    # queryset = School.objects.all() # # (минимальные настройки)
    # Еcли хотим переопределить метод Delete и не удалаять объект Школа а пометить как не активный
    queryset = School.objects.all().filter(is_active=True)
    serializer_class = SchoolSerializer
    # end (минимальные настройки)

    # можно переопределять функции
    # Например мы можем добавить метод .list() в класс SchoolViews, чтобы он ничего не возвращал.
    # Аналогично можно переопределить и методы .post(), .patch(), .put(), .destroy()
    # def list(self, request, format=None):
    #     return Response([])

    def destroy(self, request, pk, format=None): # путь в постмане http://127.0.0.1:8000/schools/5/
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SClassViewset(viewsets.ModelViewSet):
    queryset = SClass.objects.all()
    serializer_class = SClassSerializer

class StudentViewest(viewsets.ModelViewSet):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer

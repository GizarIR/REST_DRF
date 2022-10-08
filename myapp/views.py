import django_filters
from django.shortcuts import render
from rest_framework import viewsets, permissions
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
    # Вариант 2 реализации фильтров

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["grade", "school_id"]

class StudentViewest(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # ВАЖНО: permission_classes переопределяет стандартное значение в DEFAULT_PERMISSION_CLASSES, а значит,
    # если мы хотим отменить, то достаточно переопределить как permission_classes=[permissions.AllowAny]
    # или вообще permission_classes=[]
    permission_classes = [permissions.IsAuthenticated]

    # Вариант 1 реализации фильтров
    # Данную функцию можно не писать если реализоввывать фильтры django-filter
    #  Реперь можно задать  запрос вида GET localhost:8000/students?school_id=3, то получим список только тех учеников,
    #  которые учатся в школе с id=1. Помимо этого мы можем указать id класса GET localhost:8000/students?class_id=1.
    def get_queryset(self):
        queryset = Student.objects.all()
        school_id = self.request.query_params.get('school_id', None)
        sclass_id = self.request.query_params.get('class_id', None)
        if school_id is not None:
            queryset = queryset.filter(sclass__school_id=school_id)
        if sclass_id is not None:
            queryset = queryset.filter(sclass_id=sclass_id)
        return queryset
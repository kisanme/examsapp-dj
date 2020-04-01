from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ExamSerializer
from .models import Exam

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.filter(published_status=True).order_by('-pk')
    serializer_class = ExamSerializer

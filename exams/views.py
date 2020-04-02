from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import ExamSerializer, QuestionSerializer
from .models import Exam, Question


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.filter(published_status=True).order_by('-pk')
    serializer_class = ExamSerializer


class QuestionViewSet(APIView):
    def get(self, request, pk, format=None):
        questions = Question.objects.filter(exam_id=pk)
        serialized = QuestionSerializer(questions, many=True)
        return Response(serialized.data)

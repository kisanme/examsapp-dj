from rest_framework import serializers
from .models import Exam, Question, Answers


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title', 'exam_duration', 'pub_date')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'answer_text', 'answer_image', 'answer_type')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'question_type', 'answers')
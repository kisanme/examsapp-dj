"""
DB related model imports
"""
from pprint import pprint
from django.db.models import Count
from django.db import models
from froala_editor.fields import FroalaField


class Exam(models.Model):
    """
    Exam Model
    """
    title = models.CharField(max_length=200)
    description = FroalaField(blank=True)
    exam_duration = models.DurationField(null=True)
    published_status = models.BooleanField(default=False)
    pub_date = models.DateTimeField('published date')


    def question_count(self):
        questions = Question.objects.filter(exam_id=self.id)
        return len(questions)

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    Question Model
      - Relates to the Exam model in one-to-many relationship
    """
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    question_text = FroalaField()
    question_type = models.CharField(max_length=50, default='') 

    def __str__(self):
        return self.question_text


class Answers(models.Model):
    """
    Answers Model
     - Relates to the Question Model with one to many relationship
    """
    IMAGE_ANS = 'IM'
    TEXT_ANS = 'TX'
    ANSWER_TYPES = [
        (IMAGE_ANS, 'Image'),
        (TEXT_ANS, 'Text'),
    ]
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = FroalaField(blank=True)
    answer_image = models.ImageField(blank=True)
    answer_type = models.CharField(max_length=2, choices=ANSWER_TYPES, default=TEXT_ANS)

    def answers_for_question(self):
        return Answers.objects.filter(question_id=self.question_id)

    def __str__(self):
        answers = self.answers_for_question()
        current_answer = Answers.objects.get(pk=self.id)
        current = 1
        for i in answers:
            if i == current_answer:
                return 'Answer ' + str(current)
            else:
                current += 1

        return str(current)


class CorrectAnswer(models.Model):
    """
    Pivot table which contains Question id and Answer id for correct answers
    """
    question = models.ForeignKey(Question, related_name='target_question', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, related_name='correct_answer', on_delete=models.CASCADE)

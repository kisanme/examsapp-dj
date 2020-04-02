from django.contrib import admin
from .models import Exam, Question, Answers


class InlineAnswers(admin.TabularInline):
    model = Answers
    extra = 4
    max_num = 5
    fields = [
        'answer_text',
        'answer_image',
        'answer_type',
        # 'correct_answer'
    ]


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    list_display = ["exam", "question_text", "question_type"]
    search_fields = ['question_text']
    fieldsets = (
        (None, {
            "fields": [
                "exam", 
                "question_text",
                "question_type",
            ],
        }),
    )
    inlines = [InlineAnswers]


class ExamAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "title",
                "exam_duration",
                "pub_date",
                "published_status"
            ),
        }),
    )


# Register your models here.
admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)

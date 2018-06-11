from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'data_wydarzenia', "pub_date"]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)  
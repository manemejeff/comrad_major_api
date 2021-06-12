from django.contrib import admin
from .models import Question, OptionAnswer, TextAnswer

# Register your models here.

class AnswerInline(admin.TabularInline):
    model = OptionAnswer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(OptionAnswer)
admin.site.register(TextAnswer)
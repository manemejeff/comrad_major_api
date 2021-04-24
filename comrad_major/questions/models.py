from django.db import models
from interrogations.models import Interrogation


# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    interrogation = models.ForeignKey(Interrogation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    # options

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()


class Types(models.Model):
    pass


class Options(models.Model):
    pass
    # options_list


class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Question: {self.question.text}, answer: {self.text}"
    # interrogation_name
    # question
    # chosen_options
    # answer_text
    # user

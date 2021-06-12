from django.db import models
from interrogations.models import Interrogation


# Create your models here.


class Question(models.Model):
    ONE = 1
    MANY = 2
    TEXT = 3
    TYPE_CHOICES = [
        (ONE, 'One'),
        (MANY, 'Many'),
        (TEXT, 'Text'),
    ]

    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    interrogation = models.ForeignKey(Interrogation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    type = models.SmallIntegerField(
        choices=TYPE_CHOICES,
        default=ONE
    )
    # options

    def __str__(self):
        return self.text

    def get_answers(self):
        return self.answer_set.all()


class OptionAnswer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Question: {self.question.text}, answer: {self.text}"


class TextAnswer(models.Model):
    text = models.TextField(max_length=500)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Question: {self.question.text}, answer: {self.text}"


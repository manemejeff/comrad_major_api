from django.db import models
from interrogations.models import Interrogation
from questions.models import Answer
from django.contrib.auth.models import User


# Create your models here.

class Result(models.Model):
    interrogation = models.ForeignKey(Interrogation, on_delete=models.CASCADE)
    chosen_answer = models.ManyToManyField(Answer)
    written_answer = models.TextField(
        max_length=1000,
        blank=True,
    )
    user_id = models.BigIntegerField(default=0)

    def __str__(self):
        return self.pk

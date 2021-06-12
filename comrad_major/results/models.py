from django.db import models
from interrogations.models import Interrogation
from questions.models import OptionAnswer, TextAnswer
from django.contrib.auth.models import User


# Create your models here.

class Result(models.Model):
    interrogation = models.ForeignKey(Interrogation, on_delete=models.CASCADE)
    chosen_answer = models.ForeignKey(
        OptionAnswer,
        on_delete=models.CASCADE,
        blank=True,
        default=None
        )
    written_answer = models.ForeignKey(
        TextAnswer,
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )
    user_id = models.BigIntegerField(default=0)

    def __str__(self):
        return self.pk

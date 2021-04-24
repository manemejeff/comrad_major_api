from django.db import models


# Create your models here.

class Interrogation(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    number_of_questions = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()

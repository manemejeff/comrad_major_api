from django.db import models
from interrogations.models import Interrogation
from django.contrib.auth.models import User

# Create your models here.

class Results(models.Model):
    interrogation = models.ForeignKey(Interrogation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk
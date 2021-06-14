from django.contrib import admin

from .models import PollQuestion, PollChoice

# Register your models here.

admin.site.register(PollQuestion)
admin.site.register(PollChoice)

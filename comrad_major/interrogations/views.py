from django.utils import timezone
from django.shortcuts import render
from rest_framework import viewsets
from .models import Interrogation
from .serializers import InterrogationSerializer


# Create your views here.

class InterrogationView(viewsets.ModelViewSet):
    queryset = Interrogation.objects.all()
    serializer_class = InterrogationSerializer


class ActiveInterrogationView(viewsets.ModelViewSet):
    queryset = Interrogation.objects.filter(date_end__gte=timezone.now())
    serializer_class = InterrogationSerializer

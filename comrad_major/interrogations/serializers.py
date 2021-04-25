from rest_framework import serializers
from .models import Interrogation


class InterrogationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interrogation
        fields = (
            'name',
            'description',
            'number_of_questions',
            'created',
            'date_start',
            'date_end',
        )

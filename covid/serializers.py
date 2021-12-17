from rest_framework import serializers

from covid.models import Covid


class CovidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid
        fields = '__all__'

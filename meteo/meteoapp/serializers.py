from rest_framework import serializers

from .models import Site, MeteoData

class MeteoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeteoData
        fields = ['date', 'pression', 'temp', 'humidity', 'wind', 'rain', 'co2']

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name']

from django import forms

from .models import Site, MeteoData

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name']

class MeteoDataForm(forms.ModelForm):
    class Meta:
        model = MeteoDataForm
        fields = ['site', 'date', 'pression', 'temp', 'humidity', 'wind', 'rain', 'co2']
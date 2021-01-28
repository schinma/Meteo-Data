from django.db import models
from django.db.models import Max
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Site(models.Model):

    name = models.CharField(max_length=100, unique=True)

    max_co2 = models.FloatField(null=True, blank=True)
    
    @property
    def max_temp(self):
        return self.data_list.aggregate(Max('temp'))['temp__max']

    def __str__(self):
        return self.name


class MeteoData(models.Model):

    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='data_list')

    date = models.DateTimeField(verbose_name='Date Time')
    pression = models.FloatField(verbose_name='p (mbar)')
    temp = models.FloatField(verbose_name='T (degC)')
    humidity = models.FloatField(verbose_name='rh (%)')
    wind = models.FloatField(verbose_name='wv (m/s)')
    rain = models.FloatField(verbose_name='rain (mm)')
    co2 = models.FloatField(verbose_name='CO2 (ppm)')

    def __str__(self):
        return f"Relevé du {self.date}"

@receiver(post_save, sender=MeteoData)
def save_site(sender, instance, **kwargs):
    site = instance.site
    site.max_co2 = site.data_list.aggregate(Max('co2'))['co2__max']
    site.save()

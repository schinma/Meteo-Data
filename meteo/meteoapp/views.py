from django.shortcuts import render
from django.urls import reverse
from datetime import date, time, datetime
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from rest_framework.generics import ListAPIView


from .models import Site, MeteoData
from .serializers import SiteSerializer, MeteoDataSerializer

# Create your views here.

#region Site Views
class SiteListView(ListView):
    model = Site

class SiteCreateView(CreateView):
    model = Site
    fields = ['name']
    success_url = '/site/'
    template_name_suffix = '_form'

class SiteUpdateView(UpdateView):
    model = Site
    fields = ['name']
    template_name_suffix = '_form'
    success_url = '/site/'

class SiteDeleteView(DeleteView):
    model = Site
    success_url = '/site/'

class APISiteListView(ListAPIView):
    serializer_class = SiteSerializer
    queryset = Site.objects.all()


#endregion

#region MeteoData Views

def filter_meteo_data(request, query_set):
    
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')        
    time_min = request.GET.get('time_min')
    time_max = request.GET.get('time_max')
    site = request.GET.get('site')
    
    if site != '' and site is not None:
        query_set = query_set.filter(site__name__exact=site)

    if date_min != '' and date_max is not None:
        if  time_min != '':
            datetime_min = datetime.combine(date.fromisoformat(date_min), time.fromisoformat(time_min))
        else:
            datetime_min = datetime.combine(date.fromisoformat(date_min), time(0,0,0,0))
        query_set = query_set.filter(date__gt=datetime_min)
    
    if date_max != '' and date_max is not None:
        if time_max != '':
            datetime_max = datetime.combine(date.fromisoformat(date_max), time.fromisoformat(time_max))
        else:
            datetime_max = datetime.combine(date.fromisoformat(date_max), time(0,0,0,0))
        query_set = query_set.filter(date__lt=datetime_max)
    

    return query_set

class MeteoDataListView(ListView):
    model = MeteoData
    paginate_by = 200

    def get_queryset(self):
        query_set = super().get_queryset()
        return filter_meteo_data(self.request, query_set)

class MeteoDataCreateView(CreateView):
    model = MeteoData
    fields = ['site', 'date', 'pression', 'temp', 'humidity', 'wind', 'rain', 'co2']
    template_name_suffix = '_form'
    success_url = '/data/'

class MeteoDataUpdateView(UpdateView):
    model = MeteoData
    fields = ['date', 'pression', 'temp', 'humidity', 'wind', 'co2']
    template_name_suffix = '_form'
    success_url = '/data/'

class MeteoDataDeleteView(DeleteView):
    model = MeteoData
    success_url = '/data/'

class APIMeteoDataListView(ListAPIView):
    serializer_class = MeteoDataSerializer

    def get_queryset(self):
        return filter_meteo_data(self.request, MeteoData.objects.all())
    

#endregion
from django.urls import path

from . import views

app_name = 'meteoapp'

urlpatterns = [

    path('sites/', views.SiteListView.as_view(), name='site-list'),
    path('sites/create', views.SiteCreateView.as_view(), name='site-create'),
    path('sites/<int:pk>/', views.SiteUpdateView.as_view(), name='site-update'),
    path('sites/<int:pk>/delete/', views.SiteDeleteView.as_view(), name='site-delete'),

    path('data/', views.MeteoDataListView.as_view(), name='data-list'),
    path('data/create', views.MeteoDataCreateView.as_view(), name='data-create'),
    path('data/<int:pk>/', views.MeteoDataUpdateView.as_view(), name='data-update'),
    path('data/<int:pk>/delete/', views.MeteoDataDeleteView.as_view(), name='data-delete'),

    path('api/sites/', views.APISiteListView.as_view(), name='api-site'),
    path('api/data/', views.APIMeteoDataListView.as_view(), name='api-data'),
]
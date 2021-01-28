from django.contrib import admin

from .models import Site, MeteoData

# Register your models here.
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(MeteoData)
class MeteoAdmin(admin.ModelAdmin):
    pass

import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from meteoapp.models import MeteoData, Site


class Command(BaseCommand):

    help =  """
            Permet d'insérer les données d'un fichier CSV modélisant le modèle MeteoData dans la base de données.
            Arguments: 
                - Chemin vers le fichier csv
                - Nom du site auquels appartiennent les données
            """
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=str, help='Chemin vers le fichier csv contenant les données')
        parser.add_argument('sitename', nargs=1, type=str, help='Nom du site auxquel appartiennent les données')
    
    def handle(self, *args, **options):
        df = pd.read_csv(options['filename'][0], parse_dates=['Date Time'], dayfirst=True)
        new_columns = [field.name for field in MeteoData._meta.get_fields()]
        df.columns = new_columns[2:]

        site, created = Site.objects.get_or_create(name=options['sitename'][0])

        MeteoData.objects.bulk_create(MeteoData(site=site, **values) for values in df.to_dict('records'))


# Meteo-Data

Meteo data full stack project with Django backend and Vue.js frontend for data visualisation

## Meteo Django back-end

### Project setup

#### Install dependencies
```
cd meteo
pip install -r requirements.txt
```

#### Migrations
```
python manage.py makemigrations meteoapp
python manage.py migrate
```

#### Import the data
```
python manage.py importcsv "corrected_sorted_mpi_roof_random.csv" "Site_01"
```

#### Run the development server 
```
python manage.py runserver
```

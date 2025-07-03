***************** Movies API ****************
#Created Django project: demo-django-api

#Installed djangorestframework

#Created app: movies

#Added 'rest_framework' and 'movies' to INSTALLED_APPS

#Created Movie model with fields:

  - title (CharField)

  - genre (CharField)

  - release_date (DateField)

  - rating (decimalField)

#Ran makemigrations and migrate

#Registered Movie model in admin.py

#Created MovieSerializer using ModelSerializer

#Created API views using DRF (APIView or ViewSet)

#Defined routes in movies/urls.py

#Included app URLs in main urls.py

#Tested endpoints using Postman or DRF’s web UI:

  - GET /api/movies/ – list

  - POST /api/movies/ – create

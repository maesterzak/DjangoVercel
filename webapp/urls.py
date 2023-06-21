from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('database/',  database_view, name="database_view")
]

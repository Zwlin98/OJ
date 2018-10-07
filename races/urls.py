from django.urls import path
from . import views
from django.models import *

app_name = 'races'

urlpatterns = [

    path('race/<int:race_page>', views.RaceListView.as_view(), name='race_list'),
    path('<str:id>', views.get_race, name='race')
]

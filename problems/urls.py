from django.urls import path
from . import views
app_name = 'problems'

urlpatterns = [
    path('<str:id>',views.get_problem)
]

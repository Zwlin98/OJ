from django.urls import path
from . import views
app_name = 'problems'

urlpatterns = [
    path('<int:id>',views.get_problem)
]

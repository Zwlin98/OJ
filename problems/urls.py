from django.urls import path
from . import views

app_name = 'problems'

urlpatterns = [
    path('page/<int:page>', views.ProblemListView.as_view(), name='problem_list'),
    path('<str:id>', views.get_problem, name='problem')
]

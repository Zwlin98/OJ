from django.urls import path
from . import views

app_name = 'contest'

urlpatterns = [
    path('page/<int:page>',views.ContestListView.as_view(), name='contest_list'),
    path('<str:id>',views.ContestView.as_view(), name='contest'),
    path('problem/<str:id>',views.ProblemView.as_view(), name='problem'),
]

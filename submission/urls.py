from django.urls import path
from . import views

app_name = 'submission'

urlpatterns = [
    path('', views.SubmissionListView.as_view(), name='submission_list'),
    path('<str:submission_id>', views.SubmissionView.as_view(), name='submission')
]

from django.urls import path
from . import views

app_name = 'submission'

urlpatterns = [
    path('page/<int:page>', views.SubmissionListView.as_view(), name='submission_list'),
    path('<int:submission_id>', views.SubmissionView.as_view(), name='submission'),
]

from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users, name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('active/', views.activeView.as_view()),
    path('active/<str:verify_code>', views.activeView.as_view()),
    path('reset/', views.resetpasswordView.as_view(), name='reset'),
    path('reset/<str:verify_code>', views.resetpasswordView.as_view())
]

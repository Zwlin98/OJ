from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users,),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('active/', views.ActiveView.as_view()),
    path('active/<str:verify_code>', views.ActiveView.as_view()),
    path('reset/', views.ResetPasswordView.as_view(), name='reset'),
    path('reset/<str:verify_code>', views.ResetPasswordView.as_view())
]

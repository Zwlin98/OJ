from django.urls import path,include
from . import  views
from django.contrib.auth import views as auth_views
app_name='users'

urlpatterns = [
    #path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('success/',views.success,name='success'),
    path('logout/',views.vlogout,name='logout'),
    path('profile',views.profile,name='profile')
]
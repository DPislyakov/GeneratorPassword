from generator import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('password', views.password, name = 'password'),
    path('auth', views.auth, name = 'auth')
]

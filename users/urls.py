from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
        path('', include('django.contrib.auth.urls')), # login
        path('register/', views.register, name='register'),
    ]   

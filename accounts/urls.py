from django.urls import path
from . import views 

# URLS 
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
]
from django.urls import path
from . import views 

# URLS 
urlpatterns = [
    path('login/', views.signin, name='login'),
    path('signout/', views.signout, name='signout'),
]
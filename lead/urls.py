from django.urls import path
from . import views

# URLS 
urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # USERS 
    path('users/', views.UsersListView.as_view(), name='users'),
]
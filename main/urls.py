from django.urls import path
from . import views

# URLS 
urlpatterns = [
    path('', views.index, name='index'),
    path('prods/', views.products, name='prods'),
    path('vote/<int:product_id>/<str:vote_type>/', views.vote, name='vote'),
]
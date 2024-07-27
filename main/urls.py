from django.urls import path
from . import views

# URLS 
urlpatterns = [
    path('', views.index, name='index'),
    path('prods/', views.products, name='prods'),
    path('vote/<int:product_id>/<str:vote_type>/', views.vote, name='vote'),

    # MEMBERS URLS 
    path('members_dashboard/', views.members_dashboard, name='members_dashboard'),
    path('profiles/', views.ProfilesListView.as_view(), name='profiles'),


    # MEMBERS PRODUCTS 
    path('mb_add_product/', views.MembersProductCreateView.as_view(), name='mb_add_product'),
    path('mb_products/', views.MembersProductListView.as_view(), name='mb_products'),
    path('mb_product_update/<pk>', views.MembersProductUpdateView.as_view(), name='mb_product_update'),
    path('mb_products/<pk>/delete/', views.MembersProductDeleteView.as_view(), name='mb_product_delete'),

    # my_products 
    path('my_products/', views.my_products, name='my_products'),

    # MEMBER PROFILES 
    path('update_profile/', views.update_profile, name="update_profile"),
    
]
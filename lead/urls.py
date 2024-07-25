from django.urls import path
from . import views

# URLS 
urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # USERS 
    path('users/', views.UsersListView.as_view(), name='users'),
    path('user_update/<pk>', views.user_update, name='user_update'),
    path('user_delete/<pk>', views.user_delete, name='user_delete'),
    path('add_user/', views.add_user, name='add_user'),

    # CATEGORIES 
    path('add_category/', views.CategoryCreateView.as_view(), name='add_category'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category_details/<pk>', views.CategoryDetailView.as_view(), name='category_details'),
    path('category_update/<pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # PRODUCTS
    path('add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product_update/<pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]
from django.urls import path
from . import views


app_name = "product"

urlpatterns = [
    path('product/<int:product_id>/', views.products, name='Product'),
    path('search/', views.search, name='product_search'),
]
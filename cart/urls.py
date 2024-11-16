from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='view_cart'),
    path('update-quantity/', views.update_quantity, name='update_quantity'),
    path('remove-item/', views.remove_item, name='remove_item'),
    path('complete-order/', views.complete_order, name='complete_order'),
]

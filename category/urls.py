from django.urls import path

from . import views


app_name = "category"

urlpatterns = [
    path('kadın', views.category, {'category_name': 'Kadın' }, name="Kadın"),
    path('kadın/Kadin-Giyim', views.category, {'category_name': 'Kadın-Giyim' }, name='Kadın-Giyim'),
    path('Kadın/Kadın-İç-Giyim', views.category, {'category_name': 'Kadın-İç-Giyim'}, name='Kadın-İç-Giyim'),
    path('Kadın/Spor-Giyim', views.category, {'category_name': 'Kadın-Spor-Giyim' }, name='Kadın-Spor-Giyim'),

    path('Erkek', views.category, {'category_name': 'Erkek'}, name='Erkek'),
    path('Erkek/Erkek-Giyim', views.category, {'category_name': 'Erkek-Giyim'}, name='Erkek-Giyim'),
    path('Erkek/Erkek-İç-Giyim', views.category, {'category_name': 'Erkek-İç-Giyim'}, name='Erkek-İç-Giyim' ),
    path('Erkek/Erkek-Spor-Giyim',views.category, {'category_name': 'Erkek-Spor-Giyim'}, name='Erkek-Spor-Giyim'),

    path('Anne-Çocuk', views.category, {'category_name': 'Anne-Çocuk'}, name='Anne-Çocuk'),
    path('Anne-Çocuk/Bebek-Giyim', views.category, {'category_name': 'Bebek-Giyim'}, name='Bebek-Giyim'),
    path('Anne-Çocuk/Hamile-Giyim', views.category, {'category_name': 'Hamile-Giyim'}, name='Hamile-Giyim'),
    path('Anne-Çocuk/Çocuk-Giyim', views.category, {'category_name': 'Çocuk-Giyim'}, name='Çocuk-Giyim'),

    path('Ayakkabı', views.category, {'category_name': 'Ayakkabı' }, name='Ayakkabı'),

    path('Çanta', views.category, {'category_name': 'Çanta' }, name='Çanta'),

]
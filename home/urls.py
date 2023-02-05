from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('menu', views.menu, name='menu'),
    path('breakfast', views.breakfast, name='breakfast'),
    path('main', views.main, name='main'),
    path('drinks', views.drinks, name='drinks'),
]
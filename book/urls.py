from django.urls import path
from . import views


urlpatterns = [
    path('book', views.book, name='book'),
    path('success', views.book, name='success'),
    path('fail', views.book, name='fail'),
]
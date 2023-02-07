from django.urls import path
from . import views


urlpatterns = [
    path('mybookings', views.mybookings, name='mybookings'),
    path('edit/<book_id>', views.edit_book, name='editbook'),
    path('toggle/<book_id>', views.toggle_book, name='togglebook'),
    path('delete/<book_id>', views.delete_book, name='deletebook'),
]
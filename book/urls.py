from django.urls import path
from . import views


urlpatterns = [
    path('book', views.book, name='book'),
    path('success', views.book, name='success'),
    path('fail', views.book, name='fail'),
    path('manage_bookings', views.manage_bookings, name='managebookings'),
    path('edit/<book_id>', views.edit_book, name='editbook'),
    path('toggle/<book_id>', views.toggle_book, name='togglebook'),
    path('delete/<book_id>', views.delete_book, name='deletebook'),
]
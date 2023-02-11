from django.urls import path
from . import views


urlpatterns = [
    path('staff', views.staff, name='staff'),
    path('edit/<book_id>', views.edit_book, name='editbook'),
    path('toggle/<book_id>', views.toggle_book, name='togglebook'),
    path('delete/<book_id>', views.delete_book, name='deletebook'),
    path('customer', views.customer, name='customer'),
]
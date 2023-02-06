from django.shortcuts import render
from book.forms import BookForm
from book.models import Book


def mybookings(request):
    return render(request, "mybookings.html")

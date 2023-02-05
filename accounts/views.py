from django.shortcuts import render
from book.forms import BookForm
from book.models import Book


def mybookings(request):
    mybookings = BookForm.all()
    context = {
        'mybookings': mybookings
    }
    return render(request, "mybookings.html", context)

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book
from .forms import BookForm


def Book(request):
    """
    Renders the book page
    """

    return render(
        request,
        "book.html",
        {
            "book_form": BookForm()
        }
    )

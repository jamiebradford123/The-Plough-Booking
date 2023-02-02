from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book
from .forms import BookForm


from django.http import HttpResponseRedirect


def Book(request):
    """
    Renders the book page
    """
    if request.user.is_authenticated:
        form = BookForm(request.POST or None)
        context = {
            "form": form,
        }
    else:
        return HttpResponseRedirect("accounts/login")
    return render(
        request,
        "book.html",
        {
            "book_form": BookForm()
        }
    )

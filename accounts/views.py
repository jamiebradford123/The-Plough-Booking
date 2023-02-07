from django.shortcuts import render, get_object_or_404, redirect
from book.forms import BookForm
from book.models import Book


def mybookings(request):
    booking = Book.objects.order_by('date')
    context = {
            "booking": booking,
     }
    return render(
        request, "mybookings.html", context)

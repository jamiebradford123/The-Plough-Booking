from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.shortcuts import redirect, render, get_object_or_404
from book.models import Book

@login_required(login_url="accounts/login")
def book(request):

    if request.method=="POST":
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book_form.save()
            return render(request,"success.html")

        else:       
            return render(request,"fail.html")
    else:
        book_form = BookForm()
    return render(
        request,
        "book.html",
        {
            "book_form": book_form,
        }
    )

def manage_bookings(request):
    booking = Book.objects.order_by('date')
    context = {
        "booking": booking,
    }
    return render(request, "manage_bookings.html", context)

def manage_bookings(request):
    booking = Book.objects.order_by('date')
    context = {
        "booking": booking,
    }
    return render(request, "manage_bookings.html", context)


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book_form = BookForm(request.POST, instance=book)

        if book_form.is_valid():
            book_form.save()
            return render(request, "bookeditsuccess.html")
    book_form = BookForm(instance=book)
    context = {
        'book_form': book_form
    }
    return render(request, 'edit.html', context)


def toggle_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.approved = not book.approved
    book.save()
    return redirect('managebookings')


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('managebookings')


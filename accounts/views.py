from django.shortcuts import render, get_object_or_404, redirect
from book.forms import BookForm
from book.models import Book


def staff(request):
    return render(request, "staff.html")


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


def manage_events(request):
    events = Event.objects.order_by('date')
    context = {
        "events": events,
    }
    return render(request, "manage_events.html", context)


def customer(request):
    return render(request, "customer.html")
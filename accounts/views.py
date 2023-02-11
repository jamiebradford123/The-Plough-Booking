from django.shortcuts import render, get_object_or_404, redirect
from book.forms import BookForm
from book.models import Book


def staff(request):
    booking = Book.objects.order_by('date')
    context = {
            "booking": booking,
     }
    return render(
        request, "staff.html", context)

def customer(request):
    return render(request, "customer.html")


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method=="POST":
        book_form = BookForm(request.POST, instance=book)

        if book_form.is_valid():
            book_form.save()
            return render(request,"bookeditsuccess.html")
    book_form = BookForm(instance=book)
    context = {
        'book_form': book_form
    }
    
    return render(request, 'edit.html', context)

def toggle_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.approved = not book.approved
    book.save()
    return redirect('staff')

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('staff')
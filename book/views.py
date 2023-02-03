from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Book
from .forms import BookForm
from django.http import HttpResponseRedirect

# This is a function, not a Class so should be lowercase name
def book(request):
    form = BookForm()
    # POST logic
    if request.method == 'POST':
        # If not authorized, redirect them
        if not request.user.is_authenticated:
            return HttpResponseRedirect("accounts/login")
        # otherwise, instantiate a form using POST data
        else:
            form = BookForm(request.POST)
            # If the data is valid, save to the DB
            if form.is_valid():
                form.save()
                return redirect('book')
            else:
                print(form.errors)
    # GET logic
    context = {
        'book_form': form,
    }

    return render(
        request,
        "book.html",
        context
    )
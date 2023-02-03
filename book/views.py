from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.shortcuts import redirect,render

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
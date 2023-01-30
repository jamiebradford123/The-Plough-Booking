from django.shortcuts import render


def Book(request):
    """
    Renders the book page 
    """

    return render(request, "book.html")
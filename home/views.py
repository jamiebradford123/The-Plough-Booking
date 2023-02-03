from django.shortcuts import render


def index(request):
    """
    Renders the home page 
    """

    return render(request, "index.html")

def menu(request):
    """
    Renders the menu page
    """
    return render(request, "menu.html")

def breakfast(request):
    """
    Renders the menu page
    """
    return render(request, "breakfast.html")

def main(request):
    """
    Renders the menu page
    """
    return render(request, "main.html")

def drinks(request):
    """
    Renders the menu page
    """
    return render(request, "drinks.html")
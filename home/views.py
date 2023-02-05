from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def breakfast(request):
    return render(request, "breakfast.html")

def main(request):
    return render(request, "main.html")

def drinks(request):
    return render(request, "drinks.html")
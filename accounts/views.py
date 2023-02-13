from django.shortcuts import render, get_object_or_404, redirect
from book.forms import BookForm
from book.models import Book


def staff(request):
    return render(request, "staff.html")


def manage_events(request):
    events = Event.objects.order_by('date')
    context = {
        "events": events,
    }
    return render(request, "manage_events.html", context)


def customer(request):
    return render(request, "customer.html")
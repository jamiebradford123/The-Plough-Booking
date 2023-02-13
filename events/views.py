from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EventForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('event_date')
    template_name = 'event.html'
    paginate_by = 6


def add_event(request):

    if request.method=="POST":
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            event_form.save()
            return render(request,"event_success.html")

        else:       
            return render(request,"fail.html")
    else:
        event_form = EventForm()
    return render(
        request,
        "add_event.html",
        {
            "event_form": event_form,
        }
    )


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = EventForm(instance=event)
    context = {
        'form': form
    }
    return render(request, 'edit_event.html', context)


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('event')

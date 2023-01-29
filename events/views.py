from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event
from .forms import CommentForm 


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('created_on')
    template_name = 'event.html'
    paginate_by = 6

class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by('created_on')
        interested = False
        if event.interested.filter(id=self.request.user.id).exists():
            intersted = True

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "comments": comments,
                "interested": interested,
                "comment_form": CommentForm(),
            }
        )


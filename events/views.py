from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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
            interested = True

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "comments": comments,
                "commented": False,
                "interested": interested,
                "comment_form": CommentForm(),
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by('created_on')
        interested = False
        if event.interested.filter(id=self.request.user.id).exists():
            interested = True
    
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "comments": comments,
                "commented": True,
                "interested": interested,
                "comment_form": CommentForm(),
            }
        )


class EventInterested(View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.interested.filter(id=request.user.id).exists():
            event.interested.remove(request.user)
        else:
            event.interested.add(request.user)
        
        return HttpResponseRedirect(reverse('event_detail', args=[slug]))



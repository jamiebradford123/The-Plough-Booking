from . import views
from django.urls import path
from events.views import edit_event


urlpatterns = [
    path('event', views.EventList.as_view(), name='event'),
    path('add_event', views.add_event, name='add_event'),
    path('edit_event/<event_id>', edit_event, name="edit_event"),
    path('event_success', views.add_event, name='event_success'),
]
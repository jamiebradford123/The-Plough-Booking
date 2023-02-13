from . import views
from django.urls import path


urlpatterns = [
    path('event', views.EventList.as_view(), name='event'),
    path('add_event', views.add_event, name='add_event'),
    path('event_success', views.add_event, name='event_success'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('interested/<slug:slug>', views.EventInterested.as_view(), name='event_interested'),
]
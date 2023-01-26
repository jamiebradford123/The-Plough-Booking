from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


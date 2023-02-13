from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


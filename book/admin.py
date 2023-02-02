from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('name', 'approved', 'created_on', 'date')
    search_fields = ['name', 'date']
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)

from .models import Comment, Event
from django import forms 
from datetime import date, datetime


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class DateInput(forms.DateInput):
    input_type = "date"

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'slug',
            'event_date',
            'time',
            'content',
            'featured_image',
            'price',
        ]
        widgets = {
            "event_date": DateInput(),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }

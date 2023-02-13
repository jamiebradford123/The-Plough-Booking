from .models import Event
from django import forms 
from datetime import date, datetime


class DateInput(forms.DateInput):
    input_type = "date"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
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

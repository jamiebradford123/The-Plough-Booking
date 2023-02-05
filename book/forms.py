from .models import Book
from django import forms
from datetime import date, datetime


class DateInput(forms.DateInput):
    input_type = "date"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'number_of_guests',
            'date',
            'time',
            'email',
            'requests',
        ]
        widgets = {
            "date": DateInput(),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
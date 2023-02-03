from .models import Book
from django import forms


class DateInput(forms.DateInput):
    """
    A class to register the input_type
    as date
    """
    input_type = "date"

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'number_of_guests',
            'date',
            'email',
            'requests',
        ]
        widgets = {
            "date": DateInput(),
        }
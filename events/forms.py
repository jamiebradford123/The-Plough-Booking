from .models import Event
from django import forms
from django.utils import timezone
# from datetime import date, datetime
# from datetime import date


class DateInput(forms.DateInput):
    input_type = "date"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "event_date",
            "time",
            "content",
            "featured_image",
            "price",
        ]
        widgets = {
            "event_date": DateInput(),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }

    # def clean_date(self):
    #     event_date = self.cleaned_data["event_date"]
    #     if event_date < date.today():
    #         raise forms.ValidationError("The date cannot be in the past!")
    #     return event_date


    def clean_event_date(self):
        date = self.cleaned_data.get('event_date')
        if date and date < timezone.now().date():
            raise forms.ValidationError("Please select a future date.")
        return date
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")

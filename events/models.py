from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator, MinValueValidator
from datetime import date, datetime
from django.core.exceptions import ValidationError
from .validators import validate_date

STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):
    title = models.CharField(max_length=150, unique=True)
    event_date = models.DateField(validators=[validate_date])
    time = models.TimeField(null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField("image", default="placeholder")
    price = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-event_date"]

    def __str__(self):
        return self.title

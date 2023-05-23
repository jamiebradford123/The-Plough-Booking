from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from .validators import validate_date


class Book(models.Model):
    name = models.CharField(max_length=50)
    number_of_guests = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    date = models.DateField(validators=[validate_date])
    time = models.TimeField(null=True)
    email = models.EmailField()
    requests = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.date} for {self.name}"

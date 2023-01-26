from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    event_date = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    interested = models.ManyToManyField(User, related_name='event_interested', blank=True)

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title

    def number_interesed(self):
        return self.interesed.count()

# Taken from CI Blog app tutorial


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

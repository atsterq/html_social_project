from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    contact = models.EmailField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events'
    )
    location = models.CharField(max_length=400)

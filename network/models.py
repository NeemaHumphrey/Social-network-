from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False
    )
    likes = models.ManyToManyField(
        'network.Post',
        related_name='liked_by',
    )

    def is_followed_by(self):
        return self.followed_by.count()


class Post(models.Model):
    content = models.CharField(max_length=126)
    author = models.ForeignKey("network.User", on_delete=models.CASCADE, related_name="posts")
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_created',)
    
   

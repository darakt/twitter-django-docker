from django.db import models
from django.utils import timezone
from users.models import User

class Tweet(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets', null=True)
    # name = models.CharField(max_length=20)
    # profile_img_url = models.CHarField(max_length=200)
    mention = models.ManyToManyField(User, related_name='mentioned_in')


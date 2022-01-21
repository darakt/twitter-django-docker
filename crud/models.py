from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=20)
    profil_img_url = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    followers_count = models.PositiveIntegerField(default=0)
    follow = models.ManyToManyField('self', related_name='follower')
    
    def counts_the_followers(self):
        followers = self.followers.all()
        print(len(followers))

class Tweet(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets', null=True)
    # name = models.CharField(max_length=20)
    # profile_img_url = models.CHarField(max_length=200)
    mention = models.ManyToManyField(User, related_name='mentioned_in')

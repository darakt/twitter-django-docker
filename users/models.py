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


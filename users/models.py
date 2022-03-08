from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    name = models.CharField(max_length=20, validators=[
        RegexValidator(
            regex='^[A-Za-zÀ-ÖØ-öø-ÿ\x27\-\s]{0,255}$',
            message='Username must be alphanumeric',
            code='invalid_username'
            ),
        ])
    password = models.CharField(max_length=200)
    '''
    profil_img_url = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    followers_count = models.PositiveIntegerField(default=0)
    follow = models.ManyToManyField('self', related_name='follower')
    # email = models.EmailField(max_length=200),    
    class meta:
        permissions = [
                ('can_create_a_tweet', 'As a user I can publish a tweet'),
                ('can_read_all_the_tweets','As a user I can read all the tweets'),
                ('can_update_my_tweets', 'As a user I can update my tweets'),
                ('can_delete_my_tweet', 'As a user I can delete my tweet')
                ]
    def counts_the_followers(self):
        followers = self.followers.all()
        print(len(followers))


from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
import json

attributeWhiteListed = [ # we don't want to pass everything to the front so no need to jsonified everything
    'id',
    'username',
    'first_name',
    'last_name',
    'email',
    'is_staff',
    'is_active',
    'date_joined',
    'profil_img_url',
    'description',
    'followers_count'
]

class User(AbstractUser):
    def toJson(self):
        jsonified = {}
        # No idea how to manage permissions => TODO investigate more
        # all_permissions = Permission.objects.filter(content_type__app_label='users', content_type__model='user')
        # for perm in all_permissions:
        #     print(perm)
        # print(self.get_user_permissions());
        for key in self.__dict__.keys():
            if self.__dict__[key] is not None and key in attributeWhiteListed and self.__dict__[key] != '':
                # print('[{}] = {}'.format(key, self.__dict__[key]))
                jsonified[key] = self.__dict__[key]
        return jsonified
    profil_img_url = models.CharField(max_length=200)
    description = models.TextField()
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

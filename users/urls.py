from django.urls import path 

from . import handlers

urlpatterns = [
        path('', handlers.status, name='status'),
        path('create/', handlers.create, name='create'),
        path('get/', handlers.getAUser, name='getAUser'),
        path('update/', handlers.update, name='update'),
        path('delete/', handlers.delete, name='delete'),
    ]

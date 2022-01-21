from django.urls import path

from . import handlers 

urlpatterns = [
        path('', handlers.helloCrud, name='crud'),
]

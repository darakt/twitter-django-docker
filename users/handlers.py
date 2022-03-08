from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from users.models import User
import json

allowed_to_update = ['username'] #TODO: should be an env var

def status(request):
    return HttpResponse('UP')

@csrf_exempt
def create(request): # add mandatory fields (name, ...)
    if request.method == 'POST':
        try:
            # TODO: add test null
            new = User(username = request.POST.get('username'))
            new.save()
            return HttpResponse('a new user was created: id: %s, username: %s' % (new.id, new.username))
        except Exception as err:
            return HttpResponseNotFound(err)
    return HttpResponseNotFound('Try using POST')

def getAUser(request, id = 0): # through ID
    if request.method == 'GET':
        try:
            asked = User.objects.get(id=id)
        except Exception as err:
            return HttpResponseNotFound(err)
        return HttpResponse(asked)
    return HttpResponseNotFound('Try using GET')

@csrf_exempt
def update(request, id=0):
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            # for security purposes
            topics = list(data['toPatch'].keys())
            print(topics)
            for topic in topics:
                if topic not in allowed_to_update:
                    return HttpResponseNotFound('you are trying to update an illegal parameter') # add custom exception class 
        except Exception as err:
            return HttpResponseNotFound(err)
        return HttpResponse('a user was updated')
    return HttpResponseNotFound('Try using PATCH')

@csrf_exempt
def delete(request, id=0):
    if request.method == 'DELETE':
        try:
            User.objects.get(id=id).delete()
            return HttpResponse('a user was deleted')
        except Exception as err:
            return HttpResponseNotFound(err)
    return HttpResponseNotFound('Try using DELETE')


from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from users.models import User
from users.errors import NoValueError
from django.db import IntegrityError
from django.http import JsonResponse
from users.helpers import check_string
import json
import string

allowed_to_update = ['username'] #TODO: should be an env var
# allowed_to_front = ['username', 'first_name', 'last_name', 'email', 'user_permission', 'last_login', 'date_joined', 'profil_img_url', 'description', 'followers_count', 'follow', 'follower'] # TODO: should be an env var

def status(request):
    return HttpResponse('UP')

@csrf_exempt
def create(request): # add mandatory fields (name, ...)
    if request.method == 'POST':
        try:
            email = check_string(request.POST, 'email', string.punctuation.replace('@', '').replace('.', ''))
            username = check_string(request.POST, 'username', string.punctuation)
            first_name = check_string(request.POST, 'first_name', string.punctuation)
            last_name = check_string(request.POST, 'last_name', string.punctuation)
            password = check_string(request.POST, 'password', '') # front should send an hash
            new = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            new.save()
            return JsonResponse(new.toJson())
        except IntegrityError as err:
            print(err.__cause__)
            return HttpResponseNotFound(err.__cause__);
        except Exception as err:
            print(type(err))
            print(err)
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

from django.http import HttpResponse, HttpResponseNotFound

def status(request):
    return HttpResponse('UP')

def create(request):
    if request.method == 'POST':
        return HttpResponse('a user was created')
    return HttpResponseNotFound('Try using POST')

def getAUser(request):
    if request.method == 'GET':
        return HttpResponse('a user')
    return HttpResponseNotFound('Try using GET')

def update(request):
    if request.method == 'PATCH':
        return HttpResponse('a user was updated')
    return HttpResponseNotFound('Try using PATCH')

def delete(request):
    if request.method == 'DELETE':
        return HttpResponse('a user was deleted')
    return HttpResponseNotFound('Try using DELETE')


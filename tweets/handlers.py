from django.http import HttpResponse, HttpResponseNotFound

def status(request):
    return HttpResponse('UP')

def create(request):
    if request.method == 'POST':
        return HttpResponse('a tweet was created')
    return HttpResponseNotFound('Try using POST')

def getATweet(request):
    if request.method == 'GET':
        return HttpResponse('a tweet')
    return HttpResponseNotFound('Try using GET')

def update(request):
    if request.method == 'PATCH':
        return HttpResponse('a tweet was updated')
    return HttpResponseNotFound('Try using PATCH')

def delete(request):
    if request.method == 'DELETE':
        return HttpResponse('a tweet was deleted')
    return HttpResponseNotFound('Try using DELETE')


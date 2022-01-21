from django.http import HttpResponse

def helloCrud(request):
    return HttpResponse("Hello CRUD!")


from django.http import HttpResponse

def home(request):
    return HttpResponse("HOME 2")

def contact(request):
    return HttpResponse("CONTACT")

def about(request):
    return HttpResponse("ABOUT")



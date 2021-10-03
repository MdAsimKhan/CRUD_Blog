from django.http import HttpResponse

def Authors(request):
    return HttpResponse('This page shows list of authors wiht their social media links')

def About(request):
    return HttpResponse('This is the About page')

def Contact(request):
    return HttpResponse('This is the Contact page')
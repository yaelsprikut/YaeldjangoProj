from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>This is the music homepage</h2>")
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello world James")

# Create your views here.

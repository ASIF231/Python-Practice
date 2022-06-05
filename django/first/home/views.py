from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<b>This is HomePage<b>")

def about(request):
    return HttpResponse("yhis is home page")
    
def services(request):
    return HttpResponse("service page")

def contact(request):
    return HttpResponse("contact page")

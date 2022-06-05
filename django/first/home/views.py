from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': "TEST VARIABLE"
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("yhis is home page")
    
def services(request):
    return HttpResponse("service page")

def contact(request):
    return HttpResponse("contact page")

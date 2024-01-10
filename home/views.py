from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'contact.html')
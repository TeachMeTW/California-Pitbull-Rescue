from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Website/home.html')

def about(request):
    return render(request, 'Website/about.html')

def adoptapitbull(request):
    return render(request, 'Website/adoptapitbull.html')

def adopt(request):
    return render(request, 'Website/adopt.html')

def resources(request):
    return render(request, 'Website/resources.html')

def foster(request):
    return render(request, 'Website/foster.html')

def contact(request):
    return render(request, 'Website/contact.html')

def events(request):
    return render(request, 'Website/events.html')

def volunteer(request):
    return render(request, 'Website/volunteer.html')

def store(request):
    return render(request, 'Website/store.html')

def alumni(request):
    return render(request, 'Website/alumni.html')

def donate(request):
    return render(request, 'Website/donate.html')

def adoptionprocess(request):
    return render(request, 'Website/adoptionprocess.html')

def training(request):
    return render(request, 'Website/training.html')

def pitbullfaq(request):
    return render(request, 'Website/pitbullfaq.html')

from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)

def appointment(request):
    context = {}
    return render(request, 'base/appointment.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)
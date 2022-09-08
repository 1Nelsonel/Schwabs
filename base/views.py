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

def service(request):
    context = {}
    return render(request, 'base/service.html', context)

def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)

def product(request):
    context = {}
    return render(request, 'base/product.html', context)
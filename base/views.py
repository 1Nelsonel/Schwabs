from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from base.models import Appointment, Contact, Blog, Comment, Service

# Create your views here.
def home(request):
    services = Service.objects.all()
    context = {'services': services}
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
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'base/service.html', context)

def serviceSingle(request, pk):
    service = Service.objects.get(id=pk)

    if request.method == 'POST':
        contact = Contact.objects.create(
            user=request.POST.get('user'),
            email=request.POST.get('email'),
            tel=request.POST.get('tel'),
            subject=request.POST.get('subject'),
            body=request.POST.get('body'),
        )

        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('serviceSingle', pk=service.id)

    context = {'service': service}
    return render(request, 'base/serviceSingle.html', context)

def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)

def product(request):
    context = {}
    return render(request, 'base/product.html', context)
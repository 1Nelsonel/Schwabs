from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from base.models import Appointment, Contact, Blog, Comment, Service, Product, Team

# Create your views here.
def home(request):
    services = Service.objects.all()
    teams = Team.objects.all()

    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)

    page_number = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)

    products = Product.objects.all()
    paginator = Paginator(products, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'services': services, 'blogs': blogs, 'page_obj': page_obj, 'blog_obj': blog_obj, 'teams': teams}
    return render(request, 'base/home.html', context)

def contact(request):
    if request.method == 'POST':
        contact = Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            body=request.POST.get('body'),
        )
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('contact')
    context = {}
    return render(request, 'base/contact.html', context)

def appointment(request):
    services = Service.objects.all()

    if request.method == 'POST':
        appointment = Appointment.objects.create(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            date=request.POST.get('date'),
            service=request.POST.get('service'),
            body=request.POST.get('body'),
        )
        messages.success(request, 'Your made an appointmenr. Thank you!')
        return redirect('appointment')
    context = {'services': services}
    return render(request, 'base/appointment.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def service(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'base/service.html', context)

def serviceSingle(request, slug):
    service = Service.objects.get(slug=slug)

    if request.method == 'POST':
        contact = Contact.objects.create(
            user=request.POST.get('user'),
            email=request.POST.get('email'),
            tel=request.POST.get('tel'),
            subject=request.POST.get('subject'),
            body=request.POST.get('body'),
        )

        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('serviceSingle', slug=service.slug)

    context = {'service': service}
    return render(request, 'base/serviceSingle.html', context)

def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    comments = Comment.objects.all()
    services = Service.objects.all()

    context = {'blogs': blogs, 'services': services, 'comments': comments, 'page_obj': page_obj}
    return render(request, 'base/blog.html', context)

def blogSingle(request, slug):
    blog = Blog.objects.get(slug=slug)
    services = Service.objects.all()
    comments = blog.comment_set.all()
    blogs = Blog.objects.all()
    

    if request.method == 'POST':
        comment = Comment.objects.create(
            blog=blog,
            user=request.POST.get('user'),
            email=request.POST.get('email'),
            body=request.POST.get('body'),
        )

        messages.success(request, 'Comment sent')
        return redirect('blogSingle', slug=blog.slug)

    context = {'blog': blog, 'services': services, 'comments': comments, 'blogs': blogs}
    return render(request, 'base/blogSingle.html', context)

def product(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': products, 'page_obj': page_obj}
    return render(request, 'base/product.html', context)
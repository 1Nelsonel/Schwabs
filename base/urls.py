from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('service/', views.service, name='service'),
    path('product/', views.product, name='product')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

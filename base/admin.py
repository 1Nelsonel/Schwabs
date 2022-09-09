from django.contrib import admin
from . models import Appointment, Blog, Comment, Contact, Service

# Register your models here.

admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Appointment)
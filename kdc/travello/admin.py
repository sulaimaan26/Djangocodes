from django.contrib import admin
from . models import Destination,Menus,Testimonials,News

# Register your models here.
admin.site.register(Menus)
admin.site.register(Destination)
admin.site.register(Testimonials)
admin.site.register(News)

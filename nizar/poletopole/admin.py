from django.contrib import admin
from . models import Header,HomepageBanner,HomepageDestination,HomepageOffersection,HomepageVideo,HomepagePopularDestionation,HomepageSpecialOffers
# Register your models here.
admin.site.site_header = "My Product Inventory "
class Homeadmin(admin.ModelAdmin):
    list_display = ['sku', 'title', 'unit', 'unitCost', 'quantity']
    fields = [('family','location'),('sku','barcode'), ('title','description'),('unit', 'unitCost'), ('quantity','minQuantity')]

admin.site.register(Header)
admin.site.register(HomepageBanner)
admin.site.register(HomepageDestination)
admin.site.register(HomepageOffersection)
admin.site.register(HomepageVideo)
admin.site.register(HomepagePopularDestionation)
admin.site.register(HomepageSpecialOffers)


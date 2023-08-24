from django.contrib import admin

from .models import CompanyName,DeliveryChallanFor,ShippingTo 
admin.site.register(CompanyName)
admin.site.register(DeliveryChallanFor)
admin.site.register(ShippingTo )

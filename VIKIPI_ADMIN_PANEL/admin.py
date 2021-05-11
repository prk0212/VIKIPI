from django.contrib import admin
from .models import *
admin.site.site_url="http://127.0.0.1:8000/vikipi_admin/home/"

class retailerAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','created_at','status','email')
    list_display_links=('firstname',)
    list_editable=('email','status',)
    list_per_page=5
    list_filter=('created_at',)
    search_fields=('firstname',)

# Register your models here.
admin.site.register(retailer)
admin.site.register(shop_details)
admin.site.register(employee)
admin.site.register(category)
admin.site.register(product)
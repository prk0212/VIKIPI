from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(customer_registration)
admin.site.register(user)
admin.site.register(customer)
admin.site.register(customer_FeedBack)
admin.site.register(wishlist)
admin.site.register(product_review)
admin.site.register(product_cart)
admin.site.register(Transaction)
from django.db import models
from VIKIPI_ADMIN_PANEL.models import * 
# Create your models here.

class user(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=4567)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
class customer(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    firstname=models.CharField(max_length = 30,blank=False)
    lastname=models.CharField(max_length = 30,blank=False)
    phnumber=models.BigIntegerField(max_length=10,null=True)
    gender=models.CharField(max_length=10)
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField(max_length=10,blank=True,null=True)
    address=models.CharField(max_length=100)
    view=models.BooleanField(default=False)
class customer_FeedBack(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    overall_experience=models.CharField(max_length=20)
    timely_response=models.CharField(max_length=30)
    our_support=models.CharField(max_length=30)
    overall_setisfaction=models.CharField(max_length=30) 
    view=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
class wishlist(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    added=models.DateTimeField(auto_now_add=True,blank=False)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)


class product_review(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    review=models.CharField(max_length=500)
    view=models.BooleanField(default=False)
class product_cart(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=3,blank=False,default=1)
    date_of_added=models.DateTimeField(auto_now_add=True,blank=False)
    status = models.CharField(max_length=20,default="pending")

    def total_price(self):
        return int(self.quantity * self.product_id.product_price)
class Transaction(models.Model):
    made_by = models.ForeignKey(user, related_name='transactions',on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_product_list = models.TextField(max_length=255, null=True, blank=True)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)
    date_of_order=models.DateTimeField(auto_now_add=True,blank=False)
    status=models.CharField(max_length=50,default='Pending')
    ord_deliver_otp=models.IntegerField(default=7878)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)


    


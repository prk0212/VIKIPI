from django.db import models

# Create your models here.
class retailer(models.Model):
    firstname=models.CharField(max_length=30,blank=False)
    lastname=models.CharField(max_length = 30,blank=False)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20,blank=False)
    phnumber=models.IntegerField(max_length=10,blank=True,null=True)
    gender=models.CharField(max_length=10)
    status=models.CharField(default='Pending',max_length=10)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    profile_pic=models.FileField(upload_to='images/',default='AdminLTELogo.png')
    home_country=models.CharField(max_length=30)
    home_state=models.CharField(max_length=50)
    home_city=models.CharField(max_length=50)
    home_pincode=models.IntegerField(max_length=10,blank=True,null=True)
    home_address=models.CharField(max_length=100)
    otp=models.IntegerField(max_length=8,default=7894) 
    otp_status=models.CharField(max_length=50,default='Pending')
    view=models.BooleanField(default=False) 
    def __str__(self):
        return self.firstname
class shop_details(models.Model):
    owner_id=models.ForeignKey(retailer,on_delete=models.CASCADE)
    shop_name=models.CharField(max_length=200)
    shop_type=models.CharField(max_length=200)
    shop_country=models.CharField(max_length=30)
    shop_state=models.CharField(max_length=50)
    shop_city=models.CharField(max_length=50)
    shop_pincode=models.IntegerField(max_length=10,blank=True,null=True)
    shop_address=models.CharField(max_length=100)
    view=models.BooleanField(default=False)
    owner_id_proof=models.FileField(upload_to='images/')
    elc_bill=models.FileField(upload_to='images/')
    def __str__(self):
        return self.shop_name
class category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class product(models.Model):
    owner_id=models.ForeignKey(retailer,on_delete=models.CASCADE)
    shop_id=models.ForeignKey(shop_details,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_category=models.ForeignKey(category,on_delete=models.CASCADE)
    product_price=models.IntegerField(max_length=6)
    product_quantity=models.CharField(max_length=50)
    product_description=models.CharField(max_length=4000)
    product_image=models.FileField(upload_to='images/',default='AdminLTELogo.png')
    view=models.BooleanField(default=False)
    def __str__(self):
        return self.product_name
class employee(models.Model):
    firstname=models.CharField(max_length=30,blank=False)
    lastname=models.CharField(max_length = 30,blank=False)
    email=models.EmailField(unique=True)
    phnumber=models.IntegerField(max_length=10)
    gender=models.CharField(max_length=10)
    qualification=models.CharField(max_length=20,default='select')
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField(max_length=10,blank=True,null=True)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.firstname
class product_images(models.Model):
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    sub_image=models.FileField(upload_to='images/')
class retailer_FeedBack(models.Model):
    retailer_id=models.ForeignKey(retailer,on_delete=models.CASCADE)
    review=models.CharField(max_length=1000)
    overall_experience=models.CharField(max_length=20)
    timely_response=models.CharField(max_length=30)
    our_support=models.CharField(max_length=30)
    overall_setisfaction=models.CharField(max_length=30)
    suggestion=models.CharField(max_length=1000,blank=True)
    view=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)


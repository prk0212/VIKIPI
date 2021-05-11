from django.shortcuts import render
from .models import *
from .utils import *
from VIKIPI_ADMIN_PANEL.views import *
import random
from django.db.models import Count
import datetime
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

from VIKIPI_ADMIN_PANEL import *    
def abc(request):
    if 'email' in request.session:
        print("----------------------------------------------------------",request.session['email'])
        other_pro=product.objects.all()
        six_pro=other_pro[:6]
        eight_pro=other_pro[6:14]
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'uid':uid,'cid':cid,'six_pro':six_pro,'eight_pro':eight_pro,'catid':catid,'sid':sid,'cart_id':cart_id})   
    else:
        sid=shop_details.objects.all()
        catid=category.objects.all()
        other_pro=product.objects.all()
        six_pro=other_pro[:6]
        eight_pro=other_pro[6:14]
        return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'catid':catid,'sid':sid,'six_pro':six_pro,'eight_pro':eight_pro})

def login(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        other_pro=product.objects.all()
        six_pro=other_pro[:6]
        eight_pro=other_pro[6:14]
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'six_pro':six_pro,'eight_pro':eight_pro})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def register(request):
    return render(request,'VIKIPI_CUSTOMER_PANEL/register.html')

def register_user(request):
        if 'firstname' in request.POST:
            u_fname=request.POST['firstname']
            u_lname=request.POST['lastname']
            u_email=request.POST['email']
            u_password=request.POST['password']
            uid=user.objects.create(email=u_email,password=u_password)
            if uid:
                cid=customer.objects.create(user_id=uid,firstname=u_fname,lastname=u_lname)
                if cid:
                    sendmail("Confirmation mail","mail_template",u_email,{'name':u_fname})
                    return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')
                else:
                    emsg="Registration Fail"
                    return render(request,'VIKIPI_CUSTOMER_PANEL/register.html',{'emsg':emsg})
            else:
                emsg="Registration Fail"
                return render(request,'VIKIPI_CUSTOMER_PANEL/register.html',{'emsg':emsg})
        else:
            return render(request,'VIKIPI_CUSTOMER_PANEL/register.html')

def login_user(request):
    try:    
        if 'email' not in request.session:
            if request.POST['email']=='' and request.POST['loginpassword']=='':
                return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')
            elif request.POST['email']!='' and request.POST['loginpassword']!='':
                u_email = request.POST['email']
                u_pass = request.POST['loginpassword']
                fuid=user.objects.filter(email=u_email)
                if fuid:
                    uid=user.objects.get(email=request.POST['email'])
                    if uid.password==u_pass:
                        request.session['email']=uid.email
                        cid=customer.objects.get(user_id=uid.id)
                        request.session['firstname']=cid.firstname
                        request.session['lastname']=cid.lastname
                        other_pro=product.objects.all()
                        six_pro=other_pro[:6]
                        eight_pro=other_pro[6:14]
                        catid=category.objects.all()
                        sid=shop_details.objects.all()
                        cart_id=product_cart.objects.filter(customer_id=cid).count()
                        cart_id_get=product_cart.objects.filter(customer_id=cid)
                        return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'six_pro':six_pro,'eight_pro':eight_pro})
                    else:
                        emsg="Invalid password"
                        print('---------------------------------------------------',emsg)
                        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html',{'emsg':emsg})
                else:
                    e_msg="Please Enter valid email id"
                    return render(request,'VIKIPI_CUSTOMER_PANEL/login.html',{'emsg':e_msg})
            
            else:
                return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')
        elif 'email' in request.session:
            uid=user.objects.get(email=request.session['email'])
            cid=customer.objects.get(user_id=uid)
            catid=category.objects.all()
            sid=shop_details.objects.all()
            other_pro=product.objects.all()
            six_pro=other_pro[:6]
            eight_pro=other_pro[6:14]
            cart_id=product_cart.objects.filter(customer_id=cid).count()
            cart_id_get=product_cart.objects.filter(customer_id=cid)
            return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'six_pro':six_pro,'eight_pro':eight_pro})
        else:
            uid=user.objects.get(email=request.session['email'])
            cid=customer.objects.get(user_id=uid)
            catid=category.objects.all()
            sid=shop_details.objects.all()
            other_pro=product.objects.all()
            six_pro=other_pro[:6]
            eight_pro=other_pro[6:14]
            cart_id=product_cart.objects.filter(customer_id=cid).count()
            cart_id_get=product_cart.objects.filter(customer_id=cid)
            return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'six_pro':six_pro,'eight_pro':eight_pro})
    except: 
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')
    
def logout(request):
    
    del request.session['email']
    if 'uid' in request.session:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def forgot_password(request):
    return render(request,"VIKIPI_CUSTOMER_PANEL/forgotpassword.html")

def forgot_password_user(request):
    
        email=request.POST['email']
        uid = user.objects.get(email=email)
        if uid:
                cid=customer.objects.get(user_id=uid)
                otp=random.randint(111111,999999)
                uid.otp = otp
                uid.save()
                context={
                    'firstname':cid.firstname,
                    'otp':uid.otp,
                }
                sendmail_user("Reset Password","otp_temp",email,{'context':context})
                return render(request,"VIKIPI_CUSTOMER_PANEL/forgotpasswordotp.html",{'email':email})
        else:
            return render(request,"VIKIPI_CUSTOMER_PANEL/forgotpassword.html")
    
def reset_password(request):
        if 'email' in request.POST:
            return render(request,"VIKIPI_CUSTOMER_PANEL/forgotpasswordotp.html")
        else:
            return render(request,"VIKIPI_CUSTOMER_PANEL/login.html")

def reset_password_user(request):
        if 'chkemail' in request.POST:
            email=request.POST['chkemail']
            otp=request.POST['otp']
            password1=request.POST['password']
            password2=request.POST['repassword']
            uid=user.objects.get(email=email)
            if uid:
                if otp==str(uid.otp):
                    if password1==password2:
                        uid.password=password1
                        uid.save()
                        return render(request,"VIKIPI_CUSTOMER_PANEL/login.html")
                    

def edit_profile(request):
    try:
        if 'email' in request.session:
            uid=user.objects.get(email=request.session['email'])
            cid=customer.objects.get(user_id=uid)
            catid=category.objects.all()
            sid=shop_details.objects.all()
            cart_id=product_cart.objects.filter(customer_id=cid).count()
            cart_id_get=product_cart.objects.filter(customer_id=cid)
            return render(request,"VIKIPI_CUSTOMER_PANEL/edit_profile.html",{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid, 'catid':catid})
        else:
            catid=category.objects.all()
            sid=shop_details.objects.all()
            other_pro=product.objects.all()
            six_pro=other_pro[:6]
            eight_pro=other_pro[6:14]
            cart_id=product_cart.objects.filter(customer_id=cid).count()
            cart_id_get=product_cart.objects.filter(customer_id=cid)
            return render(request,"VIKIPI_CUSTOMER_PANEL/index.html",{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'catid':catid,'six_pro':six_pro,'eight_pro':eight_pro})
    except:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/edit_profile.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'uid':uid,'cid':cid, 'catid':catid,'sid':sid})

def edit_profile_user(request):
    try :
        phonenumber=request.POST['phonenumber']
        gender=request.POST['gender']
        country=request.POST['country']
        state=request.POST['state']
        address=request.POST['address']
        city=request.POST['city']
        pincode=request.POST['pincode']
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        if uid: 
            cid.phnumber=phonenumber
            cid.gender=gender
            cid.country=country
            cid.state=state
            cid.address=address
            cid.city=city
            cid.pincode=pincode
            cid.save()
            catid=category.objects.all()
            other_pro=product.objects.all()
            six_pro=other_pro[:6]
            eight_pro=other_pro[6:14]
            return render(request,"VIKIPI_CUSTOMER_PANEL/index.html",{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'six_pro':six_pro,'eight_pro':eight_pro})
    except:
        return render(request,'VIKIPI_CUSTOMER_PANEL/edit_profile.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'uid':uid,'cid':cid,'catid':catid})

def add_feedback(request):
    uid=user.objects.get(email=request.session['email'])
    cid=customer.objects.get(user_id=uid)
    return render(request,'VIKIPI_CUSTOMER_PANEL/feedback.html',{'cid':cid,'uid':uid})

def add_feedback_user(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        overall_experience=request.POST['overall_experience']
        overall_setisfaction=request.POST['overall_setisfaction']
        our_support=request.POST['our_support']
        timely_response=request.POST['timely_response']
        cus_feedback=customer_FeedBack.objects.create(customer_id=cid,overall_experience=overall_experience,overall_setisfaction=overall_setisfaction,our_support=our_support,timely_response=timely_response)
        catid=category.objects.all()
        other_pro=product.objects.all()
        six_pro=other_pro[:6]
        eight_pro=other_pro[6:14]
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'six_pro':six_pro,'eight_pro':eight_pro})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def view_product_by_category(request,pk):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        selected_catid=category.objects.get(id=pk)
        pid=product.objects.filter(product_category=pk)
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        
        return render(request,'VIKIPI_CUSTOMER_PANEL/view-product-by-category.html',{'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid':pid,'selected_catid':selected_catid})
    else:
        catid=category.objects.all()
        selected_catid=category.objects.get(id=pk)
        pid=product.objects.filter(product_category=pk)
        sid=shop_details.objects.all()
        return render(request,'VIKIPI_CUSTOMER_PANEL/view-product-by-category.html',{'sid':sid,'catid':catid,'pid':pid,'selected_catid':selected_catid})

def add_to_wishlist(request,pk):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        pid1=product.objects.get(id=pk)
        selected_catid=pid1.product_category
        wishlist_check=wishlist.objects.filter(customer_id=cid)
        pid=product.objects.filter(product_category=selected_catid)
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        var=[]
        if not wishlist_check:
            wlid=wishlist.objects.create(customer_id=cid,product_id=pid1)
            return render(request,'VIKIPI_CUSTOMER_PANEL/view-product-by-category.html',{'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid':pid,'selected_catid':selected_catid})
        else:
            for i in wishlist_check:
                var.append(i.product_id.id)
            if pk in var:
                msg="Item already added to wishlist"
                return render(request,'VIKIPI_CUSTOMER_PANEL/view-product-by-category.html',{'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid':pid,'selected_catid':selected_catid,'msg':msg})
            else:
                wlid=wishlist.objects.create(customer_id=cid,product_id=pid1)
                return render(request,'VIKIPI_CUSTOMER_PANEL/view-product-by-category.html',{'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid':pid,'selected_catid':selected_catid})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def view_wishlist(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        wlid=wishlist.objects.filter(customer_id=cid).prefetch_related('product_id')
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/wishlist.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'wlid':wlid})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def view_product(request,pk):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        pid=product.objects.get(id=pk)
        selected_catid=pid.product_category
        pimg=product_images.objects.filter(product_id=pid)
        other_product=product.objects.all()[:3]
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        return render(request,'VIKIPI_CUSTOMER_PANEL/view_product.html',{'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid':pid,'pimg':pimg,'other_product':other_product})
    else:
        catid=category.objects.all()
        pid=product.objects.get(id=pk)
        selected_catid=pid.product_category
        pimg=product_images.objects.filter(product_id=pid)
        other_product=product.objects.all()[:3]
        sid=shop_details.objects.all()
        return render(request,'VIKIPI_CUSTOMER_PANEL/view_product.html',{'sid':sid,'catid':catid,'pid':pid,'pimg':pimg,'other_product':other_product})

def product_feedback(request,pk):
    if 'email' in request.session:
        comment = request.POST['comment']
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        pid=product.objects.get(id=pk)
        catid=category.objects.all()
        pimg=product_images.objects.filter(product_id=pid)
        rev_id=product_review.objects.create(customer_id=cid,product_id=pid,review=comment)
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/view_product.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid':pid,'pimg':pimg})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def shopping_cart(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        pid_cart=product_cart.objects.filter(customer_id=cid)
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        price_list=[]
        # n1=[]
        for i in pid_cart:
            price_list.append(i.product_id.product_price)
            # n1.append(i.total_price)
        total_price=sum(price_list)
        
        net_list = [] 
        for i in pid_cart:
            net_list.append(i.quantity * i.product_id.product_price)
        
        netamount = sum(net_list)
        print("-->netamount ",netamount)

        product_list = [] 
        
        for i in pid_cart:
            product_list.append(i.product_id.id)
            print("-------------------------------------------------------------",product_list)
        print("---->>>user",uid.email,"----> product cart list = ",product_list)

        # print("n1",n1)
        # n_total = sum(n1)
        print("------>total price ",total_price)
        return render(request,'VIKIPI_CUSTOMER_PANEL/shoppingcart.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid_cart':pid_cart,'total':total_price,'netamount':netamount,'product_list':product_list})
    else :
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def product_add_to_cart(request,pk):
    if 'email' in request.session:
        pid=product.objects.get(id=pk)
        uid=user.objects.get(email=request.session['email'])
        catid=category.objects.all()
        cid=customer.objects.get(user_id=uid)
        pimg=product_images.objects.filter(product_id=pid)
        pid_cart=product_cart.objects.filter(customer_id=cid)
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
       
        other_pro=product.objects.all()
        six_pro=other_pro[:6]
        eight_pro=other_pro[6:14]
        var=[]
        if not pid_cart:
            print("--------------------------------------------------------",pid_cart)
            p_cart=product_cart.objects.create(customer_id=cid,product_id=pid)
            return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'pid_cart':pid_cart,'six_pro':six_pro,'eight_pro':eight_pro})
        else:
            for i in pid_cart:
                print("--------------------------------------------------------",i)
                var.append(i.product_id.id)
            if pk in var:
                msg="Product is already added to cart"
                return render(request,'VIKIPI_CUSTOMER_PANEL/view_product.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid':pid,'pimg':pimg,'msg':msg})
            else:
                p_cart=product_cart.objects.create(customer_id=cid,product_id=pid)
                return render(request,'VIKIPI_CUSTOMER_PANEL/index.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'pid_cart':pid_cart,'six_pro':six_pro,'eight_pro':eight_pro})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def cart_product_remove(request,pk):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        pid=product.objects.get(id=pk)
        pid_cart=product_cart.objects.get(product_id=pid,customer_id=cid)
        pid_cart.delete()
        pid_cart=product_cart.objects.filter(customer_id=cid)
        catid=category.objects.all()
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/shoppingcart.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'uid':uid,'cid':cid,'catid':catid,'pid_cart':pid_cart})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def cart_qty_inc(request,pk):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        pid=product.objects.get(id=pk)
        pid_cart=product_cart.objects.get(product_id=pid,customer_id=cid)
        pid_cart=product_cart.objects.filter(customer_id=cid)
        catid=category.objects.all() 
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/shoppingcart.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'uid':uid,'cid':cid,'catid':catid,'pid_cart':pid_cart})   

def get_more_tables(request):
    increment = int(request.GET['append_increment'])
    increment_to = increment + 10
    uid=user.objects.get(email=request.session['email'])
    cid=customer.objects.get(user_id=uid)
    pid_cart = product_cart.objects.filter(customer_id=cid).order_by('-id')[increment:increment_to]
    cart_id=product_cart.objects.filter(customer_id=cid).count()
    cart_id_get=product_cart.objects.filter(customer_id=cid)
    return render(request, 'get_more_tables.html', {'cart_id_get':cart_id_get,'cart_id':cart_id,'pid_cart': pid_cart})

def checkout_page(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        total=0
        for i in cart_id_get:
            total+=i.product_id.product_price
        sid=shop_details.objects.all()
        return render(request,'VIKIPI_CUSTOMER_PANEL/checkout.html',{'uid':uid,'sid':sid,'cid':cid,'cart_id':cart_id,'cart_id_get':cart_id_get,'total':total})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def checkout_user(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        lst_cart = []
        rtl_id = []
        total_amount = 0
        if request.POST['firstname']!='' and request.POST['lastname']!='' and request.POST['country']!='' and request.POST['state']!='' and request.POST['city']!='' and request.POST['zip']!='' and request.POST['address']!='':
            cid.country=request.POST['country']
            cid.state=request.POST['state']
            cidcity=request.POST['state']
            cid.pincode=request.POST['zip']
            cid.address=request.POST['address']
            cid.save()
            year=datetime.datetime.now().year
            day=datetime.datetime.now().day
            month=datetime.datetime.now().month
            name=cid.firstname[:4].upper()
            rndm_no=random.randint(111111,999999)
            sid=shop_details.objects.all()
            catid=category.objects.all()
            cart_id=product_cart.objects.filter(customer_id=cid).count()
            cart_id_get=product_cart.objects.filter(customer_id=cid)
            order_id="VKPORD"+str(year)+str(day)+str(month)+name+str(rndm_no)
            cart_details=[]
            total=0
            if cart_id!=0:
                for i in cart_id_get:
                    order_entry=order_details.objects.create(order_id=order_id,customer_id=cid,retailer_id=i.product_id.owner_id,product_id=i.product_id,total_amount=i.product_id.product_price)
                    total+=i.product_id.product_price
            else:
                pass
            

            return render(request,'VIKIPI_CUSTOMER_PANEL/payment.html',{'order_id':order_id,'email':request.session['email'],'cart_id_get':cart_id_get,'cart_id':cart_id,'sid':sid,'cid':cid,'uid':uid,'catid':catid,'total':total})    
        else:
           return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')
           
def payment(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        sid=shop_details.objects.all()
        catid=category.objects.all()
        email=request.session['email']
        return render(request,'VIKIPI_CUSTOMER_PANEL/payment.html',{'email':email,'sid':sid,'cid':cid,'uid':uid,'catid':catid,'cart_id':cart_id,'cart_id_get':cart_id_get})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')

def view_product_by_shop(request,pk):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        sid=shop_details.objects.all()
        selected_sid=shop_details.objects.get(id=pk)
        pid=product.objects.filter(shop_id=pk)
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/view-product-by-shop.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'uid':uid,'cid':cid,'catid':catid,'sid':sid,'pid':pid})
    else:
        catid=category.objects.all()
        sid=shop_details.objects.all()
        selected_sid=shop_details.objects.get(id=pk)
        pid=product.objects.filter(shop_id=pk)
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        cart_id_get=product_cart.objects.filter(customer_id=cid)
        return render(request,'VIKIPI_CUSTOMER_PANEL/view-product-by-shop.html',{'cart_id_get':cart_id_get,'cart_id':cart_id,'catid':catid,'sid':sid,'pid':pid})
def view_all_products(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        sid=shop_details.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        pid_all=product.objects.all()
        return render(request,'VIKIPI_CUSTOMER_PANEL/view-all-pro.html',{'uid':uid,'cid':cid,'catid':catid,'sid':sid,'cart_id':cart_id,'pid_all':pid_all})
    else:
        catid=category.objects.all()
        sid=shop_details.objects.all()
        pid_all=product.objects.all()
        return render(request,'VIKIPI_CUSTOMER_PANEL/view-all-pro.html',{'catid':catid,'sid':sid,'pid_all':pid_all})

def search(request):
    item=request.POST['item_product']
    all_products=product.objects.all()
    sid=shop_details.objects.all()
    catid=category.objects.all()
    all_prod=[]
    for i in all_products:
        if item.lower() in i.product_description.lower() or  item.lower() in i.product_category.name.lower() or item.lower() in i.product_name.lower():
            all_prod.append(i)
    return render(request,'VIKIPI_CUSTOMER_PANEL/search_product.html',{'catid':catid,'sid':sid,'all_prod':all_prod})
def order_list(request):
    if 'email' in request.session:
        uid=user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        ford_id=Transaction.objects.filter(made_by=cid.id)
        print("------------------------------------",ford_id)
        catid=category.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()
        order_id_dict={}
        product_list=[]
        if ford_id:
            for i in ford_id:
                ord_id=Transaction.objects.get(id=i.id)
                product_list.clear() 
                for j in i.order_product_list:
                    
                    if j.isnumeric():
                        pid=product.objects.get(id=j)
                        product_list.append(pid.id)
                        order_id_dict[i.order_id]=product_list
            print("------------------------------------",order_id_dict)
        return render(request,'VIKIPI_CUSTOMER_PANEL/order_details.html',{'order_id_dict':order_id_dict,'uid':uid,'cid':cid,'catid':catid,'cart_id':cart_id})

def initiate_payment(request):
    if 'email' in request.session:
        uid = user.objects.get(email=request.session['email'])
        cid=customer.objects.get(user_id=uid)
        catid=category.objects.all()
        cart_id=product_cart.objects.filter(customer_id=cid).count()

        productlist = request.POST['productlist']
        totalprice = request.POST['totalprice']
        if cid.address:
            transaction = Transaction.objects.create(made_by=uid, amount=totalprice,order_product_list=productlist)
            transaction.save()
            merchant_key = settings.PAYTM_SECRET_KEY
            params = (
                ('MID', settings.PAYTM_MERCHANT_ID),
                ('ORDER_ID', str(transaction.order_id)),
                ('CUST_ID', str(transaction.made_by.email)),
                ('TXN_AMOUNT', str(transaction.amount)),
                ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
                ('WEBSITE', settings.PAYTM_WEBSITE),
                # ('EMAIL', request.user.email),
                # ('MOBILE_N0', '9911223388'),
                ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
                ('CALLBACK_URL', 'http://127.0.0.1:8000/vikipi_shop_hub/callback/'),
                # ('PAYMENT_MODE_ONLY', 'NO'),
            )

            paytm_params = dict(params)
            checksum = generate_checksum(paytm_params, merchant_key)
            
            transaction.checksum = checksum
            transaction.save()

            paytm_params['CHECKSUMHASH'] = checksum
            print('SENT: ', checksum)
            
            
            return render(request, 'VIKIPI_CUSTOMER_PANEL/redirect.html', context=paytm_params)
        else:
            msg="Please provide delivery address. "
            return render(request,'VIKIPI_CUSTOMER_PANEL/edit_profile.html',{'msg':msg,'cart_id':cart_id,'uid':uid,'cid':cid,'catid':catid})
    else:
        return render(request,'VIKIPI_CUSTOMER_PANEL/login.html')
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        paytm_checksum = ''
        print(request.body)
        print(request.POST)
        received_data = dict(request.POST)
        print(received_data)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        
        orderid = received_data['ORDERID']
        s = str(orderid)
        n= s[2:]
        final = n[:-2]
        tid = Transaction.objects.get(order_id=final)
        for i in tid.order_product_list:
            # i.status = "Payment done"
            print("-----------",i)
        tid.save()  
        tid.status="Paied";
        
        if tid.status=="Paied":
            uid=tid.made_by
            cid=customer.objects.get(user_id=uid)
            s_cart=product_cart.objects.filter(customer_id=cid)
            s_cart.delete()
            tid.save()
        otp=random.randint(111111,999999)
        tid.ord_deliver_otp=otp
        tid.save()
        if is_valid_checksum:
            print("Checksum Matched")
            received_data['message'] = "Checksum Matched"
            if received_data['STATUS'] == ['TXT_SUCCESS']:

                return render(request,"VIKIPI_CUSTOMER_PANEL/payment_result.html",{'tid':tid,'context':received_data})
        else:
            print("Checksum Mismatched")
            received_data['message'] = "Checksum Mismatched"

        return render(request,"VIKIPI_CUSTOMER_PANEL/payment_result.html",{'tid':tid,'context':received_data})

@csrf_exempt
def updateqty(request):
    id=request.POST['id']
    qty = request.POST['qty']
    pid = product_cart.objects.get(id=id)
    print("--------->pid",pid)
    print("--->qty ",pid.quantity)
    pid.quantity=qty 
    pid.save()

    uid=user.objects.get(email=request.session['email'])
    cid=customer.objects.get(user_id=uid)
    catid=category.objects.all()
    pid_cart=product_cart.objects.filter(customer_id=cid)
    sid=shop_details.objects.all()
    cart_id=product_cart.objects.filter(customer_id=cid).count()
    cart_id_get=product_cart.objects.filter(customer_id=cid)
    price_list=[]
    # n1=[]
    for i in pid_cart:
        price_list.append(i.product_id.product_price)
        # n1.append(i.total_price)
    total_price=sum(price_list)
    
    net_list = [] 
    for i in pid_cart:
        net_list.append(i.quantity * i.product_id.product_price)
    
    netamount = sum(net_list)
    print("-->netamount ",netamount)


    # data=User.objects.values()
    # data=list(data)
    return JsonResponse({'data':netamount})
from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from .models import *
from .utils import *
from VIKIPI_CUSTOMER_PANEL.views import *
import random
from datetime import *
from validate_email import validate_email
# Create your views here.
def base(request):
    return render(request,'VIKIPI_ADMIN_PANEL/base.html')

def homepage(request):
    return render(request,'VIKIPI_ADMIN_PANEL/homepage.html')
        
def home(request):
    if 'email' in request.session:
        if request.session['email']=='vikipi_admin@gmail.com':
            customer_view=customer.objects.filter(view=False).count()
            product_view=product.objects.filter(view=False).count()
            retailer_view=retailer.objects.filter(view=False).count()
            shop_view=shop_details.objects.filter(view=False).count()
            total=customer_view+product_view+retailer_view+shop_view
            
            context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
        
            return render(request,'VIKIPI_ADMIN_PANEL/admin_index.html',{'ct':context})
        else:    
            rid=retailer.objects.get(email=request.session['email'])
            if rid:
                return render(request,'VIKIPI_ADMIN_PANEL/index.html',{'rid':rid})
            else:
                return render(request,'VIKIPI_ADMIN_PANEL/login.html')   
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def retailer_register(request):
    if request.POST:
        pass
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/register.html')

def retailer_register_user(request):
    if 'email' not in request.session:    
        if request.POST['firstname']!='' and request.POST['lastname']!='' and request.POST['email']!='' and request.POST['password']!='':
            u_firstname=request.POST['firstname']
            u_lastname=request.POST['lastname']
            u_email=request.POST['email']
            is_valid=validate_email(u_email,verify=True)
            print("-------------------------------------------------------------",is_valid)
            u_password=request.POST['password']
            otp=random.randint(111111,999999)
            email_id=retailer.objects.filter(email=u_email)
            context={
                'firstname':u_firstname,
                'lastname':u_lastname,
                'otp':otp
            }
            sendmail("Otp Validation mail","retailer_otp",u_email,{'context':context})
            if not email_id:
                if is_valid:
                    rid = retailer.objects.create(firstname=u_firstname,lastname=u_lastname,email=u_email,password=u_password,otp=otp)
                    if rid:
                        return render(request,'VIKIPI_ADMIN_PANEL/otp_validation.html',{'email':u_email})
                    else:
                        emsg="Registration Fail"
                        return render(request,'VIKIPI_ADMIN_PANEL/register.html',{'emsg':emsg})
                else:
                    emsg="email does not exist in gmail enter valid"
                    return render(request,'VIKIPI_ADMIN_PANEL/register.html',{'emsg':emsg})
            else:
                emsg="Please Enter another email id"
                return render(request,'VIKIPI_ADMIN_PANEL/register.html',{'emsg':emsg})
        else:
            emsg="Please Enter The Details"
            return render(request,'VIKIPI_ADMIN_PANEL/register.html',{'emsg':emsg})
        
        if rid:
            return render(request,'VIKIPI_ADMIN_PANEL/login.html')
        else:
            emsg="Registration Fail"
            return render(request,'VIKIPI_ADMIN_PANEL/register.html',{'emsg':emsg})
    else:
        if request.session['email']=='vikipi_admin@gmail.com':
            customer_view=customer.objects.filter(view=False).count()
            product_view=product.objects.filter(view=False).count()
            retailer_view=retailer.objects.filter(view=False).count()
            shop_view=shop_details.objects.filter(view=False).count()
            total=customer_view+product_view+retailer_view+shop_view
            context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
            
            return render(request,'VIKIPI_ADMIN_PANEL/admin_index.html',{'ct':context})
        else:    
            rid=retailer.objects.filter(email=request.session['email'])
            if rid:
                return render(request,'VIKIPI_ADMIN_PANEL/index.html',{'rid':rid})
            else:
                return render(request,'VIKIPI_ADMIN_PANEL/login.html')
        

def retailer_login_user(request):
    
        if request.POST['email']!='' and request.POST['password']!='':
            email=request.POST['email']
            password=request.POST['password']
            if email=='vikipi_admin@gmail.com' and password=='admin':
                request.session['email']=email
                customer_view=customer.objects.filter(view=False).count()
                product_view=product.objects.filter(view=False).count()
                retailer_view=retailer.objects.filter(view=False).count()
                shop_view=shop_details.objects.filter(view=False).count()
                total=customer_view+product_view+retailer_view+shop_view
                context={
                        'customer':customer_view,
                        'product':product_view,
                        'retailer':retailer_view,
                        'shop':shop_view,
                        'total':total,
                    }
                return render(request,'VIKIPI_ADMIN_PANEL/admin_index.html',{'ct':context})
            else:
                frid=retailer.objects.filter(email=email)
                
                if frid:
                    rid=retailer.objects.get(email=email)
                    if rid.password==password:
                        request.session['email']=email
                        request.session['firstname']=rid.firstname
                        request.session['lastname']=rid.lastname
                        return render(request,'VIKIPI_ADMIN_PANEL/index.html',{'rid':rid})
            
                    else:
                        emsg="Incorrect Password"
                        return render(request,'VIKIPI_ADMIN_PANEL/login.html',{'emsg':emsg})
                else:
                    emsg="Incorrect Email Id"
                    return render(request,'VIKIPI_ADMIN_PANEL/login.html',{'emsg':emsg})
        
        elif 'email' in request.session:    
            if request.session['email']=='vikipi_admin@gmail.com':
                customer_view=customer.objects.filter(view=False).count()
                product_view=product.objects.filter(view=False).count()
                retailer_view=retailer.objects.filter(view=False).count()
                shop_view=shop_details.objects.filter(view=False).count()
                total=customer_view+product_view+retailer_view+shop_view
                context={
                        'customer':customer_view,
                        'product':product_view,
                        'retailer':retailer_view,
                        'shop':shop_view,
                        'total':total,
                    }
                return render(request,'VIKIPI_ADMIN_PANEL/admin_index.html',{'ct':context})
            else:
                rid=retailer.objects.get(email=request.session['email'])
                return render(request,'VIKIPI_ADMIN_PANEL/index.html',{'rid':rid})
        else:
            emsg="Please enter Email ID and Password"
            return render(request,'VIKIPI_ADMIN_PANEL/login.html',{'emsg':emsg})         
    

def retailer_login(request):
    if 'email' in request.session:
        print("-----------------------------------------",request.session['email'])
        if request.session['email']=='vikipi_admin@gmail.com':
            customer_view=customer.objects.filter(view=False).count()
            product_view=product.objects.filter(view=False).count()
            retailer_view=retailer.objects.filter(view=False).count()
            shop_view=shop_details.objects.filter(view=False).count()
            total=customer_view+product_view+retailer_view+shop_view
            context={
                    'customer':customer_view,
                    'product':product_view,
                    'retailer':retailer_view,
                    'shop':shop_view,
                    'total':total,
                }
            return render(request,'VIKIPI_ADMIN_PANEL/admin_index.html',{'ct':context})
        else:
            rid=retailer.objects.filter(email=request.POST['email'])
            if rid:
                    return render(request,'VIKIPI_ADMIN_PANEL/index.html')
            else:
                
                return render(request,'VIKIPI_ADMIN_PANEL/login.html')
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
        
def retailer_edit_profile(request):
    if 'email' in request.session:
        if request.session['email']=='vikipi_admin@gmail.com':
            return render(request,'VIKIPI_ADMIN_PANEL/admin_index.html')
        else:
            rid=retailer.objects.get(email=request.session['email'])
            fsid=shop_details.objects.filter(owner_id=rid)
            if fsid:
                sid=shop_details.objects.get(owner_id=rid)
                return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'rid':rid,'sid':sid})
            else:
                return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'rid':rid})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def retailer_edit_profile_personal_details_user(request):
    if 'email' in request.session:
        phonenumber=request.POST['phonenumber']
        gender=request.POST['gender']
        rlandmark=request.POST['rlandmark']
        rcity=request.POST['rcity']
        rstate=request.POST['rstate']
        rcountry=request.POST['rcountry']
        rpincode=request.POST['rpincode']
        rid=retailer.objects.get(email=request.session['email'])
        rid.phnumber=phonenumber
        rid.gender=gender
        rid.home_address=rlandmark
        rid.home_city=rcity
        rid.home_state=rstate
        rid.home_country=rcountry
        rid.home_pincode=rpincode
        rid.save()
        msg="Details are successfully Changed"
        return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'rid':rid,'msg':msg})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def retailer_edit_profile_shop_details_user(request):
    if 'email' in request.session:
        frid=retailer.objects.filter(email=request.session['email'])
        if frid:
            rid=retailer.objects.get(email=request.session['email'])
            sid=shop_details.objects.filter(owner_id=rid)
            
            if not sid:
                if request.POST['shopname']!='' and request.POST['shoptype']!='' and request.POST['slandmark']!='' and request.POST['scity']!='' and request.POST['sstate']!='' and request.POST['scountry']!='' and request.POST['spincode']!='' and request.FILES['idproof']!='' and request.FILES['ebill']!='':
                    shopname=request.POST['shopname']
                    shoptype=request.POST['shoptype']
                    slandmark=request.POST['slandmark']
                    scity=request.POST['scity']
                    sstate=request.POST['sstate']
                    scountry=request.POST['scountry']
                    spincode=request.POST['spincode']
                    owner_id_proof=request.FILES['idproof']
                    elc_bill=request.FILES['ebill']
                    rid=retailer.objects.get(email=request.session['email'])
                    sid=shop_details.objects.create(owner_id=rid,shop_name=shopname,elc_bill=elc_bill,owner_id_proof=owner_id_proof,shop_type=shoptype,shop_address=slandmark,shop_city=scity,shop_state=sstate,shop_country=scountry,shop_pincode=spincode)
                    if sid:
                        sid=shop_details.objects.get(owner_id=rid)
                        msg="Details are successfully Changed"
                        return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'rid':rid,'msg':msg,'sid':sid})
                else:
                    emsg="Please enter all the details"
                    return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'rid':rid,'emsg':emsg})
            else:
                sid=shop_details.objects.get(owner_id=rid)
                return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'rid':rid,'sid':sid})
        else:
            return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def add_product(request):
    if 'email' in request.session:
        cid = category.objects.all()
        rid=retailer.objects.get(email=request.session['email'])
        
        if rid:
            print("--------------",rid)
            print("---------------> add product pic",rid.profile_pic)
            return render(request,'VIKIPI_ADMIN_PANEL/add_product.html',{'rid':rid,'cid':cid})
    else:
        print("user does not login ")
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def add_product_details(request):
    if 'email' in request.session:
        frid=retailer.objects.filter(email=request.session['email'])
        if frid:
            rid=retailer.objects.get(email=request.session['email'])
            sid=shop_details.objects.get(owner_id=rid)
            if rid.status=='Approve':
                if 'productname' in request.POST:
                    productname=request.POST['productname']
                    c_id=request.POST['category']
                    cid=category.objects.get(id=c_id)
                    quantity=request.POST['quantity']
                    price=request.POST['price']
                    description=request.POST['description']
                    image=request.FILES['productimage']
                    pid=product.objects.create(product_name=productname,shop_id=sid,product_category=cid,product_quantity=quantity,product_price=price,product_description=description,product_image=image,owner_id=rid)
                    if pid:
                        pid=product.objects.filter(owner_id=rid)
                        return render(request,'VIKIPI_ADMIN_PANEL/view-all-products.html',{'rid':rid,'pid':pid})
                    else:
                        msg="Fail to add the Product details"
                        return render(request,'VIKIPI_ADMIN_PANEL/add_product.html',{'msg':msg,'rid':rid})
                else:
                    msg="Fail to add the Product details"
                    return render(request,'VIKIPI_ADMIN_PANEL/index.html',{'rid':rid,'msg':msg})
            else:
                msg="Please Update Your Status to Add Products"
                print("---------------------------------------------",msg)
                return render(request,'VIKIPI_ADMIN_PANEL/add_product.html',{'msg':msg,'rid':rid})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
def forgot_password(request):
    return render(request,'VIKIPI_ADMIN_PANEL/forgot-password.html')

def forgot_password_user(request):
        email=request.POST['email']
        rid = retailer.objects.get(email=email)
        if rid:
            otp=random.randint(111111,999999)
            rid.otp = otp
            rid.save()
            context={
                        'firstname':rid.firstname,
                        'otp':rid.otp,
                    }
            sendmail("Reset Password","retailer_otp",email,{'context':context})
            return render(request,"VIKIPI_ADMIN_PANEL/recover-password.html",{'email':email})
        else:
            return render(request,"VIKIPI_ADMIN_PANEL/forgot-password.html")

def recover_password(request):
    return render(request,'VIKIPI_ADMIN_PANEL/recover-password.html')

def recover_password_user(request):
    if 'email' in request.POST:
            email=request.POST['email']
            otp=request.POST['rotp']
            password1=request.POST['password']
            password2=request.POST['confirmpassword']
            rid=retailer.objects.get(email=email)
            if rid:
                if otp==str(rid.otp):
                    if password1==password2:
                        rid.password=password1
                        rid.save()
                        return render(request,"VIKIPI_ADMIN_PANEL/login.html")
              
def retailer_logout(request):
    del request.session['email']
    if 'rid' in request.session:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def change_password_user(request):
    if 'email' in request.session:
        email=request.session['email']
        current_password=request.POST['currentpassword']
        new_password=request.POST['newpassword']
        retype_new_password=request.POST['retypenewpassword']
        rid=retailer.objects.get(email=email)
        print("----------------------------------------------------------rid",rid)
        
        if rid:
            fsid=shop_details.objects.filter(owner_id=rid)
            if fsid:
                sid=shop_details.objects.get(owner_id=rid)
            if rid.password==current_password:
                if new_password==retype_new_password:
                    rid.password=new_password
                    rid.save()
                    msg='Your password is successfully changed.'
                    return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'msg':msg,'rid':rid,'sid':sid})
                else:
                    msg="New password and Retype New password must be same"
                    return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'emsg':msg,'rid':rid,'sid':sid})
            else:
                msg="Current Password is Incorrect"
                return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'emsg':msg,'rid':rid,'sid':sid})
        else:
            return render(request,'VIKIPI_ADMIN_PANEL/index.html',{'rid':rid})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
    
def retailer_view_all_products(request):
    
    rid=retailer.objects.get(email=request.session['email'])    
    pid=product.objects.filter(owner_id=rid)
    return render(request,'VIKIPI_ADMIN_PANEL/view-all-products.html',{'pid':pid,'rid':rid})

def retailer_view_product(request,pk):
    rid=retailer.objects.get(email=request.session['email'])
    pid=product.objects.get(id=pk)
    pimg=product_images.objects.filter(product_id=pid)
    return render(request,'VIKIPI_ADMIN_PANEL/view_product.html',{'pid':pid,'rid':rid,'pimg':pimg})

def retailer_edit_product(request,pk):
    cid=category.objects.all()
    rid=retailer.objects.get(email=request.session['email'])
    pid=product.objects.get(id=pk)
    return render(request,'VIKIPI_ADMIN_PANEL/edit_product_details.html',{'pid':pid,'rid':rid,'cid':cid})

def retailer_edit_product_user(request):
    if 'id' in request.POST:
        id=request.POST['id']
        product_name=request.POST['productname']
        c_id=request.POST['category']
        cid=category.objects.get(id=c_id)
        quantity=request.POST['quantity']
        price=request.POST['price']
        description=request.POST['description']
        image=request.FILES['product_image']
        pid=product.objects.get(id=id)
        pid.product_name=product_name
        pid.product_category=cid
        pid.product_price=price
        pid.product_quantity=quantity
        pid.product_description=description
        pid.product_image=image
        pid.save()
        pid=product.objects.all()
        rid=retailer.objects.get(email=request.session['email'])
        return render(request,'VIKIPI_ADMIN_PANEL/view-all-products.html',{'pid':pid,'rid':rid})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/view-all-products.html',{'allpid':allpid})

def retailer_delete_product(request,pk):
    if 'email' in request.session:
        frid=retailer.objects.filter(email=request.session['email'])
        if frid:
            rid=retailer.objects.get(email=request.session['email'])
            pid=product.objects.get(id=pk)
            pid.delete()
            pid=product.objects.all()
            return render(request,'VIKIPI_ADMIN_PANEL/view-all-products.html',{'pid':pid,'rid':rid})
        else:
            return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def retailer_todays_order(request):
    if 'email' in request.session:
        rid=retailer.objects.get(email=request.session['email'])

        ord_id=order_details.objects.filter(retailer_id=rid) 
        today_ord=[]
        for i in ord_id:
            if i.date_of_order.date()==date.today():
                today_ord.append(i)
            
        return render(request,'VIKIPI_ADMIN_PANEL/retailer_view_all_orders.html',{'rid':rid, 'today_ord':today_ord})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def retailer_total_orders_details(request):
    if 'email' in request.session:
        rid=retailer.objects.get(email=request.session['email'])
        print("-------------------------------------------------rid",rid)
        ord_dtls_rid=order_details.objects.filter(retailer_id=rid)
        lst_product_order=[]
        if ord_dtls_rid:
            for i in ord_dtls_rid:
                lst_product_order.append(i)
            return render(request,'VIKIPI_ADMIN_PANEL/retailer_view_all_orders.html',{'order_lst':lst_product_order,'rid':rid})
        else:

            return render(request,'VIKIPI_ADMIN_PANEL/retailer_view_all_orders.html',{'rid':rid})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
def ratailer_pending_orders(request):
    pass

def retailer_pending_orders_user(request):
    pass

def retailer_delivered_orders(request):
    pass

def retailer_change_profile_picture(request):
    picture=request.FILES['picture']
    rid=retailer.objects.get(email=request.session['email'])
    print(rid.profile_pic)
    if rid:
        rid.profile_pic=picture
        rid.save()
        # return redirect('home')
        return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html',{'rid':rid})

    else:
        return redirect('home')
        # return render(request,'VIKIPI_ADMIN_PANEL/edit_profile.html')
def retailer_upload_product_image(request,pk):
    pid=product.objects.get(id=pk)
    rid=retailer.objects.get(email=request.session['email'])
    print('---------------------------------------------------------------------',request.session['email'])
    return render(request,'VIKIPI_ADMIN_PANEL/upload-product-image.html',{'pid':pid,'rid':rid})
def retailer_upload_product_image_user(request):
    if 'email' in request.session:
        if 'id' in request.POST:
            id=request.POST['id']
            image=request.FILES.getlist('upload_img')
            for f in image:
                pid=product.objects.get(id=id)
                pimgcreate=product_images.objects.create(product_id=pid,sub_image=f)
                pimg=product_images.objects.filter(product_id=pid)
                rid=retailer.objects.get(email=request.session['email'])
            return render(request,'VIKIPI_ADMIN_PANEL/view_product.html',{'rid':rid,'pid':pid,'pimg':pimg})
        else:
            return render(request,'VIKIPI_ADMIN_PANEL/view_product.html',{'rid':rid,'pid':pid,'pimg':pimg})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
def retailer_feedback(request):
    if 'email' in request.session:
        rid=retailer.objects.get(email=request.session['email'])
        return render(request,'VIKIPI_ADMIN_PANEL/retailer-feedback.html',{'rid':rid})

def retailer_feedback_user(request):
    if 'email' in request.session:
        rid=retailer.objects.get(email=request.session['email'])
        review=request.POST['your_review']
        overall_experience=request.POST['overall_experience']
        timely_response=request.POST['timely_response']
        our_support=request.POST['our_support']
        overall_setisfaction=request.POST['overall_setisfaction']
        suggestion=request.POST['overall_setisfaction']
        rf=retailer_FeedBack.objects.create(retailer_id=rid,review=review,overall_experience=overall_experience,timely_response=timely_response,our_support=our_support,overall_setisfaction=overall_setisfaction,suggestion=suggestion)
        return render(request,'VIKIPI_ADMIN_PANEL/index.html',{'rid':rid})
def retailer_otp_validation(request):
    if 'email' in request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        rid=retailer.objects.get(email=email)
        if otp==str(rid.otp):
                rid.otp_status="approved"
                rid.save()
                return render(request,'VIKIPI_ADMIN_PANEL/login.html')
        else:
            msg="Please enter valid otp"
            return render(request,'VIKIPI_ADMIN_PANEL/otp_validation.html',{'msg':msg})
    else:
        msg="registration Failed"
        return render(request,'VIKIPI_ADMIN_PANEL/register.html',{'msg':msg})
    


#---------------------------ADMIN------------------------------------------

def admin_view_all_retailers(request):
    if 'email' in request.session:
        if request.session['email']=='vikipi_admin@gmail.com':
            allrid=retailer.objects.all()
            customer_view=customer.objects.filter(view=False).count()
            product_view=product.objects.filter(view=False).count()
            retailer_view=retailer.objects.filter(view=False).count()
            shop_view=shop_details.objects.filter(view=False).count()
            total=customer_view+product_view+retailer_view+shop_view
            context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
            return render(request,'VIKIPI_ADMIN_PANEL/view-all-retailers.html',{'allrid':allrid,'ct':context})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')

def admin_view_all_products(request):
    if 'email' in request.session: 
        if request.session['email']=='vikipi_admin@gmail.com':
            pid=product.objects.all()
            customer_view=customer.objects.filter(view=False).count()
            product_view=product.objects.filter(view=False).count()
            retailer_view=retailer.objects.filter(view=False).count()
            shop_view=shop_details.objects.filter(view=False).count()
            total=customer_view+product_view+retailer_view+shop_view
            context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
            return render(request,'VIKIPI_ADMIN_PANEL/admin-view-all-products.html',{'pid':pid,'ct':context})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
def admin_add_employee(request):
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
            }
    return render(request,'VIKIPI_ADMIN_PANEL/add-employee.html',{'ct':context})

def admin_add_employee_user(request):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    qualification=request.POST['qualification']
    phonenumber=request.POST['phonenumber']
    gender=request.POST['gender_value']
    homeaddr=request.POST['rlandmark']
    city=request.POST['rcity']
    state=request.POST['rstate']
    country=request.POST['rcountry']
    pincode=request.POST['rpincode']
    eid=employee.objects.create(firstname=firstname,lastname=lastname,gender=gender,email=email,phnumber=phonenumber,qualification=qualification,address=homeaddr,city=city,state=state,country=country,pincode=pincode),
    if eid:
        customer_view=customer.objects.filter(view=False).count()
        product_view=product.objects.filter(view=False).count()
        retailer_view=retailer.objects.filter(view=False).count()
        shop_view=shop_details.objects.filter(view=False).count()
        total=customer_view+product_view+retailer_view+shop_view
        context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
        return render(request,'VIKIPI_ADMIN_PANEL/admin_index.html',{'ct':context})
    else:
        customer_view=customer.objects.filter(view=False).count()
        product_view=product.objects.filter(view=False).count()
        retailer_view=retailer.objects.filter(view=False).count()
        shop_view=shop_details.objects.filter(view=False).count()
        total=customer_view+product_view+retailer_view+shop_view
        context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
        return render(request,'VIKIPI_ADMIN_PANEL/add-employee.html',{'ct':context})

def admin_all_employee(request):
    eid=employee.objects.all()
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view-all-employee.html',{'eid':eid,'ct':context})

def admin_view_all_shops(request):
    sid=shop_details.objects.all().prefetch_related('owner_id')
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view-all-shops.html',{'sid':sid,'ct':context})

def admin_view_all_customers(request):
    cid = customer.objects.all().prefetch_related('user_id')
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/admin-view-all-customers.html',{'cid':cid,'ct':context})

def admin_retailers_pending_request(request):
    rid=retailer.objects.filter(status='pending')
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/retailers-pending-request.html',{'rid':rid,'ct':context})


def admin_view_retailer_profile(request,pk):
    rid=retailer.objects.get(id=pk)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    ord_dtls_rid=order_details.objects.filter(retailer_id=rid)
    ord_count=order_details.objects.filter(retailer_id=rid).count()
    lst_product_order=[]
    total_collection=0
    todays_collection=0
    if ord_dtls_rid:
        for i in ord_dtls_rid:
            lst_product_order.append(i)
            total_collection+=i.product_id.product_price
            if i.date_of_order.date()==date.today():
                todays_collection+=i.product_id.product_price
            print('-----------------------------------------------------------------------',i.date_of_order.date())
            print('-----------------------------------------------------------------------',date.today())
    
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    if rid:
        fsid=shop_details.objects.filter(owner_id=pk)
        if fsid:
            sid=shop_details.objects.get(owner_id=pk)
            pid=product.objects.filter(owner_id=pk)
            if pid:
                total_product=product.objects.filter(owner_id=pk).count()
                return render(request,'VIKIPI_ADMIN_PANEL/view-retailer-profile.html',{'rid':rid,'sid':sid,'pid':pid,'total_product':total_product,'ct':context,'lst_product_order':lst_product_order,'ord_count':ord_count,'total_collection':total_collection,'todays_collection':todays_collection})
            else:
                return render(request,'VIKIPI_ADMIN_PANEL/view-retailer-profile.html',{'rid':rid,'sid':sid,'ct':context})
        else:
            return render(request,'VIKIPI_ADMIN_PANEL/view-retailer-profile.html',{'rid':rid,'ct':context})
    
def admin_edit_retailer_profile(request,pk):
    pass

def admin_delete_retailer_profile(request,pk):
    rid=product.objects.get(id=pk)
    rid.delete()
    allrid=product.objects.all()
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/admin-view-all-products.html',{'allrid':allrid,'ct':context})

def admin_view_product(request,pk):
    pid=product.objects.get(id=pk)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    pimg=product_images.objects.filter(product_id=pk)
    return render(request,'VIKIPI_ADMIN_PANEL/admin-view-product.html',{'pid':pid,'ct':context,'pimg':pimg})

def admin_edit_product(request,pk):
    cid=category.objects.all()
    pid=product.objects.get(id=pk)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/admin-edit-product.html',{'pid':pid,'cid':cid,'ct':context})

def admin_edit_product_user(request):
    if 'id' in request.POST:
        id=request.POST['id']
        product_name=request.POST['productname']
        print("---------------------------------------------------------------------",product_name)
        c_id=request.POST['category']
        cid=category.objects.get(id=c_id)
        quantity=request.POST['quantity']
        price=request.POST['price']
        description=request.POST['description']
        image=request.FILES['product_image']
        pid=product.objects.get(id=id)
        pid.name=product_name
        pid.product_category=cid
        pid.product_price=price
        pid.product_quantity=quantity
        pid.product_description=description
        pid.product_image=image
        pid.save()
        pid=product.objects.all()
        customer_view=customer.objects.filter(view=False).count()
        product_view=product.objects.filter(view=False).count()
        retailer_view=retailer.objects.filter(view=False).count()
        shop_view=shop_details.objects.filter(view=False).count()
        total=customer_view+product_view+retailer_view+shop_view
        context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
        return render(request,'VIKIPI_ADMIN_PANEL/view-all-products.html',{'pid':pid,'ct':context})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/view-retailer-profile.html',{'pid':pid,'ct':context})

def admin_delete_product(request,pk):
    pid=product.objects.get(id=pk)
    pid.delete()
    pid=product.objects.all()
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/admin-view-all-products.html',{'pid':pid,'ct':context})

def admin_edit_employee_details(request,pk):
    eid=employee.objects.get(id=pk)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render (request,'VIKIPI_ADMIN_PANEL/employee-edit-details.html',{'eid':eid,'ct':context})

def admin_edit_employee_details_user(request):
    if 'id' in request.POST:
        id = request.POST['id']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        qualification = request.POST['qualification']
        phunumber = request.POST['phonenumber']
        gender = request.POST['gender_value']
        address = request.POST['rlandmark']
        city = request.POST['rcity']
        state = request.POST['rstate']
        country = request.POST['rcountry']
        pincode = request.POST['rpincode']
        eid=employee.objects.get(id=id)
        eid.firstname=firstname
        eid.lastname=lastname
        eid.email=email
        eid.qualification=qualification
        eid.phnumber=phunumber
        eid.gender=gender
        eid.address=address
        eid.city=city
        eid.state=state
        eid.country=country
        eid.pincode=pincode
        eid.save()
        eid=employee.objects.all()
        customer_view=customer.objects.filter(view=False).count()
        product_view=product.objects.filter(view=False).count()
        retailer_view=retailer.objects.filter(view=False).count()
        shop_view=shop_details.objects.filter(view=False).count()
        total=customer_view+product_view+retailer_view+shop_view
        context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
        return render(request,'VIKIPI_ADMIN_PANEL/view-all-employee.html',{'eid':eid,'ct':context})

def admin_delete_employee_details(request,pk):
    eid=employee.objects.get(id=pk)
    eid.delete()
    eid=employee.objects.all()
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view-all-employee.html',{'eid':eid,'ct':context})

def admin_view_customer_details(request,pk):
    cid = customer.objects.get(id=pk)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    orders=order_details.objects.filter(customer_id=pk)
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
            'orders':orders,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view-customer-details.html',{'cid':cid,'ct':context})

def admin_edit_customer_details(request,pk):
    try:
        cid=customer.objects.get(id=pk)
        customer_view=customer.objects.filter(view=False).count()
        product_view=product.objects.filter(view=False).count()
        retailer_view=retailer.objects.filter(view=False).count()
        shop_view=shop_details.objects.filter(view=False).count()
        total=customer_view+product_view+retailer_view+shop_view
        context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
        return render(request,'VIKIPI_ADMIN_PANEL/edit-customer-details.html',{'cid':cid,'ct':context})
    except:
        return render(request,'VIKIPI_ADMIN_PANEL/edit-customer-details.html')
    
def admin_edit_customer_details_user(request):
    pass

def admin_delete_customer_details(request,pk):
    pass

def admin_edit_shop_details(request,pk):
    sid=shop_details.objects.get(id=pk)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/admin_edit_shop_details.html',{'sid':sid,'ct':context})

def admin_edit_shop_details_user(request):
    pass

def admin_delete_shop_details(request,pk):
    sid=shop_details.objects.get(id=pk)
    sid.delete()
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    sid=shop_details.objects.all().prefetch_related('owner_id')
    return render(request,'VIKIPI_ADMIN_PANEL/view-all-shops.html',{'sid':sid,'ct':context})

def admin_contact(request):
    if 'email' in request.session:
        return render(request,'VIKIPI_ADMIN_PANEL/contact.html'),
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html'),

def admin_notification_shop(request):
    sid = shop_details.objects.filter(view=False)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/notification-shop.html',{'sid':sid,'ct':context})
def admin_notification_product(request):
    pid = product.objects.filter(view=False)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/notification-product.html',{'pid':pid,'ct':context})
def admin_notification_retailer(request):
    rid = retailer.objects.filter(view=False)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/notification-retailer.html',{'rid':rid,'ct':context})
def admin_notification_customer(request):
    cid = customer.objects.filter(view=False)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/notification-customer.html',{'cid':cid,'ct':context})
def admin_notification_product_view(request,pk):
    pid=product.objects.get(id=pk)
    pid.view=True
    pid.save()
    rid=retailer.objects.get(email=pid.owner_id.email)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view_product.html',{'pid':pid,'ct':context,'rid':rid})
def admin_notification_shop_view(request,pk):
    sid=shop_details.objects.get(id=pk)
    sid.view=True
    sid.save()
    pid=product.objects.filter(owner_id=sid.owner_id)
    total_product=product.objects.filter(owner_id=sid.owner_id).count()
    rid=retailer.objects.get(id=sid.owner_id.id)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    ord_dtls_rid=order_details.objects.filter(retailer_id=rid)
    ord_count=order_details.objects.filter(retailer_id=rid).count()
    lst_product_order=[]
    total_collection=0
    todays_collection=0
    if ord_dtls_rid:
        for i in ord_dtls_rid:
            lst_product_order.append(i)
            total_collection+=i.product_id.product_price
            if i.date_of_order.date()==date.today():
                todays_collection+=i.product_id.product_price

    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view-retailer-profile.html',{'pid':pid,'ct':context,'rid':rid,'sid':sid,'ord_count':ord_count,'total_collection':total_collection,'todays_collection':todays_collection,'lst_product_order':lst_product_order,'total_product':total_product})
def admin_notification_retailer_view(request,pk):
    rid=retailer.objects.get(id=pk)
    rid.view=True
    rid.save()
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view-retailer-profile.html',{'rid':rid,'ct':context})
def admin_notification_customer_view(request,pk):
    cid=customer.objects.get(id=pk)
    cid.view=True
    cid.save()
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view-customer-details.html',{'cid':cid,'ct':context})
def admin_update_retailer_status(request,pk):
    rid=retailer.objects.get(id=pk)
    status=request.POST['status']
    rid.status=status
    rid.save()
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    rid=retailer.objects.filter(status='pending')
    return render(request,'VIKIPI_ADMIN_PANEL/retailers-pending-request.html',{'rid':rid,'ct':context})
def admin_view_all_retailers_feedback(request):
    rtlr_feedback=retailer_FeedBack.objects.all().prefetch_related('retailer_id')
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/admin-retailer-feedback.html',{'ct':context,'rtlrfb':rtlr_feedback})
def admin_view_all_customer_feedback(request):
    ctmr_feedback=customer_FeedBack.objects.all().prefetch_related('customer_id')
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/admin-customer-feedback.html',{'ct':context,'ctmrfb':ctmr_feedback})
def admin_view_retailer_feedback(request,pk):
    rid=retailer.objects.get(id=pk)
    rtlfb=retailer_FeedBack.objects.get(retailer_id=rid)
    sid=shop_details.objects.get(owner_id=rid)
    customer_view=customer.objects.filter(view=False).count()
    product_view=product.objects.filter(view=False).count()
    retailer_view=retailer.objects.filter(view=False).count()
    shop_view=shop_details.objects.filter(view=False).count()
    total=customer_view+product_view+retailer_view+shop_view
    context={
            'customer':customer_view,
            'product':product_view,
            'retailer':retailer_view,
            'shop':shop_view,
            'total':total,
        }
    return render(request,'VIKIPI_ADMIN_PANEL/view-retailer-profile.html',{'rid':rid,'rtlfb':rtlfb,'ct':context,'sid':sid})
def admin_all_orders(request):
    if 'email' in request.session:
        ord_id=order_details.objects.all()
        customer_view=customer.objects.filter(view=False).count()
        product_view=product.objects.filter(view=False).count()
        retailer_view=retailer.objects.filter(view=False).count()
        shop_view=shop_details.objects.filter(view=False).count()
        total=customer_view+product_view+retailer_view+shop_view
        context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
        return render(request,'VIKIPI_ADMIN_PANEL/order_summary.html',{'ord_id':ord_id,'ct':context})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
def admin_todays_orders(request):
    if 'email' in request.session:
        ord_id=order_details.objects.all()
        
        today_ord=[]
        for i in ord_id:
            if i.date_of_order.date()==date.today():
                today_ord.append(i)
        customer_view=customer.objects.filter(view=False).count()
        product_view=product.objects.filter(view=False).count()
        retailer_view=retailer.objects.filter(view=False).count()
        shop_view=shop_details.objects.filter(view=False).count()
        total=customer_view+product_view+retailer_view+shop_view
        context={
                'customer':customer_view,
                'product':product_view,
                'retailer':retailer_view,
                'shop':shop_view,
                'total':total,
            }
        return render(request,'VIKIPI_ADMIN_PANEL/order_summary.html',{'ct':context,'today_ord':today_ord})
    else:
        return render(request,'VIKIPI_ADMIN_PANEL/login.html')
        


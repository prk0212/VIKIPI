"""VIKIPI_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from VIKIPI_ADMIN_PANEL import views
from django.views.generic import TemplateView


urlpatterns = [
    path('home/',views.home,name='home'),
    path('retailer_register/',views.retailer_register,name='retailer_register'),
    path('retailer_register_user/',views.retailer_register_user,name='retailer_register_user'),
    path('retailer_login/',views.retailer_login,name='retailer_login'),
    path('retailer_login_user/',views.retailer_login_user,name='retailer_login_user'),
    path('retailer_edit_profile/',views.retailer_edit_profile,name='retailer_edit_profile'),
    path('retailer_edit_profile_personal_details_user/',views.retailer_edit_profile_personal_details_user,name='retailer_edit_profile_personal_details_user'),
    path('retailer_edit_profile_shop_details_user/',views.retailer_edit_profile_shop_details_user,name='retailer_edit_profile_shop_details_user'),
    path('add_product/',views.add_product,name='add_product'),
    path('add_product_details/',views.add_product_details,name='add_product_detailes'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('forgot_password_user/',views.forgot_password_user,name='forgot_password_user'),
    path('recover_password/',views.recover_password,name='recover_password'),
    path('recover_password_user/',views.recover_password_user,name='recover_password_user'),
    path('retailer_logout/',views.retailer_logout,name='retailer_logout'),
    path('change_password_user/',views.change_password_user,name='change_password_user'),
    path('retailer_view_all_products/',views.retailer_view_all_products,name='retailer_view_all_products'), 
    path('retailer_view_product/<int:pk>',views.retailer_view_product,name='retailer_view_product'),
    path('retailer_edit_product/<int:pk>',views.retailer_edit_product,name='retailer_edit_product'),
    path('retailer_edit_product_user/',views.retailer_edit_product_user,name='retailer_edit_product_user'),
    path('retailer_delete_product/<int:pk>',views.retailer_delete_product,name='retailer_delete_product'),
    path('retailer_todays_order/',views.retailer_todays_order,name='retailer_todays_order'),
    path('retailer_total_orders_details/',views.retailer_total_orders_details,name='retailer_total_orders_details'),
    path('ratailer_pending_orders/',views.ratailer_pending_orders,name='ratailer_pending_orders'),
    path('retailer_pending_orders_user/',views.retailer_pending_orders_user,name='retailer_pending_orders_user'),
    path('retailer_delivered_orders/',views.retailer_delivered_orders,name='retailer_delivered_orders'),
    path('retailer_change_profile_picture/',views.retailer_change_profile_picture,name='retailer_change_profile_picture'),
    path('retailer_upload_product_image/<int:pk>',views.retailer_upload_product_image,name='retailer_upload_product_image'),
    path('retailer_upload_product_image_user',views.retailer_upload_product_image_user,name='retailer_upload_product_image_user'),
    path('retailer_feedback/',views.retailer_feedback,name='retailer_feedback'),
    path('retailer_feedback_user/',views.retailer_feedback_user,name='retailer_feedback_user'),
    path('retailer_otp_validation/',views.retailer_otp_validation,name='retailer_otp_validation'),
    
    

    
    # admin

    path('admin_view_all_retailers/',views.admin_view_all_retailers,name='admin_view_all_retailers'),
    path('admin_view_all_products/',views.admin_view_all_products,name='admin_view_all_products'),
    path('admin_add_employee/',views.admin_add_employee,name='admin_add_employee'),
    path('admin_add_employee_user/',views.admin_add_employee_user,name='admin_add_employee_user'),
    path('admin_all_employee/',views.admin_all_employee,name='admin_all_employee'),
    path('admin_view_all_shops/',views.admin_view_all_shops,name='admin_view_all_shops'),
    path('admin_view_all_customers/',views.admin_view_all_customers,name='admin_view_all_customers'),
    path('admin_retailers_pending_request/',views.admin_retailers_pending_request,name='admin_retailers_pending_request'),
    
    path('admin_view_retailer_profile/<int:pk>',views.admin_view_retailer_profile,name='admin_view_retailer_profile'),
    path('admin_edit_retailer_profile/<int:pk>',views.admin_edit_retailer_profile,name='admin_edit_retailer_profile'),
    path('admin_delete_retailer_profile/<int:pk>',views.admin_delete_retailer_profile,name='admin_delete_retailer_profile'),
    path('admin_view_product/<int:pk>',views.admin_view_product,name='admin_view_product'),
    path('admin_edit_product/<int:pk>',views.admin_edit_product,name='admin_edit_product'),
    path('admin_edit_product_user/',views.admin_edit_product_user,name='admin_edit_product_user'),
    path('admin_delete_product/<int:pk>',views.admin_delete_product,name='admin_delete_product'),
    path('admin_edit_employee_details/<int:pk>',views.admin_edit_employee_details,name='admin_edit_employee_details'),
    path('admin_edit_employee_details_user/',views.admin_edit_employee_details_user,name='admin_edit_employee_details_user'),
    path('admin_delete_employee_details/<int:pk>',views.admin_delete_employee_details,name='admin_delete_employee_details'),
    path('admin_view_customer_details/<int:pk>',views.admin_view_customer_details,name='admin_view_customer_details'),
    path('admin_edit_customer_details/<int:pk>',views.admin_edit_customer_details,name='admin_edit_customer_details'),
    path('admin_edit_customer_details_user/',views.admin_edit_customer_details_user,name='admin_edit_customer_details_user'),
    path('admin_delete_customer_details/<int:pk>',views.admin_delete_customer_details,name='admin_delete_customer_details'),
    path('admin_edit_shop_details/<int:pk>',views.admin_edit_shop_details,name='admin_edit_shop_details'),
    path('admin_edit_shop_details_user/',views.admin_edit_shop_details_user,name='admin_edit_shop_details_user'),
    path('admin_delete_shop_details/<int:pk>',views.admin_delete_shop_details,name='admin_delete_shop_details'),
    path('admin_contact/',views.admin_contact,name='admin_contact'),
    path('admin_notification_customer/',views.admin_notification_customer,name='admin_notification_customer'),
    path('admin_notification_product/',views.admin_notification_product,name='admin_notification_product'),
    path('admin_notification_shop/',views.admin_notification_shop,name='admin_notification_shop'),
    path('admin_notification_retailer/',views.admin_notification_retailer,name='admin_notification_retailer'),
    path('admin_notification_customer_view/<int:pk>',views.admin_notification_customer_view,name='admin_notification_customer_view'),
    path('admin_notification_retailer_view/<int:pk>',views.admin_notification_retailer_view,name='admin_notification_retailer_view'),
    path('admin_notification_shop_view/<int:pk>',views.admin_notification_shop_view,name='admin_notification_shop_view'),
    path('admin_notification_product_view/<int:pk>',views.admin_notification_product_view,name='admin_notification_product_view'),
    path('admin_update_retailer_status/<int:pk>',views.admin_update_retailer_status,name='admin_update_retailer_status'),
    path('admin_view_all_customer_feedback/',views.admin_view_all_customer_feedback,name='admin_view_all_customer_feedback'),
    path('admin_view_retailer_feedback/<int:pk>',views.admin_view_retailer_feedback,name='admin_view_retailer_feedback'),
    path('admin_view_all_retailers_feedback/',views.admin_view_all_retailers_feedback,name='admin_view_all_retailers_feedback'),
    path('admin_all_orders/',views.admin_all_orders,name='admin_all_orders'),
    path('admin_todays_orders/',views.admin_todays_orders,name='admin_todays_orders'),


    path("base/",views.base,name="base"),
    path("homepage/",views.homepage,name="homepage"),
]

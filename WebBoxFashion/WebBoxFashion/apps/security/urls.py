# coding=utf-8
from django.urls import path, re_path, include
from django.urls import resolve
from .views import Login, Logout
from .views import UserProfileData, UserList, UserNew, UserDelete
from .views import ActiveInactiveUser, ChangePassword, Login_Customer, Login_Partner
from .views import Register_Customer, Register_Partner


app_name = 'security'

urlpatterns = [
    
    path('login_partner/', Login_Partner.as_view(), name="login_partner"),
    path('login_customer/', Login_Customer.as_view(), name="login_customer"),
    path('register_partner/', Register_Partner.as_view(), name="register_partner" ),
    path('register_customer/', Register_Customer.as_view(), name="register_customer"),
    path('login/', Login.as_view(),  name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('userprofile/', UserProfileData.as_view(), name="userprofile"),
    path('userprofilechange-password/', ChangePassword.as_view(), name="userprofile-change-password"),
    path('user/list/', UserList.as_view(), name="user-list"),
    path('user/new/', UserNew.as_view(), name="user-new"),
    path('user/delete/<int:pk>/', UserDelete.as_view(), name="user-delete"),
    path('user/active-inactive/<int:user_id>/', ActiveInactiveUser.as_view(), name="user-active-inactive"),
   
    path('accounts/', include('allauth.urls')),
    

]
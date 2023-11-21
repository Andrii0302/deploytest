from django.contrib import admin
from django.urls import path,include

from .views import Register,Login,UserView,Logout,ForgotPassword,ResetPassword,EmailVerification
urlpatterns = [
    
    path('register/',Register.as_view() ),
    path('verify/<str:token>/', EmailVerification.as_view(), name='email-verification'),
    path('login/',Login.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',Logout.as_view()),  
    path('pswrd-forgot/',ForgotPassword.as_view()),
    path('pswrd-reset/',ResetPassword.as_view()),
]
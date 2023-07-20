from django.urls import path
from . import views
from rest_framework.authtoken import views as authtoken_views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.userlogin, name='userlogin'),
    path('sign-up', views.createUser, name='createUser'),
    path('forgetpassword', views.forgetPassword, name='forgetpassword'),
    path('dashboard', views.userDashboard, name='userDashboard'),
    path('testcase', views.testingCompiler, name='testingCompiler'),
    path('codeoutput', views.test_compilerCode, name='test_compilerCode'),
    path('mycourses', views.mycourses, name='mycourses'),
    
    # API Views with authentications
    path('user/',views.Authenticateuser.as_view()),
    path('register/',views.Registeruser.as_view()), #token auhtentication
    path('Authlogin/',views.LoginAuth_token.as_view()),
    path('Email-check/recovery/',views.RecoverUser_Account.as_view()),
   
]

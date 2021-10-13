"""mukundraj_nursery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('about',views.about,name="AboutUs"),
    path('signup',views.signup,name="SignUp"),
    path('login',views.login,name="Login"),
    path('for_pass',views.forgot_pass,name="Forgotpassword"),
    path('create_acc',views.create_acc,name=""),
    path('login_acc',views.login_acc,name="Login_acc"),
    path('logout',views.logout,name=""),
    path('siteadmin',views.admin,name="Administrator"),
    path('store',views.store,name="Store"),
    path('viewprofile',views.profile_land,name="Profile"),
    path('buycp1',views.buycp1,name="productcp1"),
    path('buycp2',views.buycp2,name="productcp2"),
    path('buycp3',views.buycp3,name="productcp3"),
    path('buysp1',views.buysp1,name="productsp1"),
    path('buysp2',views.buysp2,name="productsp2"),
    path('buysp3',views.buysp3,name="productsp3"),
    path('buysp4',views.buysp4,name="productsp4"),
    path('buybp1',views.buybp1,name="productbp1"),
    path('buybp2',views.buybp2,name="productbp2"),
    path('buybp3',views.buybp3,name="productbp3"),
]

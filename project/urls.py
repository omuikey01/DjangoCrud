"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homepage),
    path("", views.homepage, name=""),
    path("register/", views.registerpage, name="register"),
    path("login/", views.loginpage, name="login"),
    path("logout/", views.logoutpage, name="logout"),
    path("registerData/", views.registerpageData, name="registerData"),
    path("loginData/", views.loginDataData, name="loginData"),
    path("queryData/", views.queryDatapage, name="queryData"),
    path("showqueryData/", views.showqueryDatapage, name="showqueryData"),
    path("delete/<str:mail>,<int:idd>", views.Deletepage, name="delete"),
    path("edit/<str:mail>,<int:idd>/", views.editpage, name="edit"),
    path("updatequery/<int:idd>", views.updatequerydatapage, name="updatequery"),
    path("search/<str:mail>", views.search, name="search"),
]
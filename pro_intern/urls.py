"""pro_intern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Bank import views
#from Bank.views import detailAPIView,ifscAPIView

urlpatterns = [

    path('admin/', admin.site.urls),
#    path('',detailAPIView.as_view(),name="details"),
    path('',views.detail_list,name="details"),
    path('ifsc/',views.ifsc_list,name="ifsc"),


    #path('ifscgg/',ifscAPIView.as_view(),name="ifsc")
]

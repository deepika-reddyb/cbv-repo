"""CBVProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from myApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^students/',views.StudentListView.as_view(),name='students'),
    url(r'^(?P<pk>\d+)/',views.StudentDetailView.as_view(),name='detail'),
    url(r'^create/',views.StudentCreateView.as_view(),name='create'),
    url(r'update/(?P<pk>\d+)/',views.StudentUpdateView.as_view()),
    url(r'delete/(?P<pk>\d+)/',views.StudentDeleteView.as_view()),
   
]

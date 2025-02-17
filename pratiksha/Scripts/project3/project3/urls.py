"""
URL configuration for project3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app3.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sampl1/',sampl1,name='sampl1'),
    path('sampl2/',sampl2,name='sampl2'),
    path('sampl3/',sampl3,name='sampl3'),
    path('sampl4/',sampl4,name='sampl4'),
]

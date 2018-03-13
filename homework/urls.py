"""shifu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^page/(?P<title>[a-z]+)$', views.page, name='page'),
    url(r'^all_city$', views.all_city, name='all_city'),
    url(r'^new_city$', views.new_city, name='new_city'),
    url(r'^edit_city/(?P<id>[0-9]+)$', views.edit_city, name='edit_city'),
    url(r'^del_city/(?P<id>[0-9]+)$', views.del_city, name='del_city'),
]

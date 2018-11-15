"""myMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from goods import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^goods/', include('goods.urls')),

    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls')),

    url('add_production.html', views.add_production),
    url('add_class.html', views.add_class),
    url('add_ingre.html', views.add_ingre),
    url('add_foods.html', views.add_foods),
    url('get_foods.html', views.get_foods),
    url('edit_foods.html/', views.edit_foods),
    url('delete_foods.html', views.delete_foods)
]

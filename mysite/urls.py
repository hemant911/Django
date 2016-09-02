"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^$', include('polls.urls')),
	  url(r'^admin/', admin.site.urls),


# user auth urls
url(r'^login/$',views.login,name ='vote'),
url(r'^auth/$', views.auth_view,name = 'auth_view'),
url(r'^logout/$',views.logout,name = 'logout'),
url(r'^loggedin/$',views.loggedin,name = 'loggedin'),
url(r'^invalid/$',views.inavlid_login, name = 'invalid_login'),
]

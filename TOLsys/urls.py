from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from tolsys import views as tolsys_views
from tolsys import urls as tolsys_urls
from django.conf.urls import include

urlpatterns = [
    url(r'^$', tolsys_views.MainPage, name='mainpage'),
    url(r'^tolsys/', include(tolsys_urls)),
    # url(r'^tolsys/', include(tolsys_urls)),
    url('admin/', admin.site.urls),
]

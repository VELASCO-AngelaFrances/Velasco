from django.contrib import admin
from django.urls import path
from tolsys import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^newlist_url$', views.NewList, name='newlist'),
    url(r'^(\d+)/$', views.ViewList, name='viewlist'),
    url(r'^(\d+)/addans$', views.AddAns, name='addans'),
    url(r'^(\d+)/addappointment$', views.AddAppointment, name='addappointment'),
    url(r'^(\d+)/app_url$', views.App, name='app_url'),
    url(r'^edit/(\d+)', views.edit, name='edit'),
    url(r'^edit/update/(\d+)', views.update, name='update'),
    url(r'^(\d+)/delete/', views.delete, name='delete'),
    url(r'^None/Addans2/', views.Addans2, name='Addans2'),
    # path('app_url', views.App, name='app_url'),
    # path('', views.Summary)
    # path('addappointment', views.AddAppointment, name='addappointment'),
    path('topic', views.TopicPage, name='topic'),
    path('newsroom', views.Newsroom, name='newsroom'),
    path('findhelp', views.Findhelp, name='findhelp'),
    path('aboutus', views.Aboutus, name='aboutus'),
    # url(r'^(\d+)/delete$', views.Delete, name='delete'),
]
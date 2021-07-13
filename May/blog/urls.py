#booktest/urls.py
from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^index/$',views.index),
    #url(r'^(\d+)$',views.show),
    url(r'^new/$',views.NewUser),
]
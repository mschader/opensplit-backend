from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^v1/user/$', views.user_list),
    url(r'^v1/user/(?P<pk>[0-9]+)/$', views.user_detail),
]

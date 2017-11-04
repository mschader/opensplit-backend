from django.urls import path, include
from rest_framework import routers

from opensplit.api import views


router_v1 = routers.DefaultRouter()
router_v1.register('users', views.UserViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
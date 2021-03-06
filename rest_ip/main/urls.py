from django.urls import path, include
from rest_framework import routers
from main import endpoints

router = routers.DefaultRouter()
router.register(r'list_all_ips', endpoints.CIDRViewSetAll)

urlpatterns = [
    path('api/', include(router.urls)),
]

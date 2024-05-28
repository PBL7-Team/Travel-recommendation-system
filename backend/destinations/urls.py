from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from .views import DestinationViewSet

router = DefaultRouter()
router.register(r'destinations', DestinationViewSet)

app_name="destinations"
urlpatterns = [
    re_path('api/v1/', include(router.urls)),
]
from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter
from .views import AttractionViewSet
app_name = "attractions"
router = DefaultRouter()
router.register(r'attractions', AttractionViewSet)

urlpatterns = [
    re_path(
        r"^api/v1/", include(router.urls)
    ),
]
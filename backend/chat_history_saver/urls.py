from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from .views import ChatHistoryViewSet

router = DefaultRouter()
router.register(r"chathistory", ChatHistoryViewSet, basename="chathistory")

app_name = "chat_history_saver"
urlpatterns = [
    re_path(
        r"^api/v1/", include(router.urls)
    ),
]

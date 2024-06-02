from django.urls import path
from .views import MyAPIView

app_name = "scrapy_api"
urlpatterns = [
    path("api/v1/<str:action>/", MyAPIView.as_view(), name="api-action"),
]

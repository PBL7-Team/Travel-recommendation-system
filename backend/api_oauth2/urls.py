from django.urls import path, include,re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework_nested import routers

from .views import Oauth2ViewSet

app_name = "api_oauth2"
router = routers.SimpleRouter(trailing_slash=False)

router.register(r"", Oauth2ViewSet, basename="oauth2")

urlpatterns = [
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^api/v1/', include(router.urls)),
]

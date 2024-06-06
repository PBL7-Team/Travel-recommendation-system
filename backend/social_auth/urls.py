from django.urls import path, include,re_path
from rest_framework_nested import routers

from .views import GoogleSocialAuthView,FacebookSocialAuthView,TwitterSocialAuthView

app_name = "social_auth"
router = routers.SimpleRouter()

router.register(r"google",GoogleSocialAuthView, basename="google")


urlpatterns = [
    re_path(r'^api/v1/', include(router.urls)),
    
]
# urlpatterns = [
#     path('google', GoogleSocialAuthView.as_view()),
#     path('facebook', FacebookSocialAuthView.as_view()),
#     path('twitter', TwitterSocialAuthView.as_view()),
#     # re_path(
#     #     r"^api/v1/", include(router.urls)
#     # ),
# ]
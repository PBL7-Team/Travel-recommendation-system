from django.urls import path, include,re_path
from rest_framework_nested import routers

from .views import GoogleSocialAuthView,FacebookSocialAuthView,TwitterSocialAuthView

app_name = "social_auth"
router = routers.SimpleRouter(trailing_slash=False)

router.register(r"google",GoogleSocialAuthView.as_view(), basename="google")
router.register(r"facebook",FacebookSocialAuthView.as_view(), basename="facebook")
router.register(r"twitter",TwitterSocialAuthView.as_view(), basename="twitter")

# urlpatterns = [
#     re_path(r'^api/v1/', include(router.urls)),
    
# ]
urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    path('facebook/', FacebookSocialAuthView.as_view()),
    path('twitter/', TwitterSocialAuthView.as_view()),
]
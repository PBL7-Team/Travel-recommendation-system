"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/o/", include("api.urls", namespace="api")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path('', include("api_oauth2.urls")),
    
    path('', include("api_user.urls", namespace="users")),
    path('', include("destinations.urls", namespace="destinations")),
    path('', include("attraction.urls", namespace="attraction")), 
    path('', include("chat_history_saver.urls", namespace="chat_history_saver")),
]

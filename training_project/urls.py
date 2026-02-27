from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/token/", obtain_auth_token),

    # HTML views
    path('providers/', include('providers.urls')),

    # DRF API views
    path('api/providers/', include('providers.api_urls')),  # API URL prefix
]
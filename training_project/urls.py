from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # HTML views
    path('providers/', include('providers.urls')),

    # DRF API views
    path('api/providers/', include('providers.api_urls')),  # API URL prefix
]
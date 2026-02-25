from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProviderViewSet

router = DefaultRouter()
router.register(r"", ProviderViewSet, basename="provider")  # no prefix here, router will use ''

urlpatterns = [
    path("", include(router.urls)),
]
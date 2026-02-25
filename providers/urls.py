from django.urls import path
from .views import (
    ProviderListView,
    ProviderDetailView,
    ProviderListCreateAPIView,
    ProviderDetailAPIView,
)

urlpatterns = [
    # HTML Views
    path("", ProviderListView.as_view(), name="provider_list"),
    path("<int:pk>/", ProviderDetailView.as_view(), name="provider_detail"),

    # API Endpoints
    path("api/providers/",
         ProviderListCreateAPIView.as_view(),
         name="api_provider_list"),

    path("api/providers/<int:pk>/",
         ProviderDetailAPIView.as_view(),
         name="api_provider_detail"),
]
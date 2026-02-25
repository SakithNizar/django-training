from django.urls import path
from .views import ProviderListView, ProviderDetailView

urlpatterns = [
    path("", ProviderListView.as_view(), name="provider_list"),
    path("<int:pk>/", ProviderDetailView.as_view(), name="provider_detail"),
]
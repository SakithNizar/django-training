from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Provider

# DRF imports
from rest_framework import viewsets, filters
from .serializers import ProviderSerializer

class ProviderListView(ListView):
    model = Provider
    template_name = "providers/provider_list.html"
    context_object_name = "providers"
    ordering = ["business_name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")

        if search:
            queryset = queryset.filter(
                Q(business_name__icontains=search) |
                Q(email__icontains=search)
            )
        return queryset


class ProviderDetailView(DetailView):
    model = Provider
    template_name = "providers/provider_detail.html"
    context_object_name = "provider"


class ProviderViewSet(viewsets.ModelViewSet):
    """
    DRF ModelViewSet for Provider.
    Provides list, create, retrieve, update, partial_update, delete.
    Supports search and ordering.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["business_name", "email"]
    ordering_fields = ["business_name", "created_at"]
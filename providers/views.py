from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Provider

# DRF imports
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProviderSerializer
from .permissions import IsProviderOwner, IsAdminOrReadOnly


# -------------------------------
# Classic Django HTML Views
# -------------------------------

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


# -------------------------------
# DRF API ViewSet
# -------------------------------

class ProviderViewSet(viewsets.ModelViewSet):
    """
    DRF API endpoints for Providers:
    - Only owners can edit/delete their own providers
    - Anyone can read (GET)
    - Filtering, search, ordering enabled
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    # Permissions
    permission_classes = [IsAuthenticated & (IsProviderOwner | IsAdminOrReadOnly)]

    # Filtering, search, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["rating"]  # exact match filter
    search_fields = ["business_name", "email", "phone"]  # partial match search
    ordering_fields = ["business_name", "created_at", "rating"]  # sortable fields
    ordering = ["id"]  # default ordering

    # Automatically assign the owner on creation
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
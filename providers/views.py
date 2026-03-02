from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Provider
from django.contrib.auth.models import User  

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProviderSerializer, UserRegistrationSerializer

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
# DRF API Views
# -------------------------------

class ProviderViewSet(viewsets.ModelViewSet):
   
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["rating"]
    search_fields = ["business_name", "email", "phone"]
    ordering_fields = ["business_name", "created_at", "rating"]
    ordering = ["id"]

    #  Show only logged-in user's providers
    def get_queryset(self):
        user = self.request.user

        # Admin can see everything
        if user.is_staff:
            return Provider.objects.all()

        # Normal users see only their own providers
        return Provider.objects.filter(owner=user)

    # Automatically assign owner
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        # Custom delete message
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {"message": "Provider deleted successfully."},
            status=status.HTTP_200_OK
        )

# -------------------------------
# User Registration API
# -------------------------------
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] 
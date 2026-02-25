from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Provider

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

class ProviderListCreateAPIView(APIView):

    def get(self, request):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProviderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProviderDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return None

    def get(self, request, pk):
        provider = self.get_object(pk)

        if not provider:
            return Response(
                {"error": "Provider not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    def put(self, request, pk):
        provider = self.get_object(pk)

        if not provider:
            return Response(
                {"error": "Provider not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProviderSerializer(provider, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        provider = self.get_object(pk)

        if not provider:
            return Response(
                {"error": "Provider not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
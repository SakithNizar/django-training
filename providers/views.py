from django.views.generic import ListView
from django.db.models import Q
from .models import Provider


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
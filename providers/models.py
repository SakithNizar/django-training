from django.db import models
from django.contrib.auth.models import User

# Custom manager for active providers
class ActiveProviderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rating__gte=1)

# Provider model
class Provider(models.Model):
    business_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    rating = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # Default manager
    active_providers = ActiveProviderManager()  # Custom manager

    def __str__(self):
        return self.business_name
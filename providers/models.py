from django.db import models

class ActiveProviderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rating__gte=1)

class Provider(models.Model):
    business_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # default
    active_providers = ActiveProviderManager()  # custom manager
    
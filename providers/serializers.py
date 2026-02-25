from rest_framework import serializers
from .models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"

    def validate_business_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Business name must be at least 3 characters."
            )
        return value
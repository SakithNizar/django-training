from django.test import TestCase
from django.contrib.auth.models import User
from providers.models import Provider

class ProviderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="Password123!")
    
    def test_provider_creation(self):
        provider = Provider.objects.create(
            business_name="Test Business",
            email="test@example.com",
            phone="1234567890",
            rating=5,
            owner=self.user
        )
        self.assertEqual(provider.owner, self.user)
        self.assertEqual(provider.rating, 5)
from django.test import TestCase
from django.contrib.auth.models import User
from providers.models import Provider
from providers.permissions import IsProviderOwner

class ProviderPermissionTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="Password123!")
        self.user2 = User.objects.create_user(username="user2", password="Password123!")
        self.provider = Provider.objects.create(
            business_name="Business1",
            email="b1@example.com",
            phone="11111111",
            rating=5,
            owner=self.user1
        )
    
    def test_is_provider_owner_permission(self):
        perm = IsProviderOwner()
        class Request:
            user = self.user1
        class Obj:
            owner = self.user1
        self.assertTrue(perm.has_object_permission(Request(), None, Obj()))
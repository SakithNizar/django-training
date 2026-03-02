from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from providers.models import Provider
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

class ProviderAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="Password123!")
        self.admin = User.objects.create_superuser(username="admin", password="AdminPass123!")
        self.client = APIClient()
        self.provider = Provider.objects.create(
            business_name="User1 Business",
            email="user1@example.com",
            phone="1234567890",
            rating=5,
            owner=self.user
        )

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_list_providers_authenticated(self):
        token = self.get_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get('/api/providers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_provider(self):
        token = self.get_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        data = {
            "business_name": "New Business",
            "email": "new@example.com",
            "phone": "0987654321",
            "rating": 4
        }
        response = self.client.post('/api/providers/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cannot_access_other_user_provider(self):
        other_user = User.objects.create_user(username="user2", password="Password123!")
        token = self.get_token(other_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.get(f'/api/providers/{self.provider.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
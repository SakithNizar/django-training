# day2_test.py
import django
import os
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "training_project.settings")
django.setup()

from providers.models import Provider
from django.db.models import Q, F

print("=== Day 2 ORM & Manager Test ===\n")

# 1️⃣ All providers
print("All Providers:")
for p in Provider.objects.all():
    print(f"- {p} | Email: {p.email} | Phone: {p.phone} | Rating: {p.rating}")
print()

# 2️⃣ Providers with 'gmail' in email
print("Providers with 'gmail' in email:")
for p in Provider.objects.filter(email__icontains="gmail"):
    print(f"- {p}")
print()

# 3️⃣ Providers created in the last 7 days
week_ago = timezone.now() - timedelta(days=7)
print("Providers created in last 7 days:")
for p in Provider.objects.filter(created_at__gte=week_ago):
    print(f"- {p}")
print()

# 4️⃣ Providers ordered by business name
print("Providers ordered by business name:")
for p in Provider.objects.order_by("business_name"):
    print(f"- {p}")
print()

# 5️⃣ Total number of providers
print(f"Total number of providers: {Provider.objects.count()}")
print()

# 6️⃣ Update a specific provider's phone using F expression
print("Updating phone for 'global@gmail.com' using F expression...")
Provider.objects.filter(email="global@gmail.com").update(phone=F("phone"))
print("Updated phone:", Provider.objects.get(email="global@gmail.com").phone)
print()

# 7️⃣ Delete a provider by email
print("Deleting provider with email 'tech@example.com'...")
Provider.objects.filter(email="tech@example.com").delete()
print("All providers after deletion:")
for p in Provider.objects.all():
    print(f"- {p}")
print()

# 8️⃣ Active providers using custom manager
print("Active providers (rating >= 1):")
for p in Provider.active_providers.all():
    print(f"- {p}")
print()

# 9️⃣ Increase rating for all providers by 1 using F expression
print("Increasing rating for all providers by 1...")
Provider.objects.update(rating=F("rating") + 1)
print("Active providers after increasing rating:")
for p in Provider.active_providers.all():
    print(f"- {p} | Rating: {p.rating}")
print("\n=== End of Day 2 Test ===")
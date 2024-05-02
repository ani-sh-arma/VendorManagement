from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from vendors.views import VendorViewSet

router = routers.DefaultRouter()
router.register(r'vendors', VendorViewSet)  # 'vendors' endpoint mapped to VendorViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the API router in the project URLs
]

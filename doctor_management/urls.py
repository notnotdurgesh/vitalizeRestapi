from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),  # Include DRF URLs
    path('api/prescriptions/', include('prescriptions.urls')),  # Include your app's URLs
]

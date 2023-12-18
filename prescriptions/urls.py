from django.urls import path
from .views import PrescriptionCreateView

urlpatterns = [
    path('create/', PrescriptionCreateView.as_view(), name='create-prescription'),
]

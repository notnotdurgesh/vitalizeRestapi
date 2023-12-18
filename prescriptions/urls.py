from django.urls import path
from .views import PrescriptionCreateView

urlpatterns = [
    path('prescriptions/', PrescriptionCreateView.as_view(), name='prescription-list-create'),
]

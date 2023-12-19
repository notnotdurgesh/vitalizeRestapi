from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Prescription
from .serializers import PrescriptionSerializer
import logging

logger = logging.getLogger(__name__)

class PrescriptionCreateView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Prescription.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f"Prescription created: {serializer.data}")

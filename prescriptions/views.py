from rest_framework import generics
from .models import Prescription
from .serializers import PrescriptionSerializer

class PrescriptionCreateView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        return Prescription.objects.all()

    def perform_create(self, serializer):
        serializer.save()


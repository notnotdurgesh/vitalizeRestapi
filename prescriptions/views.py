from rest_framework import generics
from .models import Prescription
from .serializers import PrescriptionSerializer

class PrescriptionCreateView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

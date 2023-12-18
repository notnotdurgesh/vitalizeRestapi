# prescriptions/serializers.py
from rest_framework import serializers
from .models import Prescription

class MedicineSerializer(serializers.Serializer):
    medicineName = serializers.CharField(max_length=100)
    dosage = serializers.IntegerField()
    frequency = serializers.IntegerField()

class PrescriptionSerializer(serializers.ModelSerializer):
    medicines = MedicineSerializer(many=True)
    date = serializers.SerializerMethodField()

    class Meta:
        model = Prescription
        fields = '__all__'

    def get_date(self, instance):
        return instance.formatted_date()

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
        # Add extra validation and error messages
        extra_kwargs = {
            'age': {'required': True, 'error_messages': {'required': 'Age is required.'}},
            'gender': {'required': True, 'error_messages': {'required': 'Gender is required.'}},
        }

    def get_date(self, instance):
        return instance.formatted_date()

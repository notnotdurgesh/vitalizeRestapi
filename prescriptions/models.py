from django.db import models
from django.db.models import JSONField
from datetime import datetime

class Prescription(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    username = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    date = models.DateField(null=True, blank=True)
    symptoms = JSONField()
    medicines = JSONField()

    def formatted_date(self):
        return self.date.strftime('%d-%m-%Y') if self.date else None

    def __str__(self):
        return f"{self.username}'s Prescription"
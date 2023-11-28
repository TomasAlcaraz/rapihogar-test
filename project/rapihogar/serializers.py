from rest_framework import serializers
from .models import Technician


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = ["id", "full_name", "hours_worked", "total_to_charge", "num_orders"]

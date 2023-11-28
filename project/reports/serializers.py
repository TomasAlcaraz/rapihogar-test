from rest_framework import serializers
from rapihogar.models import Technician

class ReportSerializer(serializers.Serializer):
    average_payment = serializers.FloatField()
    low_earning_technicians = serializers.ListField(child=serializers.DictField())
    lowest_earning_technician = serializers.DictField()
    highest_earning_technician = serializers.DictField()
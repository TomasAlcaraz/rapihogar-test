from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rapihogar.models import Technician
from django.db.models import Avg

# Create your views here.


class ReportView(APIView):
    def get(self, request, *args, **kwargs):
        technicians = Technician.objects.all()

        if technicians.exists():
            # Calcular el monto promedio
            average_charge = Technician.objects.aggregate(Avg("total_to_charge"))[
                "total_to_charge__avg"
            ]

             # Técnicos que cobraron menos que el promedio
            below_average_technicians = Technician.objects.filter(
                total_to_charge__lt=average_charge
            ).values("full_name", "total_to_charge")

            # Técnico que cobró el monto más bajo
            lowest_charge_technician = (
                Technician.objects.filter(total_to_charge__gt=0)
                .order_by("total_to_charge")
                .values("full_name", "total_to_charge")
                .first()
            )

            # Técnico que cobró el monto más alto
            highest_charge_technician = (
                Technician.objects.filter(total_to_charge__gt=0)
                .order_by("-total_to_charge")
                .values("full_name", "total_to_charge")
                .first()
            )
        
            context = {
                "average_charge": average_charge,
                "below_average_technicians": below_average_technicians.values(),
                "lowest_charge_technician": lowest_charge_technician,
                "highest_charge_technician": highest_charge_technician,
            }

            return render(request, "report_template.html", context)
        else:
            return Response(
                {"error": "No hay técnicos disponibles"},
                status=status.HTTP_404_NOT_FOUND,
            )

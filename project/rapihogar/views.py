from rest_framework.views import APIView
from .models import Technician
from pedidos.models import Pedido
from rest_framework import viewsets
from django.shortcuts import render
from django.db.models import Q


class TechnicianListView(APIView):
    template_name = "technician_list.html"

    def get(self, request):

        search_name = request.GET.get("search_name", "")

        technicians = Technician.objects.filter(Q(full_name__icontains=search_name))

        technician_data = []

        for technician in technicians:
            total_payment = technician.calculate_total_to_charge()
            technician_data.append(
                {
                    "id": technician.id,
                    "full_name": technician.full_name,
                    "hours_worked": technician.hours_worked,
                    "total_to_charge": total_payment,
                    "num_orders": technician.num_orders,
                }
            )

        context = {"technicians": technician_data, "search_name": search_name}
        return render(request, "technician_list.html", context=context)


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()

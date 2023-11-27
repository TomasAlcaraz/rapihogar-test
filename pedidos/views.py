from django.shortcuts import render
from django.views import View
from .models import Pedido

# Create your views here.

class PedidoListView(View):
    template_name = 'pedido_list.html'

    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.all()
        context = {'pedidos': pedidos}
        return render(request, self.template_name, context)
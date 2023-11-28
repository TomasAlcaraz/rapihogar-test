from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from .models import Pedido
from .utils.update_forms import PedidoUpdateForm


class PedidoListView(View):
    template_name = "pedido_list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        pedidos = Pedido.objects.all()
        form = PedidoUpdateForm()
        context["pedidos"] = pedidos

        return render(request, "pedido_list.html", context)


class PedidoUpdateView(View):
    template_name = "pedido_update.html"

    def get(self, request, pedido_id, *args, **kwargs):
        pedido = get_object_or_404(Pedido, id=pedido_id)
        form = PedidoUpdateForm(instance=pedido)
        context = {"pedido": pedido, "form": form}
        return render(request, self.template_name, context=context)

    def post(self, request, pedido_id, *args, **kwargs):
        pedido = get_object_or_404(Pedido, id=pedido_id)
        form = PedidoUpdateForm(request.POST, instance=pedido)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/pedidos")

        context = {"pedido": pedido, "form": form}
        return render(request, self.template_name, context=context)

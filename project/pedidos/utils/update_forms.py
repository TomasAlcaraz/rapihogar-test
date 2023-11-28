from django import forms
from pedidos.models import Pedido


class PedidoUpdateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["title", "description", "location", "status"]

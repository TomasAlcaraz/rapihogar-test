from django.urls import path
from .views import PedidoListView

app_name = 'pedidos'

urlpatterns = [
    path('', PedidoListView.as_view(), name='pedido_list'),
]
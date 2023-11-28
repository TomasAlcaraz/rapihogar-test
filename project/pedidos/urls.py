from django.urls import path
from .views import PedidoListView, PedidoUpdateView

app_name = "pedidos"

urlpatterns = [
    path("", PedidoListView.as_view(), name="pedido_list"),
    path(
        "pedido/<int:pedido_id>/update/",
        PedidoUpdateView.as_view(),
        name="pedido-update",
    ),
]

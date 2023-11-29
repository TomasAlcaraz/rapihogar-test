from django.test import TestCase, Client
from django.urls import reverse
from .models import Pedido
from rapihogar.models import Technician, User
from django.contrib.auth import get_user_model

User = get_user_model()

class PedidoViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(email="test@example.com", username="test_user")
        technician = Technician.objects.create(full_name="Técnico de Prueba")

        Pedido.objects.create(
            client=user,
            scheme=None,
            technician=technician,
            hours_worked=5,
            title="Test Pedido",
            description="Descripción de prueba",
            location="Ubicación de prueba",
            status="Pendiente",
        )

    def test_pedido_list_view(self):
        response = self.client.get(reverse("pedidos:pedido_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Pedido")
        self.assertTemplateUsed(response, "pedido_list.html")
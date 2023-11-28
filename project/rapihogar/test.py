from django.test import TestCase, Client
from django.urls import reverse
from .models import Technician
from django.contrib.auth import get_user_model

User = get_user_model()

class TechnicianViewTest(TestCase):
    def setUp(self):
        # Crear un usuario para el técnico
        self.user = User.objects.create(email="test@example.com", username="test_user")

        # Crear un técnico
        self.technician = Technician.objects.create(
            full_name="Técnico de Prueba",
            hours_worked=20, 
        )

    def test_technician_list_view(self):
        # Realizar una solicitud GET a la vista de la lista de técnicos
        response = self.client.get(reverse("technician-list"))

        # Verificar que la solicitud fue exitosa
        self.assertEqual(response.status_code, 200)

        # Verificar que la información del técnico está presente en la respuesta
        self.assertContains(response, "Técnico de Prueba")
        self.assertContains(response, "20")  

        # Verificar que se está utilizando el template correcto
        self.assertTemplateUsed(response, "technician_list.html")

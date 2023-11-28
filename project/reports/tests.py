from django.test import TestCase
from django.urls import reverse
from rapihogar.models import Technician

# Create your tests here.

class ReportViewTest(TestCase):
    def setUp(self):
        # Crea algunos técnicos para las pruebas
        Technician.objects.create(full_name="Test-Técnico1", hours_worked=20)
        Technician.objects.create(full_name="Test-Técnico2", hours_worked=20)

    def test_report_view(self):
        # Realiza una solicitud GET a la vista de informes
        response = self.client.get(reverse("reports:report_templete"))

        # Verifica que la solicitud fue exitosa
        self.assertEqual(response.status_code, 200)

        # Verifica que se está utilizando el template correcto
        self.assertTemplateUsed(response, "report_template.html")
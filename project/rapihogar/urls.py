from django.contrib import admin
from django.urls import path, include
from .views import TechnicianListView
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("api/", include("api.urls")),
    path("pedidos/", include("pedidos.urls")),
    path('technicians/', TechnicianListView.as_view(), name='technician-list'),
    path("reports/", include("reports.urls"))
]
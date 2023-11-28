from django.contrib import admin
from django.urls import path, include
from .views import TechnicianListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("pedidos/", include("pedidos.urls")),
    path('technicians/', TechnicianListView.as_view(), name='technician-list'),
]

import random
from django.core.management.base import BaseCommand
from rapihogar.models import Technician

class Command(BaseCommand):
    help = 'Crea N técnicos aleatorios'

    def add_arguments(self, parser):
        parser.add_argument('cantidad_tecnicos', type=int, help='Número de técnicos a crear')

    def handle(self, *args, **options):
        cantidad_tecnicos = options['cantidad_tecnicos']

        for _ in range(cantidad_tecnicos):
            Technician.objects.create(
                full_name=f'Técnico {_ + 1}',
                hours_worked=random.randint(0, 40),  # Ajusta según tus necesidades
            )

        self.stdout.write(self.style.SUCCESS(f'Se crearon {cantidad_tecnicos} técnicos correctamente'))
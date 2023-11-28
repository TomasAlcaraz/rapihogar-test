import random
from django.core.management.base import BaseCommand
from rapihogar.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Crea N usuarios aleatorios'

    def add_arguments(self, parser):
        parser.add_argument('cantidad_usuarios', type=int, help='Número de usuarios a crear')

    def handle(self, *args, **options):
        cantidad_usuarios = options['cantidad_usuarios']
        fake = Faker()

        for _ in range(cantidad_usuarios):
            User.objects.create(
                email=fake.email(),
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                whatsapp_phone=f'+54{random.randint(100000000, 999999999)}',
                is_active=True,
                is_staff=False,
            )

        self.stdout.write(self.style.SUCCESS(f'Se crearon {cantidad_usuarios} usuarios correctamente'))
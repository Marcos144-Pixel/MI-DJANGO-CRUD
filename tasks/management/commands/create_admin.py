from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Crea un superusuario automáticamente si no existe'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@example.com'
        password = '1234'

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'El superusuario "{username}" ya existe')
            )
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'✅ Superusuario "{username}" creado exitosamente')
            )
            self.stdout.write(f'   Username: {username}')
            self.stdout.write(f'   Password: {password}')
from django.core.management import BaseCommand
from post.models import Categoria


class Command(BaseCommand):

    def handle(self, *args, **options):
        cat = Categoria()
        cat.titulo = "titulo automatico"
        cat.descripcion = "probando"
        cat.save()
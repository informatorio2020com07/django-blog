from django.core.management import BaseCommand
from post.models import Categoria

from csv import DictReader

class Command(BaseCommand):

    def __crear_categoria(self):
        for fila in DictReader(open("./categorias.csv")):
            cat = Categoria()
            cat.titulo = fila["titulo"]
            cat.descripcion = fila["desc"]
            cat.save()

    def handle(self, *args, **options):
        self.__crear_categoria()
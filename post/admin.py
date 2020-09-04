from django.contrib import admin
from .models import Post,Categoria
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Post)
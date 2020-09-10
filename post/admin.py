from django.contrib import admin
from .models import Post,Categoria,CalificacionPost
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(CalificacionPost)
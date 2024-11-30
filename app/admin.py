from django.contrib import admin
from .models import Editorial, Articulo

# Register your models here.

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","autor","formato","descripcion"]
    list_editable = ["precio","autor","formato","descripcion"]
    search_fields = ["nombre","autor"]
    list_filter = ["autor", "formato"]
    list_per_page = 5
 
admin.site.register(Editorial)
admin.site.register(Articulo, ArticuloAdmin)
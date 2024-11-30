from django.urls import path
from .views import  home, Carrito, catalogo,favoritos,login,nosotros,novedades,producto,\
                    registro,vendidos,agregar_articulo,modificar_articulo,listar_articulo,eliminar_articulo,logout_view,\
                    registro,agregar_al_carrito,eliminar_del_carrito

urlpatterns = [
    path('', home, name="home"),
    path('carrito/', Carrito,name="carrito"),
    path('catalogo/', catalogo,name="Catalogo"),
    path('favoritos/', favoritos,name="favoritos"),
    path('nosotros/', nosotros,name="nosotros"),
    path('novedades/', novedades,name="novedades"),
    path('producto/<id>/', producto,name="producto"),
    path('vendidos/', vendidos,name="vendidos"),
    path('agregar-Articulo/',agregar_articulo,name="agregar"),
    path('listar-Articulo/',listar_articulo,name="listar"),
    path('modificar-Articulo/<id>/',modificar_articulo,name="modificar"),
    path('eliminar-Articulo/<id>/',eliminar_articulo,name="eliminar"),
    path('logout/', logout_view, name='logout'),
    path('login/', login,name="login"),
    path('registro/', registro, name="registro"),
    path('agregar/<id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
]
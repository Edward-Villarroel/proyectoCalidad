from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo, CarritoFunc
from .forms import ArticuloForm, CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.


def home(request):
    articulos = Articulo.objects.all() 
    data = {
        'articulos': articulos
    }
    return render(request, 'app/Home.html',data)

def Carrito(request):
    items_carrito = CarritoFunc.objects.filter(usuario=request.user)
    total = sum(item.articulo.precio * item.cantidad for item in items_carrito)
    
    context = {
        'items_carrito': items_carrito,
        'total': total,
    }
    
    return render(request, 'app/carrito.html', context)

def catalogo(request):
    return render(request, 'app/catalogo.html')

def favoritos(request):
    return render(request, 'app/Favoritos.html')

def login(request):
    return render(request, 'app/Login.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def novedades(request):
    return render(request, 'app/Novedades.html')

def producto(request,id):
    articulos = get_object_or_404(Articulo, pk=id)
    return render(request, 'app/producto.html', {'articulos': articulos})

def vendidos(request):
    return render(request, 'app/Vendidos.html')

@permission_required('app.add_articulo')
def agregar_articulo(request):

    data = {
            'form': ArticuloForm()
            }
    if request.method == 'POST':
        formulario = ArticuloForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        else:
            data["form"] = formulario

    return render(request, 'app/Articulo/agregar.html',data)

@permission_required('app.view_articulo')
def listar_articulo(request):

    articulos = Articulo.objects.all()

    page = request.GET.get('page',1)

    try:
        paginator = Paginator(articulos,10)
        articulos = paginator.page(page)
    except:
        raise Http404    

    data = {
        'entity': articulos,
        'paginator': paginator
    }
    return render(request, 'app/Articulo/listar.html',data)

@permission_required('app.change_articulo')
def modificar_articulo(request,id):
    
    articulo = get_object_or_404(Articulo, id=id)

    data ={
        'form': ArticuloForm(instance=articulo)
    }
    if request.method == 'POST':
        formulario = ArticuloForm(data=request.POST, instance=articulo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        data["form"] = formulario

    return render(request, 'app/Articulo/modificar.html',data)

@permission_required('app.delete_articulo')
def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    articulo.delete()
    return redirect(to="listar")

def logout_view(request): 
    logout(request)
    return redirect('home')

def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()    
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def agregar_al_carrito(request, id):
    articulo = get_object_or_404(Articulo, pk=id)

    if CarritoFunc.objects.filter(articulo=articulo, usuario=request.user).exists():
        item = CarritoFunc.objects.get(articulo=articulo, usuario=request.user)
        item.cantidad += 1
        item.save()
    else:
        item = CarritoFunc(articulo=articulo, usuario=request.user)
        item.save()
    return redirect(to="carrito")

def eliminar_del_carrito(request, id):
    item = get_object_or_404(CarritoFunc, pk=id, usuario=request.user)
    item.delete()
    return redirect(to="carrito")
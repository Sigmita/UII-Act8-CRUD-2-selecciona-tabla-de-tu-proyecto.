from django.shortcuts import render, redirect, get_object_or_404
from .models import Visualizacion

# Listar visualizaciones
def index(request):
    visualizaciones = Visualizacion.objects.all().order_by('-fecha_visualizacion') # Ordenar por fecha más reciente
    return render(request, 'listar_visualizaciones.html', {'visualizaciones': visualizaciones})

# # Ver visualización (opcional, si quisieras una vista de detalle individual)
# def ver_visualizacion(request, id_visualizacion):
#     visualizacion = get_object_or_404(Visualizacion, id=id_visualizacion)
#     return render(request, 'ver_visualizacion.html', {'visualizacion': visualizacion})

# Agregar visualización
def agregar_visualizacion(request):
    if request.method == 'POST':
        id_usuario = request.POST['id_usuario']
        id_contenido = request.POST['id_contenido']
        tipo_contenido = request.POST['tipo_contenido']
        # Para un checkbox, si está marcado, se envía 'on', si no, no se envía nada.
        # Por eso usamos .get() con un valor por defecto False, y luego comparamos con 'on'.
        completado = request.POST.get('completado', False) == 'on' 
        
        Visualizacion.objects.create(
            id_usuario=id_usuario,
            id_contenido=id_contenido,
            tipo_contenido=tipo_contenido,
            completado=completado
        )
        return redirect('inicio') # Redirigimos al nombre de URL 'inicio' de esta app
    return render(request, 'agregar_visualizacion.html')

# Editar visualización
def editar_visualizacion(request, id_visualizacion):
    visualizacion = get_object_or_404(Visualizacion, id=id_visualizacion)
    if request.method == 'POST':
        visualizacion.id_usuario = request.POST['id_usuario']
        visualizacion.id_contenido = request.POST['id_contenido']
        visualizacion.tipo_contenido = request.POST['tipo_contenido']
        visualizacion.completado = request.POST.get('completado', False) == 'on'
        visualizacion.save()
        return redirect('inicio')
    return render(request, 'editar_visualizacion.html', {'visualizacion': visualizacion})

# Borrar visualización
def borrar_visualizacion(request, id_visualizacion):
    visualizacion = get_object_or_404(Visualizacion, id=id_visualizacion)
    if request.method == 'POST':
        visualizacion.delete()
        return redirect('inicio')
    return render(request, 'borrar_visualizacion.html', {'visualizacion': visualizacion})
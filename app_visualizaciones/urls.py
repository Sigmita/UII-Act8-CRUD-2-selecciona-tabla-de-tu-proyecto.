from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'), # La página principal de la app
    # path('<int:id_visualizacion>', views.ver_visualizacion, name='ver_visualizacion'), # Opcional si quieres una vista de detalle
    path('agregar/', views.agregar_visualizacion, name='agregar_visualizacion'),
    path('editar/<int:id_visualizacion>/', views.editar_visualizacion, name='editar_visualizacion'),
    path('borrar/<int:id_visualizacion>/', views.borrar_visualizacion, name='borrar_visualizacion'),
]
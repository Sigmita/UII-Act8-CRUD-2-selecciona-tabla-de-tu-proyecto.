from django.db import models

class Visualizacion(models.Model):
    # id_visualizacion se crea automáticamente como el Primary Key si no lo especificas.
    # Si quieres un campo explícito con ese nombre, puedes hacerlo así:
    # id_visualizacion = models.AutoField(primary_key=True) 

    id_usuario = models.IntegerField() # ID del usuario que realizó la visualización
    id_contenido = models.IntegerField() # ID del contenido (película, serie)
    tipo_contenido = models.CharField(max_length=50) # Por ejemplo: 'pelicula', 'serie', 'documental'
    fecha_visualizacion = models.DateTimeField(auto_now_add=True) # Registra la fecha/hora de creación automáticamente
    completado = models.BooleanField(default=False) # True si se vio completo, False si no

    def __str__(self):
        return f'Visualización ID: {self.id} | Usuario: {self.id_usuario} | Contenido: {self.id_contenido} | Fecha: {self.fecha_visualizacion.strftime("%Y-%m-%d %H:%M")} | Completado: {self.completado}'

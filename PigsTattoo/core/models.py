from django.db import models
# Create your models here.

class Tatuador(models.Model):
    idTatuador = models.IntegerField(primary_key=True,verbose_name='ID del tatuador')
    nombreTatuador = models.CharField(max_length=50,verbose_name='Nombre del tatuador')
    estiloTatuador = models.CharField(max_length=50,verbose_name='Estilo del tauador')
    def __str__(self):
        return self.nombreTatuador

class Diseño(models.Model):
    idDiseño = models.CharField(primary_key=True,max_length=7,verbose_name='ID del diseño')
    nombreDiseño = models.CharField(max_length=20,verbose_name='Nombre del Diseño')
    categoria = models.CharField(max_length=20,verbose_name='Categoria del diseño')
    tatuador = models.ForeignKey(Tatuador,on_delete=models.CASCADE)

    def __str__(self):
        return self.idDiseño
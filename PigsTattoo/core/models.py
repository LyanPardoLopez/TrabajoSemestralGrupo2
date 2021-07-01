from django.db import models
# Create your models here.

class Tatuador(models.Model):
    idTatuador = models.IntegerField(primary_key=True,verbose_name='ID del tatuador')
    nombreTatuador = models.CharField(max_length=50,verbose_name='Nombre del tatuador')
    estiloTatuador = models.CharField(max_length=50,verbose_name='Estilo del tauador')
    edadTatuador =models.IntegerField(null=True)
    numTatuador=models.IntegerField(null=True)
    emailTatuador=models.CharField(max_length=20,verbose_name='Email del tatuador', null=True)
    imagen = models.ImageField(upload_to='catalogo_tatuador', null=True)
    def __str__(self):
        return self.nombreTatuador

class Diseno(models.Model):
    idDiseno = models.CharField(primary_key=True,max_length=7,verbose_name='ID del diseño')
    nombreDiseno = models.CharField(max_length=20,verbose_name='Nombre del Diseño')
    categoria = models.CharField(max_length=20,verbose_name='Categoria del diseño')
    tatuador = models.ForeignKey(Tatuador,on_delete=models.CASCADE)
    imgdiseno = models.ImageField(upload_to='catalogo_diseno', null=True)
    def __str__(self):
        return self.idDiseno
        
class Register(models.Model):
    nombreuser = models.CharField(verbose_name='nombre del user', max_length=30)
    apellidouser = models.CharField(verbose_name='apellido del user', max_length=30)
    emailuser = models.CharField(verbose_name='email del user', max_length=30)
    contrauser = models.CharField(verbose_name='contraseña del user',max_length=30)
    def __str__(self):
        return self.nombreuser
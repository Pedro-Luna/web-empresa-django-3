from django.db import models
# la clase de la hora
from django.utils.timezone import now
# import del modelo de usuarios
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nombre')
    created = models.DateField(auto_now_add=True ,verbose_name='Fecha de creación')
    updated = models.DateField(auto_now=True ,verbose_name='Fecha de edición')

    class Meta:
        verbose_name ='categoria'
        verbose_name_plural ='categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateField(verbose_name='Fecha de Publicacion', default=now)
    image = models.ImageField(verbose_name='Imgen', upload_to='blog', blank=True)
   # video = models.Video
    #videofile= models.FileField(upload_to='blog', null=True, verbose_name="Video")
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categoria', related_name="get_post")
    created = models.DateField(auto_now_add=True ,verbose_name='Fecha de creación')
    updated = models.DateField(auto_now=True ,verbose_name='Fecha de edición')


    class Meta:
        verbose_name ='entrada'
        verbose_name_plural ='entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title
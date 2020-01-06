from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','created','updated')
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    # mostrar campos de modificaion, pero no su puede modificar   
    readonly_fields = ('created','updated')
    # mostrar nombre de bd
    list_display = ('title','author','published','pos_categories')
    #ordenar los registros 
    ordering = ('author','published')
    # campo de busqueda
    search_fields = ('title','author__username','categories__name')
    # navegar entre las fechas
    date_hierarchy = 'published'
    # filtrar datos 
    list_filter = ('author__username','categories__name',)
    #paginator 

    def pos_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    # cambiar el nombre
    pos_categories.short_description = 'Categorias'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
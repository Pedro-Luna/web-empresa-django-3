from django.urls import path
from . import views
#from .forms import VideoForm
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    #paths de blog
    path('',views.blog, name='blog'),
    path('category/<int:catagory_id>/',views.category, name='category'),


]

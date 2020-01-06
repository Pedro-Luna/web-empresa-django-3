from django.urls import path
from . import views

urlpatterns = [
    #paths de blog
    path('<int:page_id>/',views.page, name='page'),


]

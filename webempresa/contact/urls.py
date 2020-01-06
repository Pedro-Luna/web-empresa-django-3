from django.urls import path
from . import views

urlpatterns = [
    #paths de core
    path('',views.contact , name='contact'),

]

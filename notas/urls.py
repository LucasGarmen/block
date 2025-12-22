from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('eliminar/<int:id>',views.eliminar_nota, name='eliminar_nota'),
    path('editar/<int:id>',views.editar_nota, name='editar_nota'),
]
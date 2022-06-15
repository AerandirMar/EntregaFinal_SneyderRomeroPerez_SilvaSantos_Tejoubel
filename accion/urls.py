from django.urls import path
from accion import views


app_name='accion'
urlpatterns = [
    path('accions', views.accions, name='accion-list'),
    path('accion-django-forms', views.accion_forms_django, name='AccionDjangoForms'),
    path('search', views.search, name='Search'),
    path('accion/<int:pk>/update', views.accion_actualiza, name='accion-update'),
    path('accion/<int:pk>/delete', views.borrar_accion, name='accion-delete'),
]   
    

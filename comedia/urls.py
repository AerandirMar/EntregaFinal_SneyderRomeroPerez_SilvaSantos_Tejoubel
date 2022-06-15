from django.urls import path
from comedia import views


app_name='comedia'
urlpatterns = [
    path('comedias', views.comedias, name='comedia-list'),
    path('comedia-django-forms', views.comedia_forms_django, name='ComediaDjangoForms'),
    path('searchCom', views.searchCom, name='SearchCom'),
    path('comedia/<int:pk>/update', views.comedia_actualiza, name='comedia-update'),
    path('comedia/<int:pk>/delete', views.borrar_comedia, name='comedia-delete'),
]   

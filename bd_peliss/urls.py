from django.urls import path
from bd_peliss import views


urlpatterns = [
    #Vistas/URLS
    path('', views.index, name='Home'), 
    path('accions', views.accions, name='Accions'),
    path('terrors', views.terrors, name='Terrors'),
    path('comedias', views.comedias, name='Comedias'),
    path('sci-fi', views.cienciaFiccions, name='CienciaFiccions'),
    #Formulario
    path('formHTML', views.form_hmtl),
    #Vistas para adición de películas por género
    path('accion-django-forms', views.accion_forms_django, name='AccionDjangoForms'),
    path('comedia-django-forms', views.comedia_forms_django, name='ComediaDjangoForms'),
    path('scifi-django-forms', views.cienciaFiccion_forms_django, name='CienciaFiccionDjangoForms'),
    path('terror-django-forms', views.terror_forms_django, name='TerrorDjangoForms'),
    #Vistas para búsqueda de películas por género, nombre y fecha de estreno
    path('search', views.search, name='Search'),
    path('searchTer', views.searchTer, name='SearchTer'),
    path('searchCom', views.searchCom, name='SearchCom'),
    path('searchSci', views.searchSci, name='SearchSci'),
    #Detalle de los integrantes del grupo
    path('nosotros', views.nosotros, name='Nosotros'),
    path('contacto', views.contacto, name='Contacto'),
    #path('searchProf', views.searchProf, name='SearchProf'),
]

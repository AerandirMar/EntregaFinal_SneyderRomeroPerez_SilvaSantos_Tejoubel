from django.urls import path
from terror import views


app_name='terror'
urlpatterns = [
    path('terrors', views.terrors, name='terror-list'),
    path('terror-django-forms', views.terror_forms_django, name='TerrorDjangoForms'),
    path('searchTer', views.searchTer, name='SearchTer'),
    path('terror/<int:pk>/update', views.terror_actualiza, name='terror-update'),
    path('terror/<int:pk>/delete', views.borrar_terror, name='terror-delete'),
]    
from django.urls import path
from drama import views


app_name='drama'
urlpatterns = [
    path('dramas', views.drama, name='drama-list'),
    path('drama-django-forms', views.drama_forms_django, name='DramaDjangoForms'),
    path('searchDra', views.searchDra, name='SearchDra'),
    path('drama/<int:pk>/update', views.drama_actualiza, name='drama-update'),
    path('drama/<int:pk>/delete', views.borrar_drama, name='drama-delete'),
]

from django.contrib import admin
from django.urls import path
from HArcherApp.views import all_results, new_training, edit_training, delete_training, all_statistics, plots

urlpatterns = [
    path('treningi/', all_results, name= 'Moje_treningi'),
    path('nowy/', new_training, name= 'Dodaj_trening'),
    path('edytuj/<int:id>/', edit_training, name= 'Edytuj_trening'),
    path('usun/<int:id>/', delete_training, name= 'Usuń_trening'),
    path('statystyki/<int:id>/', all_statistics, name= 'Pokaz_statystyki'),
    path('wykresy/', plots, name= 'Pokaz_wykresy'),
]

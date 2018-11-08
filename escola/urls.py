from django.urls import path
from escola import*


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('disciplina/', views.disciplina, name='disciplina'),
    path('lstcursos/', views.cursos, name='cursos'),
    path('noticias/', views.noticias, name='noticias'),
]
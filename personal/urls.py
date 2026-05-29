from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('project/', views.project),
    path('contact/', views.contact),
    path('projects/', views.projects, name='projects'),
]
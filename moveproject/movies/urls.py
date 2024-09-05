from django.urls import path
from . import views

urlpatterns = [
    
    path('create/', views.create_movie, name='create_movie'),
    path('', views.view_movie, name='view_movies'),
    path('edit/<int:pk>/', views.edit_movie, name='edit_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),
   
]

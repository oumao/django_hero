from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.index, name='index'),
    path('delete/', views.delete, name='delete'),
]

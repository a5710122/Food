from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('add_food', views.add_food, name='add_food'),
   path('delete_food', views.delete_food, name='delete_food'),
   path('config_food', views.config_food, name='config_food'),
]

from . import views
from django.urls import path


urlpatterns = [
   
    path('',views.index),
    path('AddItem/',views.AddItem),
    path('DeleteItem/<int:todo_list>/',views.DeleteItem),
]

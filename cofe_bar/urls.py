from django.urls import path
from cofe_bar import views

urlpatterns = [
   
    path('reviews/', views.Reviews, name="reviews"), 
    path('register/', views.Register, name="cofe_bar_register")
]

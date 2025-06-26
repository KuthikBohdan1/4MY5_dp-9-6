from django.urls import path
from cofe_bar import views

urlpatterns = [
    
    path('', views.Reviews, name="reviews"), 
    path('register/', views.Register, name="cofe_bar_register"),
    path('add_review/', views.Add_review, name="add_review"),
]

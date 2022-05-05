from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('formulaire1/', views.formulaire1),
    path('formulaire2/', views.formulaire2),
    path('recup1/',views.recup1),
    path('recup2/',views.recup2),
]

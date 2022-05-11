from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('formulaire1/', views.formulaire1),
    path('formulaire2/', views.formulaire2),
    path('recup1/',views.recup1),
    path('recup2/',views.recup2),
    path('affiche/<int:id>/',views.affiche),
    path('affiche2/<int:id>/',views.affiche2),
    path('update/<int:id>/',views.update),
    path('updatetraitement/<int:id>/',views.updatetraitement),
    path('update2/<int:id>/',views.update2),
    path('updatetraitement2/<int:id>/',views.updatetraitement2),
    path('delete1/<int:id>/',views.delete1),
    path('delete2/<int:id>/',views.delete2),
]

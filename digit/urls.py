from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_j, name='index_j'),
    path('dnn/', views.index, name='index'),
    path('cnn/', views.index_cnn, name='index_cnn'),
]

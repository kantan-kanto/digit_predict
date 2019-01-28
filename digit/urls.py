from django.urls import path
from . import views

urlpatterns = [
    path('dnn/', views.index, name='index'),
    path('cnn/', views.index_cnn, name='index_cnn'),
]

"""
completely made by me.

"""
from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='home'), #this is the home pg for blog app
    path('blog/<int:pk>/', views.Read, name='read'), # to navigate via pk
    path('create/', views.Create, name='create'),
    path('update/<int:pk>/', views.Update, name='update'),
    path('delete/<int:pk>/', views.Delete, name='delete'),
]

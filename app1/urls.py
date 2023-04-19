from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'users'),
    path('add/', views.add),
    path('update/<str:email>/', views.update),
    path('delete/<str:email>/', views.delete),
]
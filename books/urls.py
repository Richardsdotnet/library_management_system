from django.urls import path

from books import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('read/', views.read),
    path('borrow/', views.borrow)
]
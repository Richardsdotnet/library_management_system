from django.urls import path

from books import views

urlpatterns = [
    path('books/', views.book_list),
    path('book/<int:pk>', views.book_details),
    path('author/', views.author_list),
    path('author/<int:pk>', views.author_details)

]
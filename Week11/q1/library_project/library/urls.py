from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.add_author, name='add_author'),
    path('publisher/', views.add_publisher, name='add_publisher'),
    path('book/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),
]
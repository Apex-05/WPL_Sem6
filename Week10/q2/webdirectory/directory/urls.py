from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-work/', views.add_work, name='add_work'),
    path('search-company/', views.search_company, name='search_company'),
]
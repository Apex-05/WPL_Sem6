from django.urls import path
from . import views

urlpatterns = [
    path('', views.square_view, name='square'),
]
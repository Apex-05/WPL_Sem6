from django.urls import path
from . import views

urlpatterns = [
    path('human/', views.human_manage, name='human_manage'),
    path('human/details/<int:human_id>/', views.get_human_details, name='get_human_details'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Primary names used in common exam statements
    path('suggestions/', views.add_entry, name='suggestions'),
    path('viewsuggestions/', views.display, name='viewsuggestions'),

    path('detail/<int:id>/', views.detail, name='detail'),
    path('final/', views.final_page, name='final'),
]

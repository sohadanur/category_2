from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list'),  # For GET all and POST
    path('categories/<int:pk>/', CategoryView.as_view(), name='category-detail'),  # For GET, PUT, DELETE
]

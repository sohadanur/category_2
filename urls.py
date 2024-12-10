from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list'),  # For GET all and POST
    #path('categories/<int:pk>/', CategoryView.as_view(), name='category-detail'),  # For GET, PUT, DELETE
    path('categories/', CategoryView.as_view(), name='category-list'),  # For GET all
    path('categories/create/', CategoryView.as_view(), name='category-create'),  # For POST
    path('categories/<int:pk>/', CategoryView.as_view(), name='category-detail'),  # For GET by ID
    path('categories/<int:pk>/edit/', CategoryView.as_view(), name='category-update-delete'),  # For PUT/DELETE
]

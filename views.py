from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer


class CategoryView(APIView):
    def get(self, request, pk=None):
        if pk:
            # Retrieve a single category by ID
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category)
                return Response({
                    "success": True,
                    "message": "Category retrieved successfully",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({
                    "success": False,
                    "message": "Category not found",
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            # Retrieve all categories
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({
                "success": True,
                "message": "List of all categories",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new category
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({
                "success": True,
                "message": "Category created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": "Validation failed",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Update an existing category
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({
                "success": False,
                "message": "Category not found",
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response({
                "success": True,
                "message": "Category updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "success": False,
            "message": "Validation failed",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete an existing category
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({
                "success": True,
                "message": "Category deleted successfully",
            }, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({
                "success": False,
                "message": "Category not found",
            }, status=status.HTTP_404_NOT_FOUND)

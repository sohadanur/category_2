from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()  # Displays the email of the creator

    class Meta:
        model = Category
        fields = [
            'category_id',
            'category_title',
            'created_at',
            'updated_at',
            'created_by',
        ]

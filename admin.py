from django.contrib import admin
# Register your models here.
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('category_title', 'created_by__email')
    list_filter = ('created_at', 'updated_at')

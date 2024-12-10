from django.db import models
from authentication.models import User  # Import User model from the authentication app

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=255, null=False)
    created_by = models.ForeignKey(
        User, related_name="categories", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_title

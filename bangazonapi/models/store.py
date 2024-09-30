from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey('Customer', on_delete=models.CASCADE)  # Linking to Customer

    # Use reverse relationship in views to access products

from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey('Customer', on_delete=models.CASCADE)  # Linking to Customer

    # Define a many-to-many relationship through a separate table
    products = models.ManyToManyField('Product', through='StoreProduct', related_name='stores')

class StoreProduct(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    # Additional fields if needed
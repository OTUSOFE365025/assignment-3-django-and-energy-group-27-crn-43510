# Defines database tables used by the project.

import sys
from django.db import models

# Product model for Cash Register App
class Product(models.Model):
    upc = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} (${self.price})"

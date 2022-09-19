from django.db import models

class Product(models.Model):
    """
    Class to represent Product database model
    """
    PRODUCTS_CATEGORIES = [
        (1, 'Others'),
        (2, 'Skateboards'),
        (3, 'Bags'),
        (4, 'Caps')
        ]

    sku = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    release_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=25,
        choices=PRODUCTS_CATEGORIES,
        blank=False, default=1
        )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True)

    class Meta:
        """
        Class to show newest product first
        """
        ordering = ['-release_date']
    
    def __str__(self):
        return str(self.sku)

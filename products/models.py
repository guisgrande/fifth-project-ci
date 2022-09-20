from django.db import models


class Category(models.Model):
    category_sku = models.SmallAutoField(primary_key=True)
    system_name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.system_name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    """
    Class to represent Product database model
    """
    sku = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    release_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
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

from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    """
    Class to represent Category database model
    """
    category_sku = models.SmallAutoField(primary_key=True)
    system_name = models.CharField(max_length=254,)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.system_name

    def get_display_name(self):
        return self.display_name


class Offer(models.Model):
    """
    Class to represent Offer database model
    """
    offer_sku = models.SmallAutoField(primary_key=True)
    offer_name = models.CharField(max_length=50,)
    offer_display = models.CharField(max_length=254, null=True, blank=True)
    offer_discount = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(80),
            MinValueValidator(0)
        ])

    def __str__(self):
        return str(self.offer_sku)
   
    def get_offer_name(self):
        return self.offer_name

    def get_offer_discount(self):
        return self.offer_discount


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
    offer_active = models.BooleanField(default=False)
    offer = models.ForeignKey(Offer, null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True)
    product_image_url = models.URLField(max_length=1024, null=True, blank=True)
    slug = models.SlugField(max_length=254, null=True, blank=True, unique=True)

    class Meta:
        """
        Class to show newest product first
        """
        ordering = ['-release_date']
    
    def __str__(self):
        return str(self.sku)
    
    def save(self, *args, **kwargs):
        """
        Function to auto generate slugfield
        """
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def cal_discount_price(self):
        return self.price - ((self.price * self.offer.offer_discount) / 100)

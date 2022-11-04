from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    """
    Class to represent Category database model
    """
    category_sku = models.SmallAutoField(primary_key=True)
    system_name = models.CharField(max_length=254,)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.display_name

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
        return str(self.offer_display)

    def get_offer_name(self):
        return self.offer_name

    def get_offer_display(self):
        return self.offer_display

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
    quantity_available = models.IntegerField(default=100,
            validators=[
            MinValueValidator(0)
        ])
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    offer = models.ForeignKey(Offer, null=True, blank=True, on_delete=models.SET_NULL)
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


class ReviewProduct(models.Model):
    """
    Class model to review a product.
    """
    REVIEW_VALUE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_review"
        )
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_review"
        )
    created_on = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)
    review = models.IntegerField(choices=REVIEW_VALUE, default=5)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return str(self.product)

import uuid
import datetime

from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


class NewsLetterList(models.Model):
    """
    Class to represent News Letter E-mails list database model
    """
    news_email = models.EmailField(max_length=70, blank=False, unique=True)
    news_name = models.CharField(max_length=70)
    news_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_email


class NewsLetterMail(models.Model):
    """
    Class for News Letter Mail database model
    """
    news_number = models.SmallAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    email = models.ManyToManyField(NewsLetterList)
    subject = models.CharField(max_length=70)
    body = models.TextField(max_length=1000)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return str(self.news_number)


class Coupon(models.Model):
    """
    Class for Coupon database model
    Unique coupon for single use
    """
    coupon = models.CharField(max_length=36, unique=True, null=False, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True, editable=False)
    date_end = models.DateTimeField(null=True, blank=True)
    discount = models.IntegerField(default=10)
    used = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return str(self.coupon)

    def _generate_coupon(self):
        """
        Generate a random, unique coupon code using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method 
        To set the coupon number, and dates.
        """
        if not self.coupon:
            self.coupon = 'CPN' + self._generate_coupon()
            self.coupon = self.coupon[:14]

        if not self.date_start:
            self.date_start = datetime.datetime.now()

        if not self.date_end:
            self.date_end = self.date_start + datetime.timedelta(days=2)

        super().save(*args, **kwargs)

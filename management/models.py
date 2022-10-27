from django.db import models


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

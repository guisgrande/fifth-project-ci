from django.contrib import admin
from .models import NewsLetterList, NewsLetterMail


@admin.register(NewsLetterList)
class NewsLetterListAdmin(admin.ModelAdmin):
    list_display = ('news_email', 'news_name', 'news_date')
    search_fields = ('news_email', 'news_name')


@admin.register(NewsLetterMail)
class NewsLetterMailAdmin(admin.ModelAdmin):
    list_display = ('news_number', 'created', 'subject', 'status')
    search_fields = ('news_number', 'subject')

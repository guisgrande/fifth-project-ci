# Generated by Django 3.2 on 2022-10-27 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterMail',
            fields=[
                ('news_number', models.SmallAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=70)),
                ('body', models.TextField(max_length=1000)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('email', models.ManyToManyField(to='management.NewsLetterList')),
            ],
        ),
    ]
# Generated by Django 3.2.24 on 2024-03-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
    ]
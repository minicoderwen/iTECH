# Generated by Django 3.2.24 on 2024-03-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_blog_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="slug",
            field=models.SlugField(default="", unique=True),
            preserve_default=False,
        ),
    ]

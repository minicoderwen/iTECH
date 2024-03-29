# Generated by Django 3.2.24 on 2024-03-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='reset_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='reset_token_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-23 13:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='follow',
            field=models.ManyToManyField(related_name='followee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-25 02:13

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_tweet_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='disp',
            field=models.ImageField(blank=True, upload_to='', verbose_name=accounts.models.Profile),
        ),
    ]

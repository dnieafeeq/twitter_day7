# Generated by Django 3.2.4 on 2021-06-25 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_tweet_disp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='disp',
        ),
    ]

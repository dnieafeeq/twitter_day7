# Generated by Django 3.2.4 on 2021-06-24 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='author',
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-05 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_new_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='address',
        ),
    ]

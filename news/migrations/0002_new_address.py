# Generated by Django 4.2.1 on 2023-05-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='address',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='Адрес'),
        ),
    ]

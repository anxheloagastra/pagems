# Generated by Django 4.2.7 on 2023-12-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]

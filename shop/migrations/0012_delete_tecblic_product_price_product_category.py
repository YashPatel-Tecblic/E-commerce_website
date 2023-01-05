# Generated by Django 4.1.4 on 2022-12-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tecblic',
        ),
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=60),
        ),
    ]
# Generated by Django 4.0 on 2022-08-06 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='published_date',
            new_name='premier',
        ),
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.PositiveSmallIntegerField(default=2022, verbose_name='Год выхода'),
        ),
        migrations.AlterField(
            model_name='product',
            name='poster',
            field=models.ImageField(upload_to='product/', verbose_name='Постер'),
        ),
    ]

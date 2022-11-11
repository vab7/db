# Generated by Django 4.1.3 on 2022-11-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, to='bank.size', verbose_name='Размер'),
        ),
    ]

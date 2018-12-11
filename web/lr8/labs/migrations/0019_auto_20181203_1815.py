# Generated by Django 2.1.3 on 2018-12-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0018_auto_20181203_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('Бесплатная', 'Бесплатная'), ('Быстрая', 'Быстрая')], max_length=20, verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='disk',
            field=models.CharField(choices=[('DVD', 'DVD'), ('CD', 'CD')], max_length=3, verbose_name='Диск'),
        ),
    ]

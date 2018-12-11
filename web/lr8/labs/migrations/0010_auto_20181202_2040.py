# Generated by Django 2.1.3 on 2018-12-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0009_auto_20181202_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.CharField(choices=[('Курсу по Фотошопу', 'Курсу по Фотошопу'), ('Курсы по PHP', 'Курсы по PHP'), ('Курсы по Adobe Dreamweawer', 'Курсы по Adobe Dreamweawer')], max_length=30, verbose_name='Курсы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='disk',
            field=models.CharField(choices=[('CD', 'CD'), ('DVD', 'DVD')], max_length=3, verbose_name='Диск'),
        ),
    ]

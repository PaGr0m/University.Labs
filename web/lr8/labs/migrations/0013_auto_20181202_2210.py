# Generated by Django 2.1.3 on 2018-12-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0012_auto_20181202_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.CharField(choices=[('Курсы по Adobe Dreamweawer', 'Курсы по Adobe Dreamweawer'), ('Курсу по Фотошопу', 'Курсу по Фотошопу'), ('Курсы по PHP', 'Курсы по PHP')], max_length=30, verbose_name='Курсы'),
        ),
    ]
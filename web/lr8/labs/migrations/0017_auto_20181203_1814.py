# Generated by Django 2.1.3 on 2018-12-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0016_auto_20181203_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regexpmodel',
            name='form_7',
        ),
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.CharField(choices=[('Курсы по Adobe Dreamweawer', 'Курсы по Adobe Dreamweawer'), ('Курсу по Фотошопу', 'Курсу по Фотошопу'), ('Курсы по PHP', 'Курсы по PHP')], max_length=30, verbose_name='Курсы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('Бесплатная', 'Бесплатная'), ('Быстрая', 'Быстрая')], max_length=20, verbose_name='Способ доставки'),
        ),
    ]

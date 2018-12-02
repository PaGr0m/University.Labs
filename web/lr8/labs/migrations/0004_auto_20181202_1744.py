# Generated by Django 2.1.3 on 2018-12-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0003_auto_20181202_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='url_height',
            field=models.PositiveIntegerField(default='200'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='url_width',
            field=models.PositiveIntegerField(default='400'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, height_field='url_height', upload_to='images/', width_field='url_width'),
        ),
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.CharField(choices=[('Курсы по Adobe Dreamweawer', 'Курсы по Adobe Dreamweawer'), ('Курсы по PHP', 'Курсы по PHP'), ('Курсу по Фотошопу', 'Курсу по Фотошопу')], max_length=30, verbose_name='Курсы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('Быстрая', 'Быстрая'), ('Бесплатная', 'Бесплатная')], max_length=20, verbose_name='Способ доставки'),
        ),
    ]
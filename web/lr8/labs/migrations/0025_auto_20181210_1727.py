# Generated by Django 2.1.3 on 2018-12-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0024_auto_20181210_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfile', models.ImageField(upload_to='images/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('Бесплатная', 'Бесплатная'), ('Быстрая', 'Быстрая')], max_length=20, verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='disk',
            field=models.CharField(choices=[('CD', 'CD'), ('DVD', 'DVD')], max_length=3, verbose_name='Диск'),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discography', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_file',
            field=models.FileField(default='1', upload_to='', verbose_name='Файл музыки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('Rock', 'Rock'), ('Rap', 'Rap'), ('Classical music', 'Classical music'), ('Electonic music', 'Electonic music')], max_length=25, verbose_name='Жанр'),
        ),
    ]
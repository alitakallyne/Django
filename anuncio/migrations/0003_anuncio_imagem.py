# Generated by Django 2.1 on 2018-11-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0002_auto_20181116_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(default=0, upload_to='', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]

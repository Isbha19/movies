# Generated by Django 4.1.3 on 2022-11-17 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(default='daffd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]

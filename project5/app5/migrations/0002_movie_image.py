# Generated by Django 3.2.12 on 2022-03-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='kim', upload_to='pics'),
            preserve_default=False,
        ),
    ]

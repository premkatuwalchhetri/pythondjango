# Generated by Django 5.1.1 on 2024-10-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(upload_to='rooms/image'),
        ),
    ]
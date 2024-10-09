# Generated by Django 5.1.1 on 2024-10-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_alter_room_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('guests', models.IntegerField()),
                ('room_id', models.IntegerField()),
            ],
        ),
    ]

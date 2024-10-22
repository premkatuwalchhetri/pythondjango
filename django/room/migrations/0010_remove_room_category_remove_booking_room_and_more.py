# Generated by Django 5.1.1 on 2024-10-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_category_remove_booking_room_id_booking_room_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='category',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.AddField(
            model_name='booking',
            name='room_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

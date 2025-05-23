# Generated by Django 5.1.1 on 2024-10-22 14:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='room_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='room.room'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='room.category'),
            preserve_default=False,
        ),
    ]

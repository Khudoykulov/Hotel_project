# Generated by Django 5.0.2 on 2024-02-15 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_room_bed_room_image_room_max_persion_room_size_a_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='max_persion',
            new_name='max_person',
        ),
        migrations.RemoveField(
            model_name='room',
            name='adults',
        ),
        migrations.RemoveField(
            model_name='room',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='room',
            name='check_out',
        ),
        migrations.RemoveField(
            model_name='room',
            name='children',
        ),
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='rooms/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_image', to='rooms.room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

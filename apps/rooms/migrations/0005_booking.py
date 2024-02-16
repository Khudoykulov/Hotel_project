# Generated by Django 5.0.2 on 2024-02-16 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_room_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
                ('price_min', models.IntegerField(default=0)),
                ('price_max', models.IntegerField()),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='rooms.room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

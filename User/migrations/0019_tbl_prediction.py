# Generated by Django 5.0.4 on 2024-04-18 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0019_tbl_user'),
        ('User', '0018_delete_tbl_prediction'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nitrogen', models.FloatField(max_length=100)),
                ('Phosphorus', models.FloatField(max_length=100)),
                ('Potassium', models.FloatField(max_length=100)),
                ('Temprature', models.FloatField(max_length=100)),
                ('Humidity', models.FloatField(max_length=100)),
                ('Ph', models.FloatField(max_length=100)),
                ('Rainfall', models.FloatField(max_length=100)),
                ('prediction_result', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]

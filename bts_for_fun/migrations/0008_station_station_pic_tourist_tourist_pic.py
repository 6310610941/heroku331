# Generated by Django 4.1 on 2022-11-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bts_for_fun', '0007_station_stt_pic_delete_stationdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='station_pic',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='tourist',
            name='tourist_pic',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]

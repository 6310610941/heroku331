# Generated by Django 4.1 on 2022-11-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bts_for_fun', '0006_tourist_t_pic_delete_touristdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='stt_pic',
            field=models.ImageField(blank=True, upload_to='static/stationpic/'),
        ),
        migrations.DeleteModel(
            name='Stationdetail',
        ),
    ]

# Generated by Django 4.1 on 2022-11-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bts_for_fun', '0005_alter_touristdetail_t_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourist',
            name='t_pic',
            field=models.ImageField(blank=True, upload_to='static/touristpic/'),
        ),
        migrations.DeleteModel(
            name='Touristdetail',
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_alter_album_albumlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumlocation',
            field=models.CharField(blank=True, default='(37.554357189598775, 126.97063477079135)', max_length=50, verbose_name='앨범위치'),
        ),
    ]

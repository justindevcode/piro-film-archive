# Generated by Django 4.0.6 on 2022-08-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framesharings', '0002_alter_frame_framephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='framelikedate',
            field=models.TextField(null=True, verbose_name='프레임메모'),
        ),
    ]
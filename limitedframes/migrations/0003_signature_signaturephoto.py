# Generated by Django 4.0.6 on 2022-08-08 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limitedframes', '0002_remove_signature_signaturephoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='signaturephoto',
            field=models.URLField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2022-05-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0006_alter_file_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='doctor_id',
            field=models.UUIDField(default=None),
        ),
        migrations.AddField(
            model_name='file',
            name='patient_id',
            field=models.UUIDField(default=None),
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileHash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.UUIDField()),
                ('patient_id', models.UUIDField()),
                ('tx_hash', models.CharField(max_length=256)),
            ],
        ),
    ]
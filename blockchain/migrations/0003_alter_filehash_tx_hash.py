# Generated by Django 3.2.9 on 2022-05-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0002_alter_filehash_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filehash',
            name='tx_hash',
            field=models.TextField(),
        ),
    ]
# Generated by Django 3.2.9 on 2022-05-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0011_remove_filehash_file_ipfs_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='filehash',
            name='file_ipfs_hash',
            field=models.TextField(null=True),
        ),
    ]
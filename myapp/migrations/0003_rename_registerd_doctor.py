# Generated by Django 4.1.2 on 2022-12-15 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_registerd_rename_name_register_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registerD',
            new_name='Doctor',
        ),
    ]

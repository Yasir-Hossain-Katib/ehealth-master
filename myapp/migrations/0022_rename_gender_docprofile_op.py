# Generated by Django 4.1.2 on 2022-12-18 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_payment_op'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docprofile',
            old_name='gender',
            new_name='op',
        ),
    ]

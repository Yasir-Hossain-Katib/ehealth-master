# Generated by Django 4.1.2 on 2022-12-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='exp',
            field=models.TextField(),
        ),
    ]

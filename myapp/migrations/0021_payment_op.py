# Generated by Django 4.1.2 on 2022-12-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_feedback_exp'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='op',
            field=models.CharField(default=85, max_length=100),
            preserve_default=False,
        ),
    ]

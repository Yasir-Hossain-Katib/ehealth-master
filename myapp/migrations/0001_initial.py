# Generated by Django 4.1.2 on 2022-12-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='username')),
                ('email', models.CharField(max_length=200, verbose_name='email')),
                ('password1', models.CharField(max_length=128, verbose_name='password1')),
                ('password2', models.CharField(max_length=128, verbose_name='password2')),
            ],
        ),
    ]

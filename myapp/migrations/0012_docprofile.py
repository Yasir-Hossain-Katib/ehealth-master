# Generated by Django 4.1.2 on 2022-12-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_delete_doc_delete_hj_alter_doctor_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
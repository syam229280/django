# Generated by Django 2.2.1 on 2019-05-04 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='created_on',
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0005_auto_20190504_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.FloatField(),
        ),
    ]

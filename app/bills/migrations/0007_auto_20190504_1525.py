# Generated by Django 2.2.1 on 2019-05-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0006_auto_20190504_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_file',
            field=models.FileField(blank=True, max_length=500, upload_to='uploads/%Y/%m/'),
        ),
    ]

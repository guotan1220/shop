# Generated by Django 4.2.6 on 2023-10-18 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zishop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bpages',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-22 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
    ]

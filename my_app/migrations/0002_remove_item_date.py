# Generated by Django 3.1.2 on 2020-10-28 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='date',
        ),
    ]
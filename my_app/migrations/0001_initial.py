# Generated by Django 3.1.2 on 2020-10-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('qty', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 4.2.1 on 2023-07-01 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fathers_name',
            field=models.TextField(default='Rahim'),
        ),
    ]
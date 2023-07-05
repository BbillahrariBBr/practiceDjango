# Generated by Django 4.2.1 on 2023-07-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
                ('section', models.CharField(max_length=50)),
                ('payment', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

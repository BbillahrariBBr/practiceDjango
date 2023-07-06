# Generated by Django 4.2.1 on 2023-07-06 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_studentinfomodel_teacherinfomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerModels',
            fields=[
                ('employeemodels_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.employeemodels')),
                ('take_interview', models.BooleanField()),
                ('hiring', models.BooleanField()),
            ],
            bases=('first_app.employeemodels',),
        ),
    ]

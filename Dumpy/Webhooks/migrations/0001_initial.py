# Generated by Django 4.2.4 on 2023-08-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_no', models.IntegerField()),
                ('area', models.CharField(max_length=100)),
                ('sanitary_inspector', models.CharField(max_length=150)),
                ('sanitary_supervisor', models.CharField(max_length=150)),
            ],
        ),
    ]

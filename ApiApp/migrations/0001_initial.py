# Generated by Django 4.2 on 2023-05-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JADWAL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.CharField(max_length=50)),
                ('imsak', models.TimeField()),
                ('Subuh', models.TimeField()),
                ('terbit', models.TimeField()),
                ('duha', models.TimeField()),
                ('Zuhur', models.TimeField()),
                ('asar', models.TimeField()),
                ('magrib', models.TimeField()),
                ('isya', models.TimeField()),
            ],
        ),
    ]

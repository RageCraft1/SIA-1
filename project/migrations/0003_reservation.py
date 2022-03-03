# Generated by Django 3.2.9 on 2022-03-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_auto_20220223_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('resId', models.AutoField(primary_key=True, serialize=False)),
                ('availRooms', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('availTime', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.0.7 on 2018-08-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookingName', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=255)),
                ('PubName', models.CharField(max_length=255)),
            ],
        ),
    ]

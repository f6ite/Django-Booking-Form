# Generated by Django 3.1.4 on 2020-12-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detailsapp', '0016_auto_20201218_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='Time',
            field=models.CharField(blank=True, choices=[('9:00 - 9:30', '9:00 - 9:30'), ('9:31 - 10:00', '9:31 - 10:00'), ('10:31 - 11:00', '10:31 - 11:00'), ('11:01 - 11:30', '11:01 - 11:30'), ('11:31 - 12:30', '11:31 - 12:30'), ('12:31 - 13:00', '12:31 - 13:00'), ('13:01 - 13:30', '13:01 - 13:30'), ('13:31 - 14:00', '13:31 - 14:00'), ('14:01 - 14:30', '14:01 - 14:30'), ('14:31 - 15:00', '14:31 - 15:00'), ('15:01 - 15:30', '15:01 - 15:30'), ('15:31 - 16:00', '15:31 - 16:00'), ('16:01 - 16:30', '16:01 - 16:30'), ('16:31 - 17:00', '16:31 - 17:00'), ('17:01 - 17:30', '17:01 - 17:30'), ('17:31 - 18:00', '17:31 - 18:00')], default='09:00', help_text='Please select a time in 24hr clock format (HH:MM) from the drop down', max_length=13),
        ),
    ]

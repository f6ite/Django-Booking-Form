# Generated by Django 3.1.4 on 2020-12-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detailsapp', '0018_auto_20201218_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='Day',
            field=models.CharField(blank=True, choices=[('Monday', 'MONDAY'), ('Tuesday', 'TUESDAY'), ('Wednesday', 'WEDNESDAY'), ('Thursday', 'THURSDAY'), ('Friday', 'FRIDAY'), ('Saturday', 'SATURDAY'), ('Sunday', 'SUNDAY')], max_length=9),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='Email',
            field=models.EmailField(help_text='Please provide email in case of cancellation.', max_length=254),
        ),
    ]

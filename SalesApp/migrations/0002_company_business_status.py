# Generated by Django 4.0 on 2021-12-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='business_status',
            field=models.CharField(default='National', max_length=50),
        ),
    ]

# Generated by Django 4.0 on 2021-12-14 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30)),
                ('business_address', models.CharField(max_length=300)),
                ('business_product', models.TextField()),
                ('business_bank_account', models.CharField(max_length=30, null=True)),
                ('business_website', models.CharField(max_length=40, null=True)),
                ('business_contact_number', models.CharField(max_length=14, null=True)),
                ('business_contact_person', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30, null=True)),
                ('product_price', models.FloatField(default=0, null=True)),
                ('product_desc', models.CharField(max_length=300, null=True)),
                ('product_qty', models.IntegerField(default=1, null=True)),
                ('product_pic', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=30, null=True)),
                ('order_qty', models.IntegerField(default=1, null=True)),
                ('order_details', models.TextField()),
                ('payment_status', models.BooleanField(default=False)),
                ('order_total_price', models.FloatField(null=True)),
                ('customer_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalesApp.company')),
                ('order_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SalesApp.product')),
            ],
        ),
    ]

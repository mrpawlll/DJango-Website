# Generated by Django 4.1.5 on 2023-01-13 16:21

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('deliveryOrderID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('vendorName', models.CharField(max_length=30)),
                ('vendorAddress', models.CharField(max_length=200)),
                ('recipientName', models.CharField(max_length=30)),
                ('recipientPhone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('recipientAddress', models.CharField(max_length=200)),
                ('deliveryOrderStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('itemDescription', models.CharField(max_length=30)),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-15 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryorder', '0007_alter_deliveryorderform_deliveryorderdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryorderform',
            name='deliveryOrderDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='deliveryorderform',
            name='deliveryOrderStatus',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Disapproved'), (3, 'Approved')], default=1),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-28 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=255),
        ),
    ]

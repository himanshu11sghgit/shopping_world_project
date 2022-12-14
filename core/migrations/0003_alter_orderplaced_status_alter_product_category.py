# Generated by Django 4.0.3 on 2022-03-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_alter_customer_state_orderplaced_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On the way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('M', 'Mobile'), ('L', 'Laptop')], max_length=255),
        ),
    ]

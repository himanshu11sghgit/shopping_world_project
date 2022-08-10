# Generated by Django 4.0.3 on 2022-03-25 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('locality', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('pincode', models.IntegerField()),
                ('state', models.CharField(choices=[('A&NI', 'Andaman & Nicobar Islands'), ('AnP', 'Andhra Pradesh'), ('ArP', 'Arunachal Pradesh'), ('As', 'Assam'), ('Bh', 'Bihar'), ('Chd', 'Chandigarh'), ('Chat', 'Chhattisgarh'), ('D&NH', 'Dadra & Nagar Haveli'), ('D&D', 'Daman and Diu'), ('Dl', 'Delhi'), ('Go', 'Goa'), ('Guj', 'Gujarat'), ('Hr', 'Haryana'), ('HP', 'Himanchal Pradesh'), ('J&K', 'Jammu & Kashmir'), ('Jhk', 'Jharkhand'), ('Krn', 'Karnataka'), ('Ker', 'Kerala'), ('Lw', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('Mhr', 'Maharashtra'), ('Mnp', 'Manipur'), ('Meg', 'Meghalaya'), ('Miz', 'Mizoram'), ('Naga', 'Nagaland'), ('Od', 'Odisha'), ('Pudu', 'Puducherry'), ('Pb', 'Punjab'), ('Raj', 'Rajasthan'), ('Sik', 'Sikkim'), ('TN', 'Tamil Nadu'), ('Telg', 'Telangana'), ('Tri', 'Tripura'), ('Uttk', 'Uttarakhand'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal')], default='Not provided', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
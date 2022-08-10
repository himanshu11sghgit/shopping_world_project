from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinValueValidator

STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himanchal Pradesh', 'Himanchal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
)

class Customer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.IntegerField()
    state = models.CharField(max_length=50, choices=STATE_CHOICES)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
    ('M', 'Mobile'),
    ('L', 'Laptop'),
)

class Product(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=255)
    product_image = models.ImageField(upload_to='product_img')

    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

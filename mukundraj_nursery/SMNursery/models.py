from django.db import models

# Create your models here.
class cust_account(models.Model):
    address=models.TextField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    total_Order_number = models.IntegerField()


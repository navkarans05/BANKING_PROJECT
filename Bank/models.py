from django.db import models

# Create your models here.

class detail(models.Model):
    ifsc=models.CharField(max_length=100)
    bank_id=models.IntegerField()
    branch=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    bank_name=models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name

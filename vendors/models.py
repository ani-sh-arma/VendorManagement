from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

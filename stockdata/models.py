from django.db import models


# Create your models here.
class StockData(models.Model):
    title = models.TextField()
    content = models.TextField()


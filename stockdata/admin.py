from django.contrib import admin

# Register your models here.
from .models import StockData


class AdminStockData(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['id', 'title', 'content']

admin.site.register(StockData, AdminStockData)

from django.contrib import admin

from bill.models import Bill, PurchaseOfGoods

# Register your models here.
admin.site.register(Bill)
admin.site.register(PurchaseOfGoods)
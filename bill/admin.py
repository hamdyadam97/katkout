from django.contrib import admin
from bill.models import Bill, PurchaseOfGoods


class PurchaseOfGoodsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class BillAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Bill, BillAdmin)
admin.site.register(PurchaseOfGoods, PurchaseOfGoodsAdmin)

import uuid
from datetime import datetime, timedelta
from django.db import models
from client.models import Client
from client.utils import get_unique_slug
from project import settings
from user.models import User


class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,help_text="مسجل الفاتورة",on_delete=models.PROTECT,related_name="user_bill",)
    client = models.ForeignKey(Client, help_text="صاحب الفاتورة", on_delete=models.CASCADE,related_name="client_bill")
    payment = models.CharField(max_length=4, help_text="المدفوع من الفاتورة ")
    remaining_amount = models.CharField(max_length=4, help_text="الباقى من الفاتورة ")
    data_payment = models.DateTimeField(auto_now_add=True)
    data_remaining_amount = models.DateField(help_text="تاريخ تسديد باقى الفاتورة")




    def __str__(self):
        return self.client.name


class PurchaseOfGoods(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  help_text="مسجل بيع البضاعة", on_delete=models.PROTECT,related_name="user")
    client = models.ForeignKey(Client,  help_text="صاحب شراء البضاعة",on_delete=models.CASCADE,related_name="client",)
    bill = models.ForeignKey(Bill, related_name="bill", help_text="  رقم الفاتورة",
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=20, help_text="اسم البطاعة")
    number = models.CharField(max_length=20,help_text="عدد  البطاعة التى تم شراؤها")
    price = models.CharField(max_length=20,help_text=" سعر وحده من البضاعة التى تم شراؤها ")

    @property
    def price_total_number_purchase_of_goods(self):
        return float(self.number) * float(self.price)

    def __str__(self):
        return format(self.client.name + "بضاعة تم شرؤاها"+self.name)
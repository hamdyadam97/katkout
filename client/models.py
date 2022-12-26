import re
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from autoslug import AutoSlugField
from client.utils import get_unique_slug


def national_id(id):
    if id.isnumeric() and len(id) == 14:
        return id
    else:
        raise ValidationError('يجب ان يكون اربعة عشر رقم لاغير')


def validation_name(name):
    regx = '[\u0621-\u064A]+'
    if re.match(regx,name):
        return name
    else:
        raise ValidationError('اسم رسمى كما هو فى البطاقة')

    pass

def validation_phone(phone):
    regx = '^01[0125][0-9]{8}$'
    if re.match(regx, phone):
        return phone
    else:
        raise ValidationError("من فضلك رقم مناسب ")


class Client(models.Model):
    class ClientChoice(models.TextChoices):
        TRADE = 'trade', 'Trade',
        CUSTOMER = 'customer', 'Customer'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    national_id = models.CharField(max_length=14, unique=True, validators=[national_id],
                          help_text='الرقم القومى مكون من 14 رقم ')
    type = models.CharField(max_length=20, choices=ClientChoice.choices,default=ClientChoice.CUSTOMER,help_text="نوع العميل " )
    name = models.CharField(max_length=50, help_text='الاسم  يجب ان  يكون رسمى يدون تكرار', validators=[validation_name],unique=True)
    phone1 = models.CharField(unique=True, max_length=11, validators=[validation_phone], help_text="رقم الموبايل")
    phone2 = models.CharField(unique=True, max_length=11, validators=[validation_phone], null=True, blank=True, help_text="رقم الموبايل")
    place = models.CharField(max_length=50, null=True, blank=True, help_text="العنوان")
    img = models.ImageField(upload_to='client/image', default='F:/AppDjango/Katkout/media/client/image/Hamdy.JPG', help_text="الصورة ")


    def __str__(self):
        return self.name



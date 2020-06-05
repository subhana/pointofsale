# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Salesperson(models.Model):
    name = models.CharField(max_length=200, db_column='name')
    created_at = models.DateField(db_column='created_at')

    class Meta:
        db_table = "salesperson"
        

class Item(models.Model):
    description = models.CharField(max_length=50, db_column='description')
    price_bdt = models.IntegerField(db_column='price_bdt')
    created_at = models.DateField(db_column='created_at')

    class Meta:
        db_table = "item"


class Vat(models.Model):
    country = models.CharField(max_length=70, db_column='country')
    amount = models.IntegerField(db_column='amount')
    created_at = models.DateField(db_column='created_at')

    class Meta:
        db_table = "vat"


class Giftcard(models.Model):
    code = models.CharField(max_length=70, db_column='code')
    amount = models.IntegerField()
    description = models.CharField(max_length=70, db_column='description')
    used = models.IntegerField()
    created_at = models.DateField()

    class Meta:
        db_table = "giftcard"


class Orders(models.Model):
    invoice_no = models.CharField(max_length=100, db_column='invoice_no')
    salespersonid = models.ForeignKey(Salesperson, db_column='salespersonid')
    total = models.FloatField(max_length=70, db_column='total')
    vat = models.FloatField(db_column='vat')
    discount = models.FloatField(db_column='discount')
    final_total = models.FloatField(db_column='final_total')
    created_at = models.DateField(db_column='created_at')

    class Meta:
        db_table = "orders"


class Orderitem(models.Model):
    order_id = models.ForeignKey(Orders, db_column='order_id', on_delete=models.CASCADE)
    item_id = models.IntegerField(db_column='item_id')
    unit = models.IntegerField(db_column='unit')
    price_bdt = models.FloatField(db_column='price_bdt')
    discount = models.FloatField(db_column='discount')
    final_total = models.FloatField(db_column='final_total')
    created_at = models.DateField(db_column='created_at')

    class Meta:
        db_table = "orderitem"

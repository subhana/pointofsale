# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .dao import saveOrder, getItemsByOrderId, getAllOrders, searchOrdersByInvoiceno

def displayOrderList(request):
    print request.method
    if request.method == 'POST':
        orders = searchOrdersByInvoiceno(request.POST['invoiceno'])
    else:
        orders = getAllOrders()
    context = {'orders': orders}
    return render(request, 'main.html', context)

def createOrder(request):
    ordr = saveOrder()
    context = {}
    return render(request, 'createorder.html', context)

def displayOrderDetail(request, order_id):
    orderItemList, orderTotal, invoice_no = getItemsByOrderId(order_id)
    context = {
                'orderItems': orderItemList,
                'orderToal': orderTotal,
                'invoice_no': invoice_no
              }
    return render(request, 'orderdetail.html', context)

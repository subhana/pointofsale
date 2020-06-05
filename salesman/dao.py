import uuid
from md5 import md5
from datetime import datetime

from .models import Item, Vat, Giftcard, Salesperson, Orders, Orderitem

def getItemList():
    return Item.objects.all()

def prepareOrderList(orders):
    orderList = []
    for each in orders:
        order = {}
        order['id'] = each.id
        order['invoice_no'] = each.invoice_no
        order['total'] = each.total
        order['vat'] = each.vat
        order['discount'] = each.discount
        order['final_total'] = each.final_total
        orderList.append(order)
    return orderList

def getAllOrders():
    orders = Orders.objects.all()
    return prepareOrderList(orders)

def searchOrdersByInvoiceno(invoice_no):
    orders = Orders.objects.filter(invoice_no__icontains=invoice_no)
    return prepareOrderList(orders)


def saveOrderItems(ordr):
    items = Item.objects.all()[0:2]

    allTotal = 0
    for item in items:
        itemUnit = 2
        orderItem = Orderitem(order_id=ordr,
                              item_id=item.id,
                              unit=itemUnit,
                              price_bdt=item.price_bdt,
                              discount=0,
                              final_total=itemUnit*item.price_bdt,
                              created_at=getCurrentDatetime())
        orderItem.save()
        allTotal = allTotal + orderItem.final_total
    return allTotal


def getUniqueInvoiceNo():
    order_invoice = md5(str(uuid.uuid4())).hexdigest()
    return order_invoice[-12:]


def getCurrentDatetime():
    curr_date = datetime.now()
    curr_date.strftime("%Y-%m-%d %H:%M:%S")
    return curr_date


def saveOrder():
    ordr = Orders(invoice_no=getUniqueInvoiceNo(),
                  salespersonid=Salesperson.objects.get(id=1),
                  created_at=getCurrentDatetime())
    ordr.save()
    orderTotal = saveOrderItems(ordr)
    ordr.total = orderTotal
    ordr.vat = 0.07
    ordr.discount = 0
    ordr.final_total = ordr.total + (ordr.total*ordr.vat) - ordr.discount
    ordr.save()

def getItemsByOrderId(id):
    orderItemList = []
    orderTotal = 0
    invoice_no = Orders.objects.get(id=id).invoice_no
    orderItems = Orderitem.objects.filter(order_id=id)

    for orderItem in orderItems:
        orderItemDetail = {}
        item = Item.objects.get(id=orderItem.item_id)

        orderItemDetail['description'] = item.description
        orderItemDetail['unit'] = orderItem.unit
        orderItemDetail['price'] = orderItem.price_bdt
        orderItemDetail['discount'] = orderItem.discount
        orderItemDetail['total'] = orderItem.final_total

        orderItemList.append(orderItemDetail)
        orderTotal = orderTotal + orderItem.final_total
    return orderItemList, orderTotal, invoice_no
